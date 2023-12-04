package com.example.sesac.sign.dto;


import lombok.Builder;
import lombok.Getter;

@Getter
public class LoginDto {
    private String userId;
    private String userPw;

    @Builder
    public LoginDto(String userId, String userPw){
        this.userId = userId;
        this.userPw = userPw;
    }
}
