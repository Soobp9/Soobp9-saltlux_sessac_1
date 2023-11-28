package com.example.sesac.sign.db.entity;


import com.example.sesac.sign.dto.UserDto;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
@Getter
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userSequence;
    private String userId;
    private String userPw;
    private String userAddr;
    private String userTell;
    private String userGender;
    private String userEmail;

    //가입날짜, 생일, ... 추가 필요!

    public static UserDto toDto(User user){
        return UserDto.builder()
                .userSequence(user.getUserSequence())
                .userId(user.getUserId())
                .userPw(user.getUserPw())
                .userAddr(user.getUserAddr())
                .userTell(user.getUserTell())
                .userGender(user.getUserGender())
                .userEmail(user.getUserEmail())
                .build();
    }

    public static User toEntity(UserDto userDto){
        return User.builder()
                .userId(userDto.getUserId())
                .userPw(userDto.getUserPw())
                .userAddr(userDto.getUserAddr())
                .userTell(userDto.getUserTell())
                .userGender(userDto.getUserGender())
                .userEmail(userDto.getUserEmail())
                .build();
    }

    @Builder
    public User(Long userSequence, String userId, String userPw, String userAddr
            , String userTell, String userGender, String userEmail){
        this.userSequence = userSequence;
        this.userId = userId;
        this.userPw = userPw;
        this.userAddr = userAddr;
        this.userTell = userTell;
        this.userGender = userGender;
        this.userEmail = userEmail;
    }




}
