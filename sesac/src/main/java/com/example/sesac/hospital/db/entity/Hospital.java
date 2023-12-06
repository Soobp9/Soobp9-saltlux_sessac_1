package com.example.sesac.hospital.db.entity;

import com.example.sesac.hospital.dto.HospitalDto;
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
public class Hospital {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long hospitalId;

    private String hospitalName;
    private String hospitalAddress;
    private String hospitalTell;
    private String hospitalDepartment;


    @Builder
    public Hospital(Long hospitalId, String hospitalName, String hospitalAddress, String hospitalTell, String hospitalDepartment) {
        this.hospitalName = hospitalName;
        this.hospitalAddress = hospitalAddress;
        this.hospitalTell = hospitalTell;
        this.hospitalDepartment = hospitalDepartment;
    }

    public static HospitalDto toDto(Hospital hospital) {
        return HospitalDto.builder()
                .hospitalId(hospital.getHospitalId())
                .hospitalName(hospital.getHospitalName())
                .hospitalAddress(hospital.getHospitalAddress())
                .hospitalTell(hospital.getHospitalTell())
                .hospitalDepartment(hospital.getHospitalDepartment())
                .build();
    }

    public static Hospital toEntity(HospitalDto hospitalDto) {
        return Hospital.builder()
                .hospitalName(hospitalDto.getHospitalName())
                .hospitalAddress(hospitalDto.getHospitalAddress())
                .hospitalTell(hospitalDto.getHospitalTell())
                .hospitalDepartment(hospitalDto.getHospitalDepartment())
                .build();
    }
}

