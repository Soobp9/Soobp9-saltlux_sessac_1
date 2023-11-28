package com.example.sesac.sign.service;

import com.example.sesac.sign.dto.LoginDto;
import com.example.sesac.sign.dto.UserDto;



public interface UserService {
    
    //회원 생성
    void createUser(UserDto userDto);
    
    //DB에서 가입한 회원ID가 있는지 조회
//    void selectUserId(LoginDto userId);
}
