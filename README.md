# Agentic AI PowerPoint Generator ⚡️

[![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)]()
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)]()

An AI-powered Streamlit application that generates complete **PowerPoint presentations** automatically using your text prompt.  
The app connects to an external **n8n workflow / AI API** that returns a ready `.pptx` file.

---

## 🚀 Features

- 🧠 **AI-based PPT generation**
- 🖥️ Modern Streamlit user interface  
- 📤 Send prompts to any AI API (n8n / FastAPI / custom backend)
- 📥 One-click download for generated PPT
- ⚡ Fast, lightweight, and fully customizable
- 🗂️ Clean & simple code structure

---

## 🖼️ UI Preview
<img width="1329" height="630" alt="Screenshot 2025-11-23 at 4 49 39 PM" src="https://github.com/user-attachments/assets/df5b2539-1184-41c0-8381-e1d4a0dc4b52" />
<img width="1438" height="781" alt="Screenshot 2025-11-23 at 4 49 51 PM" src="https://github.com/user-attachments/assets/44e74535-3489-4ef1-a0f9-c0f63ad05146" />
<img width="1082" height="526" alt="Screenshot 2025-11-23 at 4 50 04 PM" src="https://github.com/user-attachments/assets/2bf5ff65-afaf-4f6c-ac72-732c1bada1b6" />



### 🔹 Home Screen  
![UI Preview](https://via.placeholder.com/900x450?text=Streamlit+PPT+Generator+Preview)

---

## 📦 Project Structure


---

## 📥 Installation

Make sure you have **Python 3.10+**

### 1️⃣ Install dependencies

### 2️⃣ Run the application


---

## ⚙️ Configuration

Update your **API endpoint** inside `app.py`:

```python
API_URL = "https://your-n8n-or-api-endpoint.com/webhook"
