package com.example.sesac.hospital.service;

import com.example.sesac.hospital.db.entity.Hospital;

import java.util.List;

public interface HospitalService {
    List<Hospital> getAllHospitals();
    Hospital getHospitalById(Long hospitalId);
}
