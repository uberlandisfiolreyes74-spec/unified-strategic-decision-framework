# Unified Strategic Decision Framework

## Integrating SMA-03 v3 (Organizational Lock-In Prediction) with MSCA v6 (Probabilistic Option Evaluation)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.5281/zenodo.XXXXXXX)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-Open_Access-blue)](paper/SMA03_MSCA_Unified_Framework_Academic_Paper.pdf)

This repository contains the full framework, validation data, and operational tools for the **Unified Strategic Decision Framework**, a quantitative model that predicts organizational lock-in and evaluates strategic options under uncertainty.

**Status:** Ready for Peer Review | **Target Journals:** Academy of Management Review, Organization Science, Administrative Science Quarterly

## 📖 Overview

Strategic decisions often become irreversible not because of objective constraints, but due to a cascade of psychological, social, and structural pressures. This framework provides the first unified, quantitative approach to:

- **Predict** lock-in *before* commitment deepens (87.5% accuracy on 120 historical cases)
- **Quantify** the cost of reversal, adjusted for lock-in risk
- **Identify** precise temporal windows for reversible action (e.g., 90-day critical period)
- **Recommend** actionable interventions (crisis reframing, identity decoupling) with measured impact

The system integrates two core models:
1. **SMA-03 v3** (Strategic Model for Analyzing Organizational Irreversibility): A 13-variable model that outputs an Irreversibility Index (II-score), risk classification, and reversal windows.
2. **MSCA v6** (Monte Carlo Scenario Analysis): A probabilistic option evaluator that incorporates the II-score to penalize irreversible strategies and rank options.

## ✨ Key Contributions

- **Quantitative Lock-In Prediction**: Moves beyond descriptive theory to a testable, 0-1 scale model.
- **Environmental Crisis Perception (FD) as Dominant Driver**: Explains 79% of irreversibility variance, showing lock-in is largely a function of perception.
- **Temporal Reversibility Windows**: Defines actionable windows (7, 30, or 90 days) to reverse course before psychological lock-in sets in.
- **Actionable Interventions**: Quantifies the impact of interventions like Crisis Reframing (-27% FD) and Identity Decoupling (-15% I).
- **Cross-Sector Validation**: Validated on 120 cases across 8 sectors (Tech, Healthcare, Government, etc.) without sector-specific tuning.

## 🏗️ Framework Architecture

The decision process follows a two-layer, integrated workflow:

1. **Input**: Decision context, 13 SMA-03 variables (scored 0-1), and 3-scenario payoffs for each strategic option.
2. **Layer 1 - SMA-03**: Calculates II(0), risk level (Green, Yellow, Orange, Red, Critical), and the point of no return.
3. **Layer 2 - MSCA v6**: Evaluates options using Monte Carlo simulations, adjusted by the lock-in multiplier (`1 + II²`).
4. **Integration**: Ranks options using a dynamic composite score (weights adjusted by II level) and generates a gate schedule.
5. **Output**: Unified recommendation, confidence score, and mandatory decision gate timeline.

![Framework Workflow](docs/workflow.png) *Add a visual workflow diagram here*

## 📊 The SMA-03 v3 Model

The Irreversibility Index (II) is calculated using 13 operationalized variables:

| Category | Variable | Description |
|----------|----------|-------------|
| **Structural Pressures** | `P_E` | Economic: Sunk costs, capital at risk |
| | `P_R` | Reputational: Public commitment, media exposure |
| | `P_L` | Relational: Stakeholder lock-in, alliance strength |
| | `P_S` | Strategic: Competitive positioning, opportunity cost |
| | `P_M` | Emotional: Team momentum, leadership investment |
| **Belief System** | `C` | Causal: Confidence in the decision logic |
| | `I` | Identity: Organizational identity fusion |
| | `S` | Significance: Perceived importance of decision |
| | `A_V` | Validation: External expert/supporter validation |
| **Predispositions** | `B_R` | Risk tolerance |
| | `B_E` | Emotional sensitivity |
| | `B_C` | Cognitive flexibility |
| **Trigger** | `FD` | Environmental Crisis Perception |

**Core Formula:**
