package com.example.sesac.sign.dto;

import lombok.Getter;
import lombok.NoArgsConstructor;

@Getter
@NoArgsConstructor
public class LoginResp {
    String result;
    Long userId;

    public LoginResp(String result, Long userId) {
        this.result = result;
        this.userId = userId;
    }

    public LoginResp(String result) {
        this.result = result;
    }
}
