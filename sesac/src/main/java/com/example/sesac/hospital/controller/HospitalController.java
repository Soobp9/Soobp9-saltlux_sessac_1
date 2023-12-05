package com.example.sesac.hospital.controller;

import com.example.sesac.hospital.dto.HospitalDto;
import com.example.sesac.hospital.service.HospitalService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("hospital")
@RequiredArgsConstructor
@Slf4j
public class HospitalController {
    private final HospitalService hospitalService;

    // 특정 병원 정보 조회
//    @GetMapping("{hospitalId}")
//    public ResponseEntity<HospitalDto> getOneHospital(@PathVariable Long hospitalId) {
//        return new ResponseEntity<>(hospitalService.getHospital(hospitalId), HttpStatus.OK);
//    }
//
//    // 모든 병원 정보 조회
//    @GetMapping
//    public ResponseEntity<List<HospitalDto>> getAllHospitals() {
//        return new ResponseEntity<>(hospitalService.getAll(), HttpStatus.OK);
//    }

    // 특정 진료과로 병원 정보 조회
    @GetMapping
    public ResponseEntity<List<HospitalDto>> findAllByDepartment(@RequestParam String department) {
        return new ResponseEntity<>(hospitalService.getHospitalList(department), HttpStatus.OK);
        
    }


}
