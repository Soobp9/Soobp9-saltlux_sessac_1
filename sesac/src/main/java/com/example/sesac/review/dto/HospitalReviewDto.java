package com.example.sesac.review.dto;

import jakarta.persistence.Id;
import lombok.Builder;
import lombok.Getter;

@Getter
public class HospitalReviewDto {
    @Id
    private Long departmentId;
    //hospitalId;
    private String hospital_middle;
    private String hospital_major;

    @Builder
    public HospitalReviewDto(Long departmentId, String hospital_middle, String hospital_major) {
        this.departmentId = departmentId;
        this.hospital_middle = hospital_middle;
        this.hospital_major = hospital_major;
    }
}
