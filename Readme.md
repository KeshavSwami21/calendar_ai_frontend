# 📅 Google Calendar Booking Chatbot (Frontend)

This **Streamlit app** provides a **clean, conversational interface** for users to **book appointments on your Google Calendar** seamlessly.

It connects to a **FastAPI backend** that handles:
✅ Natural language processing.
✅ Google Calendar availability checks.
✅ Automatic event booking.

---

## 🚀 Features

✅ **Conversational UI**: Users can book appointments just by chatting.
✅ **Google Calendar Integration**: Checks availability and confirms bookings.
✅ **Real-time feedback**: Shows booking confirmation with a link.
✅ **Completely free deployment** on Streamlit Community Cloud.

---

## 🖥️ Live Demo

🌐 [View Live Streamlit App Here](https://calendar-ai-agent.streamlit.app/)

---

## 🛠️ Tech Stack

* **Frontend**: [Streamlit](https://streamlit.io/)
* **Backend**: FastAPI (connected via HTTP API)
* **API Calls**: Uses `requests` to communicate with your backend.

---

## 📦 Installation (Local)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/calendar-bot-frontend.git
cd calendar-bot-frontend
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Update Backend URL

In `streamlit_app.py`, replace:

```python
"https://your-backend-url/chat"
```

with your **FastAPI backend URL** deployed on Render.

---

### 5️⃣ Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Your app will open in your browser automatically.

---

## 🚀 Deployment on Streamlit Cloud (Free)

1️⃣ Push your repo to GitHub.

2️⃣ Go to [Streamlit Cloud](https://streamlit.io/cloud) and sign in.

3️⃣ Click **“New app”** and connect your GitHub repo.

4️⃣ Select:

* Branch: `main`
* File: `streamlit_app.py`

5️⃣ Click **“Deploy.”**

Your **free live app will be ready** to share.

---

## 📄 File Structure

```
calendar-bot-frontend/
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

## ✨ Usage

✅ Open the app.
✅ Type:

> “Book a dentist appointment on July 4th at 2 PM.”

✅ The bot will:

* Parse your request.
* Call your FastAPI backend.
* Check your calendar.
* Book the slot if available.
* Return a clickable Google Calendar event link.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```
3. Commit changes:

   ```bash
   git commit -m "Add feature"
   ```
4. Push to the branch:

   ```bash
   git push origin feature-name
   ```
5. Open a Pull Request.

---

## 📧 Contact

If you have any questions:

* [Keshav Swami](https://portfolio2112.netlify.app/)
* Email: [keshavswami2112@gmail.com](mailto:keshavswami2112@gmail.com)

---

## ⭐️ Acknowledgements

✅ Built for internship learning.
✅ Uses **Streamlit**, **FastAPI**, and **LangChain** to build practical AI products.

---
