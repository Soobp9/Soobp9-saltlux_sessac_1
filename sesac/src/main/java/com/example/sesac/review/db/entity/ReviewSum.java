package com.example.sesac.review.db.entity;

import com.example.sesac.hospital.db.entity.Hospital;
import com.example.sesac.review.dto.ReviewSumDto;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;

@Entity
@NoArgsConstructor
@Getter
public class ReviewSum {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long sumId;

    @ManyToOne
    @JoinColumn(name = "hospital_id", insertable = false, updatable = false)
    private Hospital hospital;

    private Long positiveReviewCnt;
    private Long negativeReviewCnt;
    private Long reviewTotalCnt;
    private double positivePercentage;
    private double negativePercentage;

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



