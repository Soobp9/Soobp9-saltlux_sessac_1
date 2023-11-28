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
    public HospitalDto(Long hospitalId, String name, String address, String Tell, String department) {
        this.hospitalId = hospitalId;
        this.hospitalName = name;
        this.hospitalAddress = address;
        this.hospitalTell = Tell;
        this.department = department;
    }
}
