ChatPTP: Internal AI Assistant
Version: 1.0 (Prototype)

Author: Muhammad Aiman Haiqal

Status: Internal Development

📖 Overview
ChatPTP is a secure, private, and offline AI chatbot developed for Port of Tanjung Pelepas (PTP). It is designed to assist employees with internal queries using company data without exposing information to the public internet.

Key Features:

100% Offline: Runs entirely on local hardware (localhost) to ensure data sovereignty.

Dual-Brain Architecture:

Speed Mode: Uses Llama 3.2 for instant text responses.

Vision Mode: Uses Llava for analyzing uploaded images and documents.

RAG (Retrieval-Augmented Generation): "Knows" internal PTP facts via the company_info.txt file.

🛠️ Prerequisites
Before starting, ensure the host machine has the following installed:

Python 3.10+: Download Here

Important: Check the box "Add Python to PATH" during installation.

Ollama (The AI Engine): Download Here

RAM Requirement: Minimum 8GB (16GB Recommended).

⚙️ Installation Guide
1. Setup the AI Engine
Open your terminal (PowerShell or Command Prompt) and install the required AI models. This may take a few minutes as it downloads the "brains" (~6GB total).

PowerShell

# Install the text model (Speed)
ollama run llama3.2

# Install the vision model (Images)
ollama run llava
2. Setup the Application
Navigate to the project folder and install the necessary Python libraries.

PowerShell

cd C:\application\chatptp-initiative
pip install streamlit ollama pillow
3. Folder Structure Check
Ensure your project folder looks exactly like this for the images to load correctly:

Plaintext

chatptp-initiative/
├── app.py                  # The main application code
├── company_info.txt        # The internal knowledge base
├── README.md               # This manual
└── public/                 # Folder for images
    ├── ptp-logo.png        # Dark text logo (for Light Mode)
    ├── ptp-logo-light.png  # White text logo (for Dark Mode)
    └── python-logo.png     # User avatar icon
🚀 How to Run
Ensure the Ollama app is running in the background (check your taskbar).

Open PowerShell and navigate to the project folder.

Run the following command:

PowerShell

streamlit run app.py
A browser window will automatically open at http://localhost:8501.

🕹️ User Guide
Changing Modes
Standard (Llama 3.2): Best for general questions, drafting emails, or summarizing text. It is fast and lightweight.

Vision (Llava): Select this from the Sidebar. A "Browse Files" button will appear. You can upload an image (like a chart or site photo) and ask the AI to describe it or extract data from it.

Updating Knowledge
To teach the bot new internal facts (e.g., new project codes or safety guidelines):

Open company_info.txt.

Paste the new information in plain text.

Save the file.

Refresh the web page. The bot will immediately know the new info.

⚠️ Troubleshooting
Issue: "Ollama is not running"

Fix: Open the start menu, type "Ollama", and click the icon to start the background service.

Issue: Images or Logos are missing (broken image icon)

Fix: Ensure your image files are inside the public folder and named exactly as listed in the "Folder Structure" section above.

Issue: "Command not found" when installing

Fix: Ensure you restarted your terminal after installing Python/Ollama. If it fails, try python -m pip install ... instead of just pip install ....