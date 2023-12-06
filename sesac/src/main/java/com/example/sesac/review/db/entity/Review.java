package com.example.sesac.review.db.entity;

import com.example.sesac.review.dto.ReviewDto;
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
public class Review {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long reviewId;

//    @ManyToOne
//    @JoinColumn(name = "hospital_id")
//    private Hospital hospital;
//
//    private String hospitalName;

    private String reviewPositive;
    private String reviewNegative;
    private Long reviewCount;


    @Builder
    public Review(Long reviewId, String hospitalName, String reviewPositive, String reviewNegative, Long reviewCount) {
        this.reviewId = getReviewId();
//        this.hospitalName = getHospitalName();
        this.reviewPositive = getReviewPositive();
        this.reviewNegative = getReviewNegative();
        this.reviewCount = getReviewCount();
    }

    public static Review toDto(Review review) {
        return Review.builder()
                .reviewId(review.getReviewId())
//                .hospitalName(review.getHospitalName())
                .reviewPositive(review.getReviewPositive())
                .reviewNegative(review.getReviewNegative())
                .reviewCount(review.getReviewCount())
                .build();
    }

    public static ReviewDto toEntity(ReviewDto reviewDto) {
        return ReviewDto.builder()
                .reviewId((reviewDto.getReviewId()))
                .hospitalName((reviewDto.getHospitalName()))
                .reviewPositive(reviewDto.getReviewPositive())
                .reviewNegative(reviewDto.getReviewNegative())
                .reviewCount(reviewDto.getReviewCount())
                .build();
    }
}



