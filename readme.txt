# IRANDP – Intelligent Rule-Based Autonomous Network Defense Platform

IRANDP is a real-time cyber defense system designed to **detect, analyze, visualize, and automatically respond to network attacks** using rule-based intelligence and live monitoring.

This project simulates a **Security Operations Center (SOC)** environment with live traffic analysis, global attack visualization, automated containment, and forensic logging.

---

##  Key Features

-  **Real-Time Network Traffic Monitoring**
-  **Rule-Based Attack Detection**
-  **Live Global Attack Map (Google Maps Integration)**
-  **Automated Threat Containment**
-  **Organizational Risk Trend Analysis**
-  **SOC Timeline Reconstruction**
-  **Real-Time Alerts (GUI + Optional Email)**
-  **Professional Animated Front Page**
-  **Cloud-Deployable Architecture (AWS / Oracle)**

---

##  System Architecture Overview

IRANDP follows a **hybrid desktop + web architecture**:

- **Desktop SOC Dashboard** (Tkinter)
- **Web-Based Front Launcher** (Flask)
- **Live Google Map Engine**
- **Rule-Based Analysis Engine**
- **Cloud-Ready Deployment**

---

##  Core Components

###  Front Launcher (Web)
- Animated landing page
- Professional cyber-themed UI
- Launches Command Center
- Built using **HTML, CSS, JavaScript**
- Served via **Flask**

###  SOC Dashboard (Desktop App)
- Built with **Python Tkinter**
- Displays:
  - Network Telemetry
  - Threat Intelligence
  - Autonomous Actions
  - Forensic Evidence
- Mission Control Bar shows:
  - Threat Level
  - Defense Mode
  - Active Threat Count

###  Network Sensor Engine
- Uses **Scapy**
- Captures live packets
- Tracks traffic spikes
- Detects abnormal behavior

###  Threat Detection & Containment
- Rule-based attack classification
- Automatic IP blocking
- Risk score escalation
- SOC event logging

###  Global Geo-Map Engine
- Real Google Map visualization
- Live red attack markers
- IP → Country mapping
- Dynamic updates via browser

###  SOC Timeline Engine
- Reconstructs attack sequence
- Logs:
  - Traffic spikes
  - Attack detection
  - Containment actions
- Thread-safe logging

---

##  Technologies Used

| Category | Technology |
|------|-----------|
| Language | Python 3 |
| GUI | Tkinter |
| Web | Flask, HTML, CSS, JavaScript |
| Network | Scapy |
| Visualization | Google Maps |
| Cloud | AWS / Oracle |
| OS | Windows / Linux |

---

## ☁ Deployment Options

-  **AWS EC2**
-  **Oracle Free Tier**
-  Local Machine (Demo / Testing)

---

##  How to Run

### 🔹 Desktop SOC Dashboard
```bash
python dashboard.py
