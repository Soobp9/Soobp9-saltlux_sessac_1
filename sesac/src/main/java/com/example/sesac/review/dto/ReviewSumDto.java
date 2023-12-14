package com.example.sesac.review.dto;

import jakarta.persistence.Id;
import lombok.Builder;
import lombok.Getter;

@Getter
public class ReviewSumDto {
    @Id
    private Long sumId;
    private Long positiveReviewCnt;
    private Long negativeReviewCnt;
    private Long reviewTotalCnt;
    private double positivePercentage;
    private double negativePercentage;

    @Builder
    public ReviewSumDto(Long sumId, Long hospitalId, String hospitalName
            , Long positiveReviewCnt, Long negativeReviewCnt, Long reviewTotalCnt
            , double positivePercentage, double negativePercentage) {
        this.sumId = sumId;
        this.hospitalId = hospitalId;
        this.hospitalName = hospitalName;
        this.positiveReviewCnt = positiveReviewCnt;
        this.negativeReviewCnt = negativeReviewCnt;
        this.reviewTotalCnt = reviewTotalCnt;
        this.positivePercentage = positivePercentage;
        this.negativePercentage = negativePercentage;
    }
}

