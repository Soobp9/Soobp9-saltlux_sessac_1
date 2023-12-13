package com.example.sesac.hospital.db.entity;

import jakarta.persistence.Id;

public class HospitalDepartment {
    @Id
    private Long departmentId;
    //hospitalId;
    private String hospital_middle;
    private String hospital_major;


}
