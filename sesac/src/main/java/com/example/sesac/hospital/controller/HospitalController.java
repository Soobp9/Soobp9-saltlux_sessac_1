package com.example.sesac.hospital.controller;

import com.example.sesac.hospital.db.entity.Hospital;
import com.example.sesac.hospital.service.HospitalService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/hospitals")
public class HospitalController {
    private final HospitalService hospitalService;

    @Autowired
    public HospitalController(HospitalService hospitalService) {
        this.hospitalService = hospitalService;
    }

    // 모든 병원 정보 조회
    @GetMapping
    public List<Hospital> getAllHospitals() {
        return hospitalService.getAllHospitals();
    }

    // 특정 병원 정보 조회
    @GetMapping("/{hospitalId}")
    public Hospital getHospitalById(@PathVariable Long hospitalId) {
        return hospitalService.getHospitalById(hospitalId);
    }
}