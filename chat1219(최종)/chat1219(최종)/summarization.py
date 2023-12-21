# <summarization.py>

import openai
import os
from dotenv import load_dotenv

# .env 파일에서 API 키를 가져옴
api_key = os.getenv("OPENAI_API_KEY")

# API 키를 사용하여 OpenAI 객체 생성
client = openai.ChatCompletion.create(api_key=api_key)

def summarize_conversation(conversation_history, model='gpt-3.5-turbo-1106', temperature=0.4, max_tokens=150):
    """
    Summarizes the conversation history using OpenAI's GPT-3.5-turbo model.

    Parameters:
    - conversation_history (list of dict): A list of message dictionaries with 'role' and 'content'.
    - model (str): The OpenAI model to use for summarization.
    - temperature (float): The temperature to use for the AI response.
    - max_tokens (int): The maximum number of tokens to use in the response.

    Returns:
    - str: A summary of the conversation.
    """

    # Convert the conversation history into a string
    conversation_str = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation_history])

    # Prepare the prompt for summarization
    prompt = f"Summarize the following conversation:\n{conversation_str}"

    try:
        # Generate the summary using OpenAI's GPT-3.5-turbo model
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )

        summary = response.choices[0].message.content
        return summary

    except Exception as e:
        print(f"Error during OpenAI API call for summarization: {e}")
        return "Unable to generate summary at this time."

