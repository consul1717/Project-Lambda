# Project-Lambda
## Ransomware Recovery Simulator
Project Lambda is an entry-level cybersecurity project that demonstrates how to detect changes to files and restore them from backups after a simulated incident.
###
The goal of this project was to learn how file integrity monitoring works, to learn how SHA-256 hashing works, basic disaster recovery and further Python practice.

## Features
### 1. File Backup
Three company files containing dummy data with backup copies.
### 2. Incident Simulation
Simulates file damage using overwritten string.
### 3. File Integrity Monitoring
Uses SHA-256 hashing to detect modified or missing files.
### 4. File Recovery
Restores files using their original backups.
### 5. Error Handling and Safety Checks
Prevents the simulator from overwriting unexpected file contents.
## Requirements
- Python 3
- Windows, macOS or Linux

## Installation and Usage
1. Download or clone the repository and open the project folder in a terminal.
2. Set up the environment.

`python lambda.py setup`

1. Simulate an incident.

`python lambda.py simulate`

2. Detect the changes.

`python lambda.py detect`

Example output:

`LAMBDA ALERT: employees.txt changed or missing`

`LAMBDA ALERT: budget.txt changed or missing`

`LAMBDA ALERT: project.txt changed or missing`

3. Recover the files.

`python lambda.py recover`

Example output:

`RESTORED: employees.txt`

`RESTORED: budget.txt`

`RESTORED: project.txt`

`OK: employees.txt`

`OK: budget.txt`

`OK: project.txt`

The program restores the original files and verifies their SHA-256 hashes with their respective backups.

## My Findings
Through the Lambda Project, I have developed more of an understanding on:
- Python functions and file handling
- SHA-256 hashing
- File integrity monitoring
- Backup and recovery processes
- Basic incident detection
- Why redcovery verification is important

## Disclaimer
Project Lambda is a basic entry-level educational simulator rather than a complete cybersecurity solution. This project does not use real ransomware or file encryption. It monitors three predetermined text files, and detection is performed manually. Backups are stored locally rather than on a separate medium. 

## Backlog
- Add automatic file monitoring
- Record security events in a log file
- Measure how long recovery takes
- Create a dashboard to display incidents
- Experiment with separate backup storage