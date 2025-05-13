# 🔐 Mini SIEM – SSH Log Monitor with Slack Alerts
This is a small Python project that watches SSH logs for failed login attempts. If an IP address has too many failed logins (like a brute-force attack), it sends an alert to Slack.

Great for learning cybersecurity, log analysis, and basic alerting!

# ✅ What It Does
- Reads SSH log files (like /var/log/auth.log or test_logs/auth.log)

- Looks for failed login attempts

- Counts how many times each IP fails to log in

- Sends a Slack alert if any IP reaches the limit (default is 5 tries)

# 📁 Files
log_monitor.py – Main script that does the log reading and detection

alert_engine.py – Sends messages to Slack

test_logs/auth.log – A sample log file you can test with

requirements.txt – Python libraries you need

README.md – This file

# 💻 Demos
![Slack Bot Alert](https://github.com/IsaacMorrow0/Mini-siem/blob/main/images/siem-slackex.png?raw=true)

![Command Line](https://github.com/IsaacMorrow0/Mini-siem/blob/main/images/Example.png?raw=true) 

# 📘 What I Learned
- While building this Mini SIEM project, I learned:

- How to parse system logs using Python and regular expressions

- How to detect brute-force login patterns by tracking failed SSH attempts

- How to send real-time alerts to Slack using incoming webhooks

- How SIEM systems use thresholds and detection logic to identify threats

- How to organize a Python project and write readable, modular code

- How to test and simulate real-world scenarios using sample log data

- How to push and document a project on GitHub for others to review

- This project helped me understand core security concepts like detection engineering, log analysis, and automated alerting — all essential skills for blue team cybersecurity work.

# 🔧 To Add Next (Ideas)
Only alert if failures happen within 60 seconds

Add IP location lookup (GeoIP)

Watch live system logs with watchdog
