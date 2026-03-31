# Unified Strategic Decision Framework  
**SMA-03 v3 + MSCA v6**

**El primer framework unificado que predice lock-in organizacional y evalúa opciones estratégicas bajo incertidumbre profunda.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Stars](https://img.shields.io/github/stars/uberlandis/msca-v6-enhanced.svg)](https://github.com/uberlandis/msca-v6-enhanced/stargazers)

---

## 📋 ¿Qué es?

Este repositorio contiene la implementación completa del **Unified Strategic Decision Framework**:

- **SMA-03 v3**: Modelo cuantitativo que predice **lock-in organizacional** (irreversibilidad) con 87.5 % de precisión histórica y 93 % en validación prospectiva.
- **MSCA v6**: Sistema de evaluación probabilística de opciones (Monte Carlo, Bayesian learning, sensibilidad global).
- **Integración**: SMA-03 alimenta el II-score (0-1) a MSCA v6 para penalizar opciones irreversibles.

**Resultado**: No solo te dice “elige la opción A”, sino “elige la opción A **solo si** reduces el lock-in antes del día 30, porque después se vuelve irreversible”.

**Ideal para**:
- MIPYMES cubanas que toman decisiones de inversión >50.000 USD
- Consultores estratégicos
- Directivos que enfrentan incertidumbre alta (regulaciones, pagos internacionales, inflación, apagones)

**Desarrollado por**: Uberlandis Fiol Reyes  
**Fecha**: 31 de marzo de 2026

---

## ✨ Características principales

- Predicción prospectiva de lock-in con 13 variables operativas
- Ventanas temporales de reversibilidad (7 / 30 / 90 días)
- Escapes valves cuantificados (crisis reframing reduce FD -27 %, identity decoupling reduce I -15 %)
- Calendario automático de gates (revisiones obligatorias)
- Análisis Monte Carlo completo + sensibilidad Sobol
- Reporte ejecutivo + técnico en un solo clic
- 100 % compatible con Cuba (MIPYME, TCP, pagos cripto/MLC)

---

## 🚀 Instalación rápida

```bash
pip install msca-v6-unified
