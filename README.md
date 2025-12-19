# 👻 Ghostclock

**Timing Side-Channel Analysis on Large Language Models (LLMs)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Local-red)](https://ollama.com/)
[![Kali Linux](https://img.shields.io/badge/OS-Kali%20Linux-black)](https://www.kali.org/)

## 📌 Overview

Ghostclock is a Python-based security research project that explores **timing side-channel vulnerabilities** in Large Language Models (LLMs).

The project demonstrates that LLMs do not execute all prompts uniformly — instead, different prompt intents trigger different internal execution paths, which can be inferred through **response timing alone**.

> **This project is conducted entirely on local models and is intended strictly for educational and defensive security research.**

## 🎯 Project Goals

- Understand how side-channel attacks apply to AI systems
- Measure and analyze timing leakage in LLM inference
- Demonstrate that safety and refusal logic introduces detectable latency
- Build a multi-layer experimental framework for timing analysis
- Promote awareness of AI security risks beyond prompt content

## 🧠 Core Concept: Timing as a Side-Channel

Even when an LLM's output is restricted or sanitized, **execution time** can still reveal information about:

- 🛡️ Safety filter activation
- ⚖️ Policy enforcement checks
- 🚫 Refusal logic execution
- 🧩 Internal reasoning complexity

**Ghostclock treats time as an observable signal** and shows how it can be used to infer hidden internal behavior.

## 🧪 Experimental Environment

| Component | Specification |
|-----------|---------------|
| **OS** | Kali Linux (VM) |
| **Language** | Python 3 |
| **Model Runtime** | Ollama |
| **Model** | mistral |
| **Measurement** | `time.perf_counter_ns()` |
| **Execution** | Local CLI inference |

> **No APIs, cloud services, or external models are used.**

## 🧱 Project Architecture

Ghostclock is structured into **four progressive layers**, each building upon the previous one.

### 🔹 Layer 1 — Baseline Timing Harness

**Purpose:** Establish a baseline for LLM inference timing and observe natural system jitter.

**What happens:**
- Model warmup
- Identical prompts executed repeatedly
- Raw timing statistics collected

**Key insight:** LLM inference time is measurable and non-constant, even for identical prompts.

### 🔹 Layer 2 — Differential Timing Analysis

**Purpose:** Compare benign prompts with sensitive prompts to detect execution path divergence.

**What happens:**
- Two prompt categories executed repeatedly
- Mean and variance calculated
- Timing deltas (`Δt`) analyzed

**Key insight:** Safety-related prompts consistently take significantly longer, revealing a slow execution path.

### 🔹 Layer 3 — Timing-Based Prompt Classification

**Purpose:** Create statistical timing profiles for different prompt intent classes.

**Prompt classes:**
- **Trivial** – Simple, low-effort prompts
- **Informational** – Neutral but computation-heavy prompts
- **Sensitive** – Safety or policy-related prompts
- **Refusal** – Prompts intended to trigger denial

**What happens:**
- Multiple samples per class collected
- Mean, median, and variance computed
- Distinct timing signatures emerge per class

**Key insight:** Prompt intent can be inferred solely from timing behavior, **without inspecting output**.

### 🔹 Layer 4 — Rule-Based Timing Classifier

**Purpose:** Demonstrate a practical side-channel exploit model.

**What happens:**
- Timing thresholds derived from Layer 3
- Unknown prompts timed
- Prompts classified based on observed latency

**Key insight:** A basic but effective timing-based classifier can predict prompt intent.

## 📊 Key Findings

- ✅ LLMs do **not** execute in constant time
- ✅ Safety and refusal logic introduces **measurable latency**
- ✅ Timing signals remain detectable **despite system noise**
- ✅ Side-channel risks apply to AI systems **just like cryptographic ones**

## 🛡️ Security Implications

Ghostclock highlights the need for:

- **Constant-time execution** for sensitive paths
- **Artificial timing normalization**
- **Noise injection or batching defenses**
- **Side-channel awareness** in AI deployments

## ⚠️ Ethical Notice

This project:

> ✅ Uses **only local models**  
> ✅ Does **not bypass safeguards**  
> ✅ Does **not extract private data**  
> ✅ Is intended to **strengthen AI security awareness**  
> ✅ All experiments are **observational and non-exploitative**


## 🚀 Quick Start

Follow these steps to get Ghostclock up and running:
1. **Clone the repository**
git clone https://github.com/Wingedarrows03/Ghostclock.git

  cd Ghostclock


3. **Activate virtual environment**

   
  source venv/bin/activate


5. **Run the classifier layers progressively**

python layer1_classifier.py

python layer2_classifier.py

python layer3_classifier.py

python layer4_classifier.py


> **Note:** Ensure Ollama is running with the mistral model before executing the classifier scripts.
