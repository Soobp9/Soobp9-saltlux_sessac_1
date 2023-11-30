package com.example.sesac.mypage.controller;

import com.example.sesac.sign.dto.UserDto;
import com.example.sesac.sign.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequiredArgsConstructor
@RequestMapping("mypage")
public class MypageController {

    private final UserService userService;

    //회원 정보 조회
    @GetMapping("{userId}")
    public ResponseEntity<UserDto> getUserInfo(@PathVariable String userId) {
        return new ResponseEntity<>(userService.getUserInfo(userId), HttpStatus.OK);

    }
}
