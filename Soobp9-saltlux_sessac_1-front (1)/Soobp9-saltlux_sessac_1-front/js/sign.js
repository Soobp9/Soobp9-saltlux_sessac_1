// const input = document.getElementById('#userId').val;
// alert(input);

const loginBtn = document.getElementById('form_btn');
const joinBtn = document.getElementById('join_btn');


//로그인 버튼 클릭 시 실행
loginBtn.addEventListener('click', (event) => {
    event.preventDefault();
    
    const loginDto = {
        "userId" : $('#signId').val(),
        "userPw" : $('#signPw').val()
    };


    $.ajax({
        type: 'POST',
        url: 'http://localhost:8080/sign/login',
        // dataType: 'json', // 서버에서 준 데이터 형식
        contentType: 'application/json',
        data: JSON.stringify(loginDto),
        success: function (result) {
            if(result == 'success'){
                console.log(result)
                alert('로그인 성공')
                // console.log(result)
                location.href = '/html/chatbot.html'
            }
            else{
                alert('잘못 입력되었습니다. \n회원 정보를 다시 확인해 주세요')
                location.href = '/html/sign.html'
            } 
        },
        error: function (result, status, error) {
            console.log(error)
        }
    });
});


//회원가입 버튼 클릭 시 실행
joinBtn.addEventListener('click', (event) => {
    event.preventDefault();
   
   
    const userDto = {
        "userId" : $('#userId').val(),
        "userPw" : $('#userPw').val(),
        "userName" : $('#userName').val(),
        "userEmail" : $('#userEmail').val(),
        "userGender" : $('#userGender').val(),
    };

    alert(userDto)
    console.log(userDto)

    $.ajax({
        type: 'POST',
        url: 'http://localhost:8080/sign',
        // dataType: 'json', // 서버에서 준 데이터 형식
        contentType: 'application/json',
        data: JSON.stringify(userDto),
        success: function (result) {
            if(result == 'success'){
                console.log(result)
                alert('회원가입 성공')
                // console.log(result)
                location.href = '/html/sign.html'
            }
            else{
                alert('가입에 실패했습니다. \n정보를 다시 확인해 주세요')
                location.href = '/html/sign.html'
            } 
        },
        error: function (result, status, error) {
            console.log(error)
        }
    });
    



});





// function logIn(){
    
//     // const userId  = document.getElementById('userId').value;
//     // const userPw  = document.getElementById('userPw').value;
//     console.log( $('#userId').val());
//     console.log( $('#userPw').val());
//     const loginDto = {
//         "userId" : $('#userId').val(),
//         "userPw" : $('#userPw').val()
//     }

//     // $.ajax({
//     //     url: 'http://localhost:8080/sign/login', 
//     //      type: 'post',
//     //      dataType: 'json',
//     //     contentType: 'application/json',
//     //      data: JSON.stringify(loginDto), 
//     //      success: function(result) {
//     //      //	 alert(wishCode);
//     //           if(result == 'SUCCESS'){
//     //              alert('로그인 성공');
//     //            }
//     //           else{
//     //              alert('로그인 실패');
//     //            }
//     //         //   location.href = `/item/itemDetail?itemCode=${itemCode}`;
//     //      },
//     //      error: function(){
//     //         alert('실패');
//     //      }
//     //  });


//      $.ajax({
//         type: 'POST',
//         url: 'http://localhost:8080/sign/login',
//         dataType: 'json',
//         contentType: 'application/json',
//         data: JSON.stringify(loginDto),
//         success: function (result) {
//             alert('로그인 성공')
//             console.log(result)
//         },
//         error: function (result, status, error) {
//             console.log(error)
//         }
//     })
    
// }






const signUpBtn = document.getElementById("signUp");
const signInBtn = document.getElementById("signIn");
const container = document.querySelector(".container");

signUpBtn.addEventListener("click", () => {
    container.classList.add("right-panel-active");
});
signInBtn.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
});

