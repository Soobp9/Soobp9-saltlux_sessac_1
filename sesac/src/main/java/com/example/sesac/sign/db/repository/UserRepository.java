package com.example.sesac.sign.db.repository;

import com.example.sesac.sign.db.entity.User;
import org.springframework.data.jpa.repository.JpaRepository;

public interface UserRepository extends JpaRepository<User, Long> {
}
