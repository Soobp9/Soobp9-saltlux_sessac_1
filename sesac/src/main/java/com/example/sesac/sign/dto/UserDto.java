package com.example.sesac.sign.dto;

import lombok.Builder;
import lombok.Getter;

@Getter
public class UserDto {
    private Long userSequence;
    private String userId;
    private String userPw;
    private String userName;
    private String userEmail;
    private String userGender;

//    private String userAddr;
//    private String userTell;


    @Builder
    public UserDto(Long userSequence, String userId, String userPw
            , String userName, String userEmail, String userGender) {
        this.userSequence = userSequence;
        this.userId = userId;
        this.userPw = userPw;
        this.userName = userName;
        this.userGender = userGender;
        this.userEmail = userEmail;
    }


}
