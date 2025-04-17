# MGEU ChatBot

Welcome to the **MGEU ChatBot**, an AI-powered assistant developed using **Python**, **Flask**, **HTML**, and **NLTK**. This chatbot is designed to answer frequently asked questions related to **Majestic Global Empire University (MGEU)**.

---

## Features

- **User-friendly** and clean chat interface
- **Pattern-based** chatbot using NLTK and regular expressions
- **Flask-based** backend for handling requests
- **Bootstrap 4** for responsive UI design
- Predefined answers for MGEU-related queries
- **Easy to run** and extend for beginners

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS (**Bootstrap**)
- **NLP Engine:** **NLTK** (`Chat` and `reflections`)
- **Regex Matching:** Stored in **pairs.py**

---

## Project Structure

```
MGEU-ChatBot/
│
├── main.py                # Main Flask application
├── pairs.py               # Regex-based question/answer pairs
│
├── templates/
│   └── index.html         # Frontend chat interface
│
└── static/
    └── images/
        └── LOGO.png       # Optional background image
```

---

## How It Works

1. The user types a message in the input box.
2. The message is sent to the server (`/get_response`) via **POST**.
3. The server uses **nltk.chat.util.Chat** with patterns from **pairs.py** to generate a response.
4. The response is returned and displayed in the chat interface.

---

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Hammadarshad026/Chat_Bot.git
cd Chat_Bot
```

### 2. Install dependencies 
Make sure you have **Python** installed.

```bash
pip install flask nltk
```

### 3. (Optional) Download NLTK data

```python
import nltk
nltk.download('punkt')
```

### 4. Run the app

```bash
python main.py
```

### 5. Open the chatbot  
Go to your browser and open:

```
http://127.0.0.1:5000/
```

---

## Example Questions
You can ask:

- **Hello** / **Hi** / **Hey**
- What is **MGEU**?
- Who created you?
- Tell me about your **programs**
- Where is your **headquarters**?
- How can I contact **MGEU**?

---

## Developer

- **Name:** Hammad Arshad
- **Program:** BS Artificial Intelligence
- **University:** Superior University, Lahore
- **Contact:** +923059262670
- **Mail:** HammadArshad026@gmail.com
  

---

**License**  
This project is for **educational** and **demonstration** purposes. You are free to use, modify, and share it with **credit to the author**.

---

**Acknowledgments**

- **NLTK** – Natural Language Toolkit
- **Flask** – Web framework for Python
- **Bootstrap** – Responsive front-end toolkit

---

**Contributions**  
Contributions are welcome. Feel free to **fork the repository**, create a **new branch**, and **submit a pull request**.

---

**Live Demo (Optional)**  
If deployed, you can access the live chatbot here:  
**Coming soon**
