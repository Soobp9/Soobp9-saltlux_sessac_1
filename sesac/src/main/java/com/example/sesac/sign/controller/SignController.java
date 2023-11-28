package com.example.sesac.sign.controller;


import com.example.sesac.sign.dto.LoginDto;
import com.example.sesac.sign.dto.UserDto;
import com.example.sesac.sign.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("Sign")
@RequiredArgsConstructor
public class SignController {
    private final UserService userService;
    private static final String SUCCESS = "success";
    private static final String FAIL = "fail";

    
    
    //회원 등록
    @PostMapping
    public ResponseEntity<String> createUser(@RequestBody UserDto userDto){
        userService.createUser(userDto);
        return new ResponseEntity<>(SUCCESS, HttpStatus.OK);

    }

    //로그인
//    @PostMapping("/login")
//    public ResponseEntity<String> login(@RequestBody LoginDto loginDto){
//
//
//    }

}
