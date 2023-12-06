package com.example.sesac.review.dto;

import lombok.Builder;
import lombok.Getter;

@Getter
public class ReviewDto {
    private Long reviewId;
    private String hospitalName;
    private String reviewPositive;
    private String reviewNegative;
    private Long reviewCount;

    @Builder
    public ReviewDto(Long reviewId, String hospitalName
            , String reviewPositive, String reviewNegative, Long reviewCount) {
        this.reviewId = getReviewId();
        this.hospitalName = getHospitalName();
        this.reviewPositive = getReviewPositive();
        this.reviewNegative = getReviewNegative();
        this.reviewCount = getReviewCount();

    }
}

