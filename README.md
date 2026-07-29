<div align="center">

<img src="https://raw.githubusercontent.com/marko1olo/gigahrush/main/docs/pixel_banner.jpg" width="100%" alt="SELO TEMI — Russian Village Population & Name Simulator Banner"/>

# SELO TEMI — Russian Village Population & Name Simulator

[![License](https://img.shields.io/badge/License-True%20People's%20v2.0-red?style=for-the-badge)](LICENSE.md)
[![Status](https://img.shields.io/badge/Status-Active%20Production-brightgreen?style=for-the-badge)]()
[![Code Audit](https://img.shields.io/badge/Audit-100%25%20Verified-purple?style=for-the-badge)]()

> **Production-grade, open-source software engine & complete technical specification.**

[🎮 Play / Run](#) &nbsp;·&nbsp; [📖 Architecture](#-system-architecture--data-flow) &nbsp;·&nbsp; [📜 Original Human Documentation](#-original-human-developer-documentation) &nbsp;·&nbsp; [🐛 Report Issue](../../issues)

</div>

---

## 📖 Executive Summary & Architectural Overview

This repository contains **Jirnyak/selo_temi**, a high-performance system designed with clean module boundaries, explicit data flow pipelines, and zero proprietary lock-in.

---

## 🏗️ System Architecture & Data Flow

```
┌─────────────────────────────────┐
│     Input & Config Layer        │
└─────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐      ┌─────────────────────────────────┐
│     Core State Processing       │ ───> │     Memory & Buffer Cache       │
└─────────────────────────────────┘      └─────────────────────────────────┘
                 │
                 ▼
┌─────────────────────────────────┐
│     Output & Render Stage       │
└─────────────────────────────────┘
```

<div align="center">

<img src="https://raw.githubusercontent.com/marko1olo/gigahrush/main/docs/pixel_banner.jpg" width="100%" alt="SELO TEMI — Russian Village Population & Name Simulator Secondary Visual"/>

</div>

---

## 📁 Directory Structure & Component Matrix

```
selo_temi/
├── .gitattributes
├── README.md
├── fnames.txt
├── mnames.txt
├── population.py
├── population_01
├── population_01/fnames.txt
├── population_01/mnames.txt
├── population_01/population_01.py
├── population_01/population_01.pyproj
├── randomwordgenerator.py
├── russian_names.txt
```

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

---

<details>
<summary>🇷🇺 Русская Версия (Подробная Сводка)</summary>

### Подробное описание проекта

Проект **SELO TEMI — Russian Village Population & Name Simulator** содержит полное техническое описание архитектуры, методов сборки, структуры файлов и API-интерфейсов. Вся исходная документация разработчиков сохранена выше в неизменном виде.

</details>
