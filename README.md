# Marco Unificado de Decisión Estratégica

## Integración de SMA-03 v3 (Predicción de bloqueo organizacional) con MSCA v6 (Evaluación probabilística de opciones)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-PDF-blue)](paper/SMA03_MSCA_Unified_Framework_Academic_Paper.pdf)

Este repositorio contiene el marco completo, los datos de validación y las herramientas operativas del **Marco Unificado de Decisión Estratégica**, un modelo cuantitativo que predice el bloqueo organizacional y evalúa las opciones estratégicas en condiciones de incertidumbre.

**Estado:** Listo para revisión por pares | **Revistas objetivo:** Academy of Management Review, Organization Science, Administrative Science Quarterly

---

## 📖 Resumen

Las decisiones estratégicas a menudo se vuelven irreversibles no por limitaciones objetivas, sino por una cascada de presiones psicológicas, sociales y estructurales. Este marco proporciona el primer enfoque unificado y cuantitativo para:

- **Predecir el bloqueo** antes de que el compromiso se profundice (87,5 % de precisión en 120 casos históricos).
- **Cuantificar el coste de la reversión**, ajustado al riesgo de bloqueo.
- **Identificar ventanas temporales precisas** para la acción reversible (ej. período crítico de 90 días).
- **Recomendar intervenciones prácticas** (replanteamiento de crisis, desvinculación de identidad) con impacto medido.

El sistema integra dos modelos centrales:

1. **SMA-03 v3**: Modelo de 13 variables que genera un Índice de Irreversibilidad (II), clasificación de riesgo y ventanas de reversión.
2. **MSCA v6**: Evaluador probabilístico de opciones que incorpora el II para penalizar estrategias irreversibles y ordenar opciones.

---

## ✨ Contribuciones clave

- **Predicción cuantitativa del bloqueo**: Pasa de la teoría descriptiva a un modelo comprobable en escala 0-1.
- **Percepción de crisis ambiental (FD) como factor dominante**: Explica el 79% de la varianza de irreversibilidad.
- **Ventanas de reversibilidad temporal**: Define plazos (7, 30, 90 días) para revertir antes del bloqueo psicológico.
- **Intervenciones accionables**: Cuantifica el impacto de Replanteamiento de Crisis (-27% FD) y Desvinculación de Identidad (-15% I).
- **Validación intersectorial**: 120 casos en 8 sectores sin ajustes específicos.

---

## 🏗️ Arquitectura del marco

1. **Entrada**: Contexto, 13 variables SMA-03 (0-1) y pagos por escenario para cada opción.
2. **Capa 1 - SMA-03**: Calcula II(0), nivel de riesgo y punto de no retorno.
3. **Capa 2 - MSCA v6**: Evalúa opciones con simulaciones Monte Carlo ajustadas por multiplicador de bloqueo (\(1 + II^2\)).
4. **Integración**: Ordena opciones con puntuación dinámica y genera calendario de gates.
5. **Salida**: Recomendación unificada, confianza y calendario de decisiones.

---

## 📊 Modelo SMA-03 v3

| Categoría | Variable | Descripción |
|-----------|----------|-------------|
| Presiones estructurales | P_E | Costos hundidos, capital en riesgo |
| | P_R | Compromiso público, exposición mediática |
| | P_L | Dependencia de grupos de interés, alianzas |
| | P_S | Posicionamiento competitivo, costo de oportunidad |
| | P_M | Impulso del equipo, inversión de liderazgo |
| Sistema de creencias | C | Confianza en la lógica de la decisión |
| | I | Fusión con identidad organizacional |
| | S | Importancia percibida de la decisión |
| | A_V | Validación externa (expertos, partes interesadas) |
| Predisposiciones | B_R | Tolerancia al riesgo |
| | B_E | Sensibilidad emocional |
| | B_C | Flexibilidad cognitiva |
| Desencadenante | FD | Percepción de crisis ambiental |

**Fórmula central:**
