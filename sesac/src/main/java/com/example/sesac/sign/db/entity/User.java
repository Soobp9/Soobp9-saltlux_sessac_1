package com.example.sesac.sign.db.entity;


import com.example.sesac.sign.dto.UserDto;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.hibernate.annotations.DynamicInsert;

@Entity
@NoArgsConstructor
@DynamicInsert
@Getter
@Slf4j
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userSequence;
    private String userId;
    private String userPw;
    private String userName;
    private String userEmail;
    private String userGender;

//    @ColumnDefault("`users`")
//    private String role;

    //가입날짜, 생일, ... 추가 필요!

    @Builder
    public User(Long userSequence, String userId, String userPw
            , String userName, String userEmail, String userGender) {
        this.userSequence = userSequence;
        this.userId = userId;
        this.userPw = userPw;
        this.userName = userName;
        this.userEmail = userEmail;
        this.userGender = userGender;
    }

    public static UserDto toDto(User user) {
        return UserDto.builder()
                .userSequence(user.getUserSequence())
                .userId(user.getUserId())
                .userPw(user.getUserPw())
                .userName(user.getUserName())
                .userEmail(user.getUserEmail())
                .userGender(user.getUserGender())
                .build();
    }

    public static User toEntity(UserDto userDto) {
        return User.builder()
                .userId(userDto.getUserId())
                .userPw(userDto.getUserPw())
                .userName(userDto.getUserName())
                .userEmail(userDto.getUserEmail())
                .userGender(userDto.getUserGender())
                .build();
    }


}
