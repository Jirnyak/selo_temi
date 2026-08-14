# 🌾 Selo Temi — Procedural Rural Topography & Slavic Folklore Narrative Engine

[![Live Demo](https://img.shields.io/badge/Live_Showcase-GitHub_Pages-22c55e?style=for-the-badge&logo=github)](https://jirnyak.github.io/selo_temi/)
[![AI Index](https://img.shields.io/badge/LLM_Search-llms.txt-38bdf8?style=for-the-badge)](https://raw.githubusercontent.com/Jirnyak/selo_temi/main/llms.txt)
[![C++20](https://img.shields.io/badge/C%2B%2B-20-00599C?style=for-the-badge&logo=cplusplus)](https://isocpp.org/)
[![Procedural](https://img.shields.io/badge/WorldGen-Perlin_Hydrology-00f5a0?style=for-the-badge)](https://en.wikipedia.org/wiki/Perlin_noise)

A procedural world generator and atmospheric narrative engine creating hyper-detailed Slavic rural settlements, hydraulic river erosion networks, and generative folklore dialogue graphs.

---

## 🏛️ Generation Pipeline

```mermaid
graph TD
    Seed[Procedural Random Seed] --> Perlin[Multi-Octave Simplex / Perlin Noise]
    Perlin --> Hydro[Hydraulic Fluvial Erosion Simulation]
    Hydro --> Settle[Optimal Village Settlement Placement]
    Settle --> Road[A* Cost-Weighted Road Network Synthesis]
    Road --> Narrative[Markov Folklore Event Generator]
```

---

### 👨‍💻 Engineering Syndicate & Authors
- **Жирняк (Jirnyak)** — Lead Procedural Architect & World Generator.  
  GitHub: [@Jirnyak](https://github.com/Jirnyak)
- **Адольф Петушков (Adolf Petushkov)** — High-Concurrency Systems & Simulation Architecture.  
  GitHub: [@marko1olo](https://github.com/marko1olo)
