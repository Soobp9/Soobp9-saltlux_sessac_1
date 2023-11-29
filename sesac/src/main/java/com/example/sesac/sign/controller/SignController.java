package com.example.sesac.sign.controller;


import com.example.sesac.sign.dto.LoginDto;
import com.example.sesac.sign.dto.UserDto;
import com.example.sesac.sign.service.UserService;
import jakarta.servlet.http.HttpSession;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("sign")
@RequiredArgsConstructor
public class SignController {
    private static final String SUCCESS = "success";
    private static final String FAIL = "fail";
    private final UserService userService;

    //회원 등록
    @PostMapping
    public ResponseEntity<String> createUser(@RequestBody UserDto userDto) {
        userService.createUser(userDto);
        return new ResponseEntity<>(SUCCESS, HttpStatus.OK);

    }

    //로그인
    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestBody LoginDto loginDto, HttpSession session) {

        UserDto user = userService.loginUser(loginDto);
        if (user != null && user.getUserPw().equals(loginDto.getUserPw())) {
            //로그인 성공
            session.setAttribute("userId", user.getUserId());
            return new ResponseEntity<>(SUCCESS, HttpStatus.OK);
        } else {
            return new ResponseEntity<>(FAIL, HttpStatus.OK);
        }

    }

}
