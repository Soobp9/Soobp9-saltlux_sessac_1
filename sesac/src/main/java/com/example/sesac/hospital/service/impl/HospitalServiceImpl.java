package com.example.sesac.hospital.service.impl;

import com.example.sesac.hospital.db.entity.Hospital;
import com.example.sesac.hospital.db.repository.HospitalRepository;
import com.example.sesac.hospital.dto.HospitalDto;
import com.example.sesac.hospital.service.HospitalService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class HospitalServiceImpl implements HospitalService {

    private final HospitalRepository hospitalRepository;

    @Override
    public HospitalDto getHospital(Long hospitalId) {
        return hospitalRepository.findById(hospitalId).map(Hospital::toDto).orElseThrow();
    }

    @Override
    public List<HospitalDto> getAll() {
        return hospitalRepository.findAll().stream().map(Hospital::toDto).collect(Collectors.toList());
    }
}
