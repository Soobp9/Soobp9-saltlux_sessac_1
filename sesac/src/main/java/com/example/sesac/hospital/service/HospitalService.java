package com.example.sesac.hospital.service;

import com.example.sesac.hospital.db.entity.Hospital;
import com.example.sesac.hospital.dto.HospitalDto;

import java.util.List;

public interface HospitalService {

    HospitalDto getHospital(Long hospitalId);

    List<HospitalDto> getAll();
}
