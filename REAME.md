# 🩺 Pipeline Doctor – CI/CD Failure Auto-Debugger

> **Static logs are boring. Smart debugging is the future.** 🚀

Pipeline Doctor is an intelligent CI/CD assistant that doesn't just tell you that your build failed—it tells you **why** and **how to fix it**. No more digging through thousands of lines of logs.

## 💡 The Problem
In traditional DevOps: 
❌ **"Build failed. Good luck."**

With Pipeline Doctor:
✅ **"Build failed because dependency not installed. Try: pip install missing-module"**

## ⚙️ How it Works
1.  **Developer Pushes Code**: GitHub Action triggers a build.
2.  **Failure Detection**: If a step fails, the workflow captures the logs.
3.  **The Doctor Arrives**: A Python script analyzes the logs using Regex-based intelligence.
4.  **Smart Suggestion**: The Doctor outputs a human-readable fix directly in the CI console.

## 🔍 Smart Detection Capabilities
The Doctor is trained to recognize:
- 📦 **Missing Modules**: Detects `ModuleNotFoundError` and suggests installation.
- 🔑 **Permissions**: Identifies `Permission denied` issues.
- 📁 **Missing Files**: Catches `FileNotFoundError`.
- ⌨️ **Code Syntax**: Points out `SyntaxError` and `IndentationError`.

## 🛠 Tech Stack
-   **GitHub Actions**: The CI/CD engine.
-   **Python**: The analytical brain.
-   **Regex**: For high-speed log parsing.

## 📂 Project Structure
```text
pipeline-doctor/
│
├── app/                 # Your application
│   └── app.py           # Target script for build
│
├── doctor/              # The AI Assistant
│   └── pipeline_doctor.py # Log analyzer logic
│
└── .github/workflows/   # CI/CD Pipeline
    └── ci.yml           # Automated triggers
```

## 🚀 Getting Started
1. **Push your code**: The pipeline runs automatically on push.
2. **Trigger a failure**: Use the `workflow_dispatch` in GitHub Actions with `cause_failure=True` to see the Doctor in action.

---
*Made with ❤️ for advanced DevOps learners.*
