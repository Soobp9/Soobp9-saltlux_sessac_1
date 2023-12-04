package com.example.sesac.hospital.dto;

import lombok.Builder;
import lombok.Data;

@Data
public class HospitalDto {
    private Long hospitalId;
    private String hospitalName;
    private String hospitalAddress;
    private String hospitalTell;
    private String department;

    @Builder
    public HospitalDto(Long hospitalId, String hospitalName, String hospitalAddress, String hospitalTell, String department) {
        this.hospitalId = hospitalId;
        this.hospitalName = hospitalName;
        this.hospitalAddress = hospitalAddress;
        this.hospitalTell = hospitalTell;
        this.department = department;
    }
}
