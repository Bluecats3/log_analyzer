# Log Analyzer (Cybersecurity Project)

This project is a Python-based log analysis tool that detects suspicious login activity by analyzing failed authentication attempts.

## What it does
- Reads a log file of login activity
- Identifies failed login attempts
- Counts how many times each IP fails
- Flags suspicious IPs with repeated failures

## Concepts Used
- File reading
- String parsing
- Dictionaries and counting
- Basic cybersecurity threat detection

## How to Run
Make sure Python is installed, then run:

python log_analyzer.py

## Files
- log_analyzer.py → main program
- log.txt → sample log data

## Example Output
⚠️ ALERT: 192.168.1.2 has 3 failed login attempts
⚠️ ALERT: 123.45.67.89 has 4 failed login attempts

## What I Learned
- How to analyze logs like a cybersecurity analyst
- How to detect suspicious patterns in data
- How to use Python for real-world security tasks

## Future Improvements
- Add GUI dashboard
- Detect more attack patterns
- Visualize results with graphs
