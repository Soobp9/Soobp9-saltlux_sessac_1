package com.example.sesac.hospital.db.entity;

import com.example.sesac.hospital.dto.HospitalDto;
import jakarta.persistence.*;
import lombok.Builder;
import lombok.Getter;
import lombok.NoArgsConstructor;
import org.hibernate.annotations.DynamicInsert;

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
    private String department;


    public static HospitalDto toDto(Hospital hospital) {
        return HospitalDto.builder()
                .hospitalId(hospital.getHospitalId())
                .hospitalName(hospital.getHospitalName())
                .hospitalAddress(hospital.getHospitalAddress())
                .hospitalTell(hospital.getHospitalTell())
                .department(hospital.getDepartment())
                .bulid();
    }

    public static Hospital toEntity(HospitalDto hospitalDto) {
        return Hosptial.bulider()
                .hospitalName(hospitalDto.getHospitalName())
                .hospitalAddress(hospitalDto.getHospitalAddress())
                .hospitalTell(hospitalDto.getHospitalTell())
                .department(hospitalDto.getDepartment())
                .build();
    }

    @Builder
    public Hospital(Long hospitalId, String hospitalName, String hospitalAddress, String hospitalTell, String department) {
        this.hospitalName = hospitalName;
        this.hospitalAddress = hospitalAddress;
        this.hospitalTell = hospitalTell;
        this.department = department;
    }
}

