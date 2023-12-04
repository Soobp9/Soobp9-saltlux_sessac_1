package com.example.sesac.hospital.db.repository;

import com.example.sesac.hospital.db.entity.Hospital;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface HospitalRepository extends JpaRepository<Hospital, Long> {
    List<Hospital> findAllByDepartment(String department);
}