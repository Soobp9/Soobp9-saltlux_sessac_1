package com.example.sesac.review.db.entity;

import com.example.sesac.review.dto.ReviewSumDto;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
@Getter
public class ReviewSum {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long sumId;
//    @ManyToOne
//    @JoinColumn(name = "hospital_id")
//    private Hospital hospital;

    private Long positiveReviewCnt;
    private Long negativeReviewCnt;
    private Long reviewTotalCnt;
    private double positivePercentage;
    private double negativePercentage;


    @Builder
    public ReviewSum(Long sumId, Long positiveReviewCnt, Long negativeReviewCnt, Long reviewTotalCnt, double positivePercentage, double negativePercentage) {
        this.sumId = getSumId();
        this.positiveReviewCnt = getPositiveReviewCnt();
        this.negativeReviewCnt = getNegativeReviewCnt();
        this.reviewTotalCnt = getReviewTotalCnt();
        this.positivePercentage = getPositivePercentage();
        this.negativePercentage = getNegativePercentage();
    }

    public static ReviewSumDto toDto(ReviewSum reviewsum) {
        return ReviewSumDto.builder()
                .sumId(reviewsum.getSumId())
                .positiveReviewCnt(reviewsum.getPositiveReviewCnt())
                .negativeReviewCnt(reviewsum.getNegativeReviewCnt())
                .reviewTotalCnt(reviewsum.getReviewTotalCnt())
                .positivePercentage(reviewsum.getPositivePercentage())
                .negativePercentage(reviewsum.getNegativePercentage())
                .build();
    }

    public static ReviewSum toEntity(ReviewSumDto reviewSumDto) {
        return ReviewSum.builder()
                .sumId(reviewSumDto.getSumId())
                .positiveReviewCnt(reviewSumDto.getPositiveReviewCnt())
                .negativeReviewCnt(reviewSumDto.getNegativeReviewCnt())
                .reviewTotalCnt(reviewSumDto.getReviewTotalCnt())
                .positivePercentage(reviewSumDto.getPositivePercentage())
                .negativePercentage(reviewSumDto.getNegativePercentage())
                .build();
    }
}



