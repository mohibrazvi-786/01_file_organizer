# 🚀 Smart File Organizer

An AI-powered file organizer that intelligently classifies and organizes files using **Google Gemini AI** with a **hybrid rule-based + AI classification system**.

## ✨ Key Features

- 🤖 AI-powered file classification using Google Gemini
- ⚡ Fast rule-based classification for common file types
- 📄 File preview extraction for intelligent AI decisions
- 🔁 Automatic retry on temporary AI service failures
- 📂 Automatic file organization into categorized folders
- 🧪 Automated code formatting, linting, and testing
- 🏗️ Clean, modular, and maintainable architecture

> **Project Goal:** Demonstrate production-style AI integration, clean software engineering practices, and modern Python development workflows.

---

## 📖 Overview

Managing files manually becomes difficult as downloads, documents, images, videos, and code files accumulate over time. Traditional file organizers rely only on file extensions, making them ineffective for files with ambiguous names or uncommon formats.

**Smart File Organizer** combines deterministic programming with Generative AI to intelligently classify files.

The application first attempts a fast **rule-based classification** using known file extensions. When the file cannot be confidently classified, it automatically extracts a preview of the file and uses **Google Gemini AI** to determine the most appropriate category.

This hybrid approach provides the best of both worlds:

- ⚡ Instant classification for common file types
- 🤖 AI reasoning for ambiguous files
- 💰 Reduced API usage and lower costs
- 🛡️ Reliable fallback when AI is unavailable

The project was built to demonstrate how Large Language Models can be integrated into production-style software while maintaining clean architecture, modular design, automated testing, and modern Python engineering practices.

---

## ✨ Features

### 🤖 AI-Powered Classification

- Integrates Google Gemini AI for intelligent file categorization.
- Understands file names and extracted content previews.
- Returns structured classification with category, confidence score, and reasoning.

### ⚡ Hybrid Classification Engine

- Uses deterministic extension-based classification whenever possible.
- Falls back to AI only when rule-based classification is insufficient.
- Reduces API usage while improving performance and reliability.

### 📄 Smart File Preview

Supports intelligent preview extraction from:

- TXT
- PDF
- DOCX
- Markdown
- Source Code
- CSV
- JSON
- HTML/CSS/JavaScript

### 📂 Automatic Organization

- Creates category folders automatically.
- Moves files into their predicted destination.
- Displays confidence score and reasoning.

### 🛡️ Fault Tolerance

- Automatic retry for temporary Gemini API failures.
- Safe fallback classification when AI is unavailable.
- Prevents crashes during transient API failures.

### 🧪 Developer Experience

- Black
- Ruff
- Pytest
- Development automation scripts

---

## 🏗️ Architecture

The project follows a modular architecture where each component has a single responsibility.

```text
                    User
                      │
                      ▼
             Scan Directory
                      │
                      ▼
            Rule-Based Classifier
              │              │
      Known Extension    Unknown File
              │              │
              ▼              ▼
       Return Result    File Preview
                              │
                              ▼
                      Gemini AI (LLM)
                              │
                              ▼
                Structured Classification
                              │
                              ▼
                       Move File
                              │
                              ▼
                    Organized Folder
```

### Core Components

| Component | Responsibility |
|-----------|----------------|
| `organizer.py` | Scans directories and orchestrates the workflow |
| `rule_classifier.py` | Fast extension-based classification |
| `ai_classifier.py` | Coordinates rule-based and AI classification |
| `llm.py` | Handles Gemini API communication |
| `file_preview.py` | Extracts preview text from supported documents |
| `mover.py` | Moves files into categorized folders |
| `models.py` | Defines structured data models |
| `prompts.py` | Builds prompts for the LLM |

---

## 📂 Project Structure

```text
01_file_organizer/
│
├── src/
│   └── file_organizer/
│       ├── ai_classifier.py
│       ├── rule_classifier.py
│       ├── llm.py
│       ├── file_preview.py
│       ├── organizer.py
│       ├── mover.py
│       ├── prompts.py
│       ├── models.py
│       ├── config.py
│       └── main.py
│
├── tests/
│   ├── test_classifier.py
│   └── test_scan.py
│
├── scripts/
│   └── tasks.py
│
├── sample_files/
├── test_workspace/
├── README.md
├── pyproject.toml
└── .gitignore
```

### Project Organization

- **src/** — Application source code
- **tests/** — Unit tests
- **scripts/** — Development automation
- **sample_files/** — Example input files
- **test_workspace/** — Temporary testing workspace

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/<your-username>/01_file_organizer.git
cd 01_file_organizer
```

### Create a Virtual Environment

```bash
python -m venv .venv
```

**Windows**

```powershell
.venv\Scripts\activate
```

**Linux / macOS**

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the application:

```bash
python -m src.file_organizer.main
```

Development workflow:

```bash
python scripts/tasks.py dev
```

Run quality checks:

```bash
python scripts/tasks.py check
```

Run tests:

```bash
python -m pytest
```
---

## 🧪 Testing

The project includes automated quality checks and unit tests.

Run all quality checks:

```bash
python scripts/tasks.py check
```

Run only the test suite:

```bash
python -m pytest
```

The project uses:

- **Black** for code formatting
- **Ruff** for linting and static analysis
- **Pytest** for unit testing

All tests are expected to pass before committing changes.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| AI Model | Google Gemini |
| AI SDK | google-genai |
| Environment | python-dotenv |
| Document Parsing | pypdf, python-docx |
| Testing | Pytest |
| Formatting | Black |
| Linting | Ruff |
| Version Control | Git & GitHub |