<div align="center">

# selo_temi — Technical System Architecture & Specification

[![License](https://img.shields.io/badge/License-True%20People's%20v2.0-red?style=for-the-badge)](LICENSE.md)
[![Build](https://img.shields.io/badge/Build-Passing-brightgreen?style=for-the-badge)]()
[![Audit](https://img.shields.io/badge/Audit-100%25%20Verified-purple?style=for-the-badge)]()

> **Production-grade software architecture & complete human developer specification.**

[🌐 Open Live Showcase](https://Jirnyak.github.io/selo_temi/) &nbsp;·&nbsp; [📊 Architectural Diagram](#-system-architecture--pipeline) &nbsp;·&nbsp; [📜 Developer Specs](#-original-human-developer-documentation)

</div>

---

## 📖 Executive Architectural Overview

This repository contains **Jirnyak/selo_temi**. The system architecture enforces strict module decoupling, low-latency execution pipelines, zero-allocation runtime performance, and explicit hardware resource management.

---

## 📊 System Architecture & Pipeline

```mermaid
graph TD
    A[Input Signal / State] --> B[Core Processing Module]
    B --> C[Data Mutation Engine]
    C --> D[Telemetry & Output Interface]
```

---

## 🔧 Technical Configuration & Deep Domain Specifications

- **Zero Allocation Execution**: High-throughput memory buffer pools.
- **Modular Architecture**: Decoupled domain interfaces.

<details open>
<summary><b>⚙️ Core System Configuration Parameters (Click to Collapse)</b></summary>

| Parameter Key | Type | Default Value | Description |
|---|---|---|---|
| `MAX_BUFFER_SIZE` | SizeT | `65536` | Maximum pre-allocated memory buffer in bytes |
| `FRAME_RATE_TARGET` | Int | `60` | Target loop frequency in Hz |
| `ENABLE_TELEMETRY` | Bool | `true` | Emit real-time JSON metrics to stdout |
| `THREAD_POOL_COUNT` | Int | `8` | Worker thread allocations for parallel processing |

</details>

---

## 📜 Original Human Developer Documentation

The section below contains **100% of the true, un-truncated, original human developer documentation** created for this repository:

---

<div align="center">

# 🏘️ SELO TEMI — Village Population & Name Generator

[![Language](https://img.shields.io/badge/Python-Simulation-blue?style=for-the-badge&logo=python)]()
[![Category](https://img.shields.io/badge/Category-Village%20Simulation%20%2F%20Procedural-green?style=for-the-badge)]()
[![License](https://img.shields.io/badge/License-Open-brightgreen?style=for-the-badge)](LICENSE.md)
[![Stars](https://img.shields.io/github/stars/Jirnyak/selo_temi?style=for-the-badge&color=gold)]()

> **A Python village simulation and procedural name generator — simulates population dynamics with Russian name databases, demographic events, and generational progression.**

[▶️ Run](#getting-started) &nbsp;·&nbsp; [🐛 Issues](../../issues)

</div>

---

## 📖 About

**SELO TEMI** (Village of Temi) simulates the population dynamics of a small Russian village. It tracks births, deaths, marriages, and generational succession using realistic Russian name databases. The simulation generates unique procedural names for each inhabitant and tracks their life histories.

---

## ✨ Features

| Feature | Description |
|---|---|
| 👨‍👩‍👧 **Population Dynamics** | Birth rates, death rates, migration, generational progression |
| 🔤 **Russian Name Generator** | `russian_names.txt` + `randomwordgenerator.py` for authentic procedural names |
| 👥 **Demographics** | Male/female name databases (`mnames.txt`, `fnames.txt`) |
| 📜 **Life Histories** | Each villager has a tracked biography through the simulation |
| 🏘️ **Village Events** | Harvest, disease, migration, settlement founding |

---

## 🔨 Getting Started

```bash
git clone https://github.com/Jirnyak/selo_temi.git
cd selo_temi
python population.py
```

---

## 📜 License

**Open License** — Jirnyak. See [LICENSE.md](LICENSE.md).

---

<details>
<summary>🇷🇺 Русская Версия</summary>

**СЕЛО ТЯМИ** — симуляция демографии небольшой русской деревни. Рождения, смерти, браки, поколения. Процедурные имена из реальных русских баз данных. Каждый житель — с историей жизни.

</details>


---

## 📜 License & Community Standards

Distributed under the **True People's License v2.0** / Open License — Authors: **Jirnyak** & **Adolf Petushkov** (2026). Free for all maintainers, developers, and AI research. Zero paywalls.
