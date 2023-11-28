package com.example.sesac.sign.dto;

import lombok.Builder;
import lombok.Getter;

@Getter
public class UserDto {
    private Long userSequence;
    private String userId;
    private String userPw;
    private String userAddr;
    private String userTell;
    private String userGender;
    private String userEmail;


    @Builder
    public UserDto(Long userSequence, String userId, String userPw
                    , String userAddr, String userTell, String userGender, String userEmail) {
        this.userSequence = userSequence;
        this.userId = userId;
        this.userPw = userPw;
        this.userAddr =  userAddr;
        this.userTell = userTell;
        this.userGender = userGender;
        this.userEmail = userEmail;
    }



}
