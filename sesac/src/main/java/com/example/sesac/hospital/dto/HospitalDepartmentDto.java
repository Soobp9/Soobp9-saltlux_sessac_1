package com.example.sesac.hospital.dto;

import lombok.Builder;
import lombok.Getter;

@Getter
public class HospitalDepartmentDto {
    private Long departmentId;
    //hospitalId;
    private String hospital_middle;
    private String hospital_major;


    @Builder
    public HospitalDepartmentDto(Long departmentId, String hospital_middle, String hospital_major) {
        this.departmentId = departmentId;
        this.hospital_middle = hospital_middle;
        this.hospital_major = hospital_major;
    }
}
