# 🌿 ESG Dashboard with IoT Integration

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Grafana](https://img.shields.io/badge/grafana-visualization-orange.svg)](https://grafana.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A production-ready environmental monitoring system integrating IoT sensor simulation, MQTT ingestion, TimescaleDB, and Grafana visualization — designed for ESG (Environmental, Social, and Governance) data compliance.

---

## 📦 Features

- Secure, modular project structure
- Simulated CO₂ sensor input
- Time-series optimized TimescaleDB
- MQTT ingestion with reconnect logic
- Grafana dashboards provisioned automatically
- Threshold-based alert system
- Dockerized and easy to deploy

---

## 🚀 Quick Start

### 1. Start the System
```bash
docker-compose up -d
```

### 2. Run Simulators
```bash
python -m simulation.devices.co2_sensor
```

---

## 📊 Access Grafana

- URL: [http://localhost:3000](http://localhost:3000)
- Login:
  - Username: `admin`
  - Password: *(value from `secrets/grafana_admin_password.txt`)*

---

## 📁 Project Structure

```
esg-dashboard/
├── backend/               # DB, ingestion, alerts
│   ├── alerts/
│   ├── ingest/
│   ├── sql/
│   └── db.py
├── simulation/            # IoT sensor simulation
│   └── devices/
├── docker/                # Grafana provisioning
│   └── grafana/
├── frontend/              # (placeholder for UI)
├── tests/                 # Unit tests
├── secrets/               # External secrets
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚠️ Alerting

Basic CO2 threshold alerting is available:
```bash
python3 -m backend.alerts.co2_alert
```

---

## 📘 Learning Resources

- [MQTT Essentials](https://www.hivemq.com/mqtt-essentials/)
- [TimescaleDB Docs](https://docs.timescale.com/)
- [Grafana Alerting](https://grafana.com/docs/grafana/latest/alerting/)

---

## 📄 License

MIT License © 2025 [Your Name / Org]
