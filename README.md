# ChatPTP: Internal AI Assistant

**Version:** 1.0 (Prototype)  
**Author:** Internal Development Team  
**Status:** Alpha / Internal Testing  

## 📖 Overview

ChatPTP is a secure, private, and offline AI chatbot developed for **Port of Tanjung Pelepas (PTP)**. It is designed to assist employees with internal queries using company data without exposing sensitive information to the public internet.

**Key Features:**
* **100% Offline:** Runs entirely on local hardware (`localhost`) to ensure data sovereignty.
* **Dual-Brain Architecture:**
    * **Speed Mode:** Uses `Llama 3.2` for instant text responses.
    * **Vision Mode:** Uses `Llava` for analyzing uploaded images and documents.
* **RAG (Retrieval-Augmented Generation):** "Knows" internal PTP facts via the `company_info.txt` file.

---

## 🛠️ Prerequisites

Before starting, ensure the host machine has the following installed:

1.  **Python 3.10+**: [Download Here](https://www.python.org/downloads/)  
    * *Important:* Check the box **"Add Python to PATH"** during the installation setup.
2.  **Ollama (The AI Engine)**: [Download Here](https://ollama.com/download)
3.  **Hardware**: Minimum 8GB RAM (16GB Recommended) with ~10GB of free disk space.

---

## ⚙️ Installation Guide

### 1. Setup the AI Engine
Open your terminal (PowerShell or Command Prompt) and install the required AI models. This process downloads the "brains" (~6GB total) and may take a few minutes depending on internet speed.

```powershell
# Install the text model (Speed)
ollama run llama3.2

# Install the vision model (Images)
ollama run llava