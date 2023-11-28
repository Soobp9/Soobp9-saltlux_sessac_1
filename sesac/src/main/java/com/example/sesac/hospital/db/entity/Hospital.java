package com.example.sesac.hospital.db.entity;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Hospital {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long hospitalId;

    private String hospitalName;
    private String hospitalAddress;
    private String hospitalTell;
    private String department; // 진료과

    // 기본 생성자
    public Hospital(){
    }

    // 파라미터를 받는 생성자
    public Hospital(String name, String address, String phoneNumber, String department) {
        this.hospitalName = name;
        this.hospitalAddress = address;
        this.hospitalTell = phoneNumber;
        this.department = department;
    }
}
