# 🤖 ChatGPT-like Streamlit App

This is a Streamlit-based chatbot interface that mimics the behavior of ChatGPT. It supports both **OpenAI-powered responses** (via the official API) and **local personality-based responses** for a lightweight alternative.

---

## 🚀 Features

- 🧠 Toggle between **OpenAI GPT model** and **local dummy responder**
- 🧑‍🎤 Choose a **custom personality** for the assistant (from a YAML or JSON config)
- 💬 Persistent chat history using `st.session_state`
- 📸 Supports **custom avatars** for each persona
- 🔐 Optional email credential fields in sidebar (for future use)
- 🎛️ Clean sidebar for setting preferences
- ✅ Works with OpenAI’s latest GPT models

---

## 🖼️ Preview

*(Add a screenshot of your app here if possible)*

---

## 🛠️ Installation

1. Clone the repo:

```bash
git clone https://github.com/yourusername/chatgpt-clone.git
cd chatgpt-clone
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 Secrets Setup
Create a .streamlit/secrets.toml file to store your OpenAI key:

```bash
OPENAI_API_KEY = "your-openai-api-key"
```

## 🧾 Config Format
Create a config.yaml file in the root directory like:

```yaml
Copy code
AI personalities:
  BroGPT: |
    You are a hype bro who loves the gym and uses slang.
  MentorGPT: |
    You are a wise and calm mentor, full of support and perspective.
  ChatGPT: |
    You are the original ChatGPT personality.
  RobotGPT: |
    You respond with cold, robotic logic.

Avatars:
  BroGPT: images/brogpt.png
  MentorGPT: images/mentorgpt.png
  ChatGPT: images/chatgpt.png
  RobotGPT: images/robotgpt.png
  User: images/user.png
```
🖼 Place avatar images in the images/ folder and ensure paths match.

## ▶️ Running the App
```bash
streamlit run main.py
```

##🧹 Optional Features
- Clear chat history button wipes messages from the current session
- Email credentials input (for future integrations — currently unused)

## 📦 Project Structure

```arduino
chatgpt-clone/
├── main.py
├── utils.py
├── config.yaml
├── images/
│   ├── brogpt.png
│   ├── chatgpt.png
│   └── ...
├── .streamlit/
│   └── secrets.toml
├── requirements.txt
└── README.md
```

## 📌 Notes
- This app uses Streamlit’s experimental chat layout
- Caching is used for loading avatars and config files efficiently
- The non-OpenAI path uses a response_generator() — make sure it's implemented in utils.py

## 📃 License
MIT – do whatever you want, just don't blame me if BroGPT gets out of hand 😎

## 👨‍💻 Author
Julien C. – built with ❤️ and way too much coffee.