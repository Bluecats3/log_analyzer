# Log Analyzer | Cybersecurity Threat Detection Tool

A Python-based log analysis tool designed to identify suspicious authentication activity by detecting repeated failed login attempts across IP addresses.

---

## Project Overview

This project simulates a core function of a Security Operations Center (SOC): analyzing system logs to detect potential intrusion attempts.  

The program processes authentication logs, extracts relevant data, and flags abnormal behavior patterns that may indicate brute-force or unauthorized access attempts.

---

## Key Features

- Parses log files to extract IP addresses and login results  
- Tracks and aggregates failed login attempts per IP  
- Detects and flags suspicious activity based on threshold conditions  
- Identifies high-risk sources of repeated authentication failures  
- Outputs a clear and actionable security report  

---

## Technical Concepts

- File I/O (reading structured log data)  
- String parsing and data extraction  
- Hash maps / dictionaries for frequency analysis  
- Pattern recognition and anomaly detection  
- Basic cybersecurity threat modeling  

---

## Usage

Run the analyzer with:

```bash
python log_analyzer.py
