import json
import os
import random

from flask import jsonify, request
from openai import OpenAI
import urllib.request
import ray
from ray.util import inspect_serializability
import threading
import requests
import asyncio
import datetime
# from models import predict_seg

from concurrent.futures import ThreadPoolExecutor

lock = threading.Lock()

def get_openai_key():
    key = None
    try:
        # 개발시 로컬파일
        # openai_key.json 파일을 읽어서 "OPENAI_API_KEY" 키값 획득
        
        key_path = "openai_key.json"
        with open(key_path) as f:
            data = json.load(f)
            # print( data['OPENAI_API_KEY'][:5] )
        key = data['OPENAI_API_KEY']
    except Exception:
        # AWS Lambda의 환경변수
        key = os.environ['OPENAI_API_KEY']
    return key


client = OpenAI(api_key=get_openai_key())

def moderate_prompt(prompt: str) -> str:
    prompt_prefix = "Front view, Full body shot"
    prompt_suffix = "High Noon, 16k uhd, ultra-realistic, soft lighting, film grain, Fujifilm XT3"

    negative_prefix = 'Do not draw as below'
    negative_suffix = "(deformed iris, deformed pupils, semi-realistic, cgi, 3d, render, sketch, cartoon, drawing, anime:1.4), \
        text, close up, cropped, out of frame, worst quality, low quality, jpeg artifacts, ugly, duplicate, morbid, mutilated, \
        extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, dehydrated, bad anatomy, \
        bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, \
        extra arms, extra legs, fused fingers, too many fingers, long neck"

    negative_prompt = "".join([negative_prefix + prompt + negative_suffix])

    return ", ".join([prompt.replace('.', ''), prompt_prefix, prompt_suffix, ]).strip() + "\n" + negative_prompt


def generate_image_sync(prompt):
    print('call create img')
    local_client = OpenAI(api_key=get_openai_key())
    get_image = local_client.images.generate(
        model='dall-e-3',
        prompt=prompt,
        size='1024x1024',
        quality='standard',
        n=1,
    )

    img = get_image.data[0].url
    title = img.split('/img-')[1].split('.png')[0]
    save_path = 'static/images/created_image/'+title+'.png'
    print(img)
    urllib.request.urlretrieve(img, save_path)
    
    # predict_seg(title)
    
    return img

# 달리 병렬
async def dalle(prompt):
  
    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor() as pool:
        save_path = await loop.run_in_executor(pool,generate_image_sync,prompt)
        
    return save_path

def current_season():
    season = "Autumn"
    
    today = datetime.date.today()
    m = today.month
    if m in [12,1,2]:
        season = "Winter"
    elif m in [3,4,5]:
        season = "Spring"
    elif m in [6,7,8]:
        season = "Summer"
        
    print(m,season)
    
    return season

user_data = {"age":"20" , 'gender' : 'female' , 'body_type' : 'normal'}
age , gender , body_type = user_data.values()
season = current_season()
gpt_system_prompt = f"""
You're a chatbot that helps people choose what to wear today. According to the user's fashion taste, you need to help them choose the right outfit and print it out as an image. To make outfit recommendations, you need the following information.
< base conditions : don't ask > 
- nation: korean
- season : {season} 
- age : {age} 
- gender : {gender}
- body type : {body_type}
<required conditions>
- Situation (example : go on a date, go to a cafe, have an interview, go to work ...  )
- Clothing preferences ( example : streat fashion , casual fashion , dark or bright color)
To create a prompt to generate an image, the process is as follows:
1. Collect information from the user by asking the required conditions.
2. Once you have enough information, complete the prompt as shown below:
Example prompt:"Draw only 1 character,The character must be stand and include shoes and pants,realistic,8k uhd,soft lighting,high quality,20s Korean woman with a chubby body type,looking straight ahead, She is dressed in warm , the fashion is suitable for colder weather and going to work,The style should be cozy yet work-appropriate. "
3. pass the completed prompt as an argument to call the `dalle` function.
4. You must answer in Korean for user but final prompt you requried must be in English.
5. You don't have to explain about function or prompt to the user
6. The prompt should be no more than 400 characters long
"""

state = ([{
    "role": "system",
    "content": gpt_system_prompt
}])

state_chatbot = ([])

async def answer(text):
       
    global state
    global state_chatbot
    print("chatbot", text)

    messages = state + [
        {"role": "user", "content": text}
    ]

    completion = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.8,
        max_tokens=2048,
        functions=[{
            "name": "dalle",
            "description": "Generate an outfit image from prompt.",
            "parameters": {
                "type": "object",
                "properties": {
                    "prompt": {
                        "type": "string",
                        "description": "Prompt that generate an outfit image",
                    },
                },
                "required": ["prompt"],
            },
        }],
        function_call="auto"

    )

    message_result = completion.choices[0].message.content if completion.choices[0].message.content else ""

    new_state = [{
        "role": "user",
        "content": text
    }, {
        "role": "assistant",
        "content": message_result
    }]

    state = state + new_state
    final_prompt = ""
    saved_three_image_url = None
    function = completion.choices[0].message.function_call
    
    if function:
        final_prompt += function.arguments.replace("\n", "").split(":")[1][:-1].replace("\"", "")
        state = ([{
            "role": "system",
            "content": gpt_system_prompt
        }])
        state_chatbot = ([])
        print(final_prompt)
        # final_prompt = moderate_prompt(final_prompt)
        print("final : ", final_prompt)
        
        try:
            saved_three_image_url = await asyncio.gather(
                dalle(final_prompt),
                dalle(final_prompt),
                dalle(final_prompt)
            )
            
        except Exception as e:
            print("An error occurred:",e)
        
        message_result = ""
        message_result += "created"
        final_img = saved_three_image_url

    else:
        state_chatbot = state_chatbot + [(text, message_result)]
        final_img = []

    print("result", message_result)
    print("state", state)
    print("state_chatbot", state_chatbot)

    return jsonify({"result": message_result, "state": state, "state_chatbot": state_chatbot,"final_img":final_img})