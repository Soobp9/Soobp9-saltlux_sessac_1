package com.example.sesac.sign.service.impl;

import com.example.sesac.sign.db.entity.User;
import com.example.sesac.sign.db.repository.UserRepository;
import com.example.sesac.sign.dto.LoginDto;
import com.example.sesac.sign.dto.UserDto;
import com.example.sesac.sign.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {

    private final UserRepository userRepository;
    @Override
    public void createUser(UserDto userDto){
        userRepository.save(User.toEntity(userDto));

    }
//    @Override
//    public void selectUserId(LoginDto userId){
//        return userRepository.findAllById(userId).map(User::toDto).orElseThrow();
//    }


}
