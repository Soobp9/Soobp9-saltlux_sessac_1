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
    public ReviewSumDto(Long sumId, Long positiveReviewCnt, Long negativeReviewCnt
            , Long reviewTotalCnt, double positivePercentage, double negativePercentage) {
        this.sumId = getSumId();
        this.positiveReviewCnt = getPositiveReviewCnt();
        this.negativeReviewCnt = getNegativeReviewCnt();
        this.reviewTotalCnt = getReviewTotalCnt();
        this.positivePercentage = getPositivePercentage();
        this.negativePercentage = getNegativePercentage();

    }
}

