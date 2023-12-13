package com.example.sesac.review.db.entity;

import lombok.Builder;

public class HospitalReview {
    private Long departmentId;
    //hospitalId;
    private String hospital_middle;
    private String hospital_major;

    @Builder
    public HospitalReview(Long departmentId, String hospital_middle, String hospital_major) {
        this.departmentId = departmentId;
        this.hospital_middle = hospital_middle;
        this.hospital_major = hospital_major;
    }

//    public static HospitalReviewDto toDto(HospitalReview hospitalReview){
//        return HospitalReviewDto.builder()
//                .departmentId(hospitalReview.get)
//    }


}
