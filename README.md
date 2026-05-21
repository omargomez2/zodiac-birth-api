# 🌌 Cosmic Profile API

A modern FastAPI project that returns:

- 📅 Day of the week of birth
- ♈ Zodiac constellation/sign
- ✨ Brief personality characteristics

Includes:

- FastAPI backend
- Beautiful HTML/CSS/JS frontend
- REST API endpoint
- Simple setup for beginners

---

# 🚀 Features

- Fast API response
- Clean JSON output
- Modern responsive UI
- Vanilla JavaScript frontend
- Easy to deploy
- Beginner friendly

---

# 📸 Preview

Example response:

```json
{
  "birth_date": "1995-07-14",
  "day_of_week": "Friday",
  "zodiac_sign": "Cancer",
  "personality": "Protective, emotional, caring, and intuitive."
}
```

---

# 📂 Project Structure

```bash
zodiac-birth-api-main/
│
├── zodiacbirth-api.py
├── zodiacbirth-client.html
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/omargomez2/zodiac-birth-api.git
```

## 2. Enter the project folder

```bash
cd zodiac-birth-api-main
```

## 3. Create virtual environment (recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```


# ▶️ Run the API

```bash
uvicorn app:zodiacbirth-api --reload
```

Server will start at:

```text
http://127.0.0.1:8000
```

---

# 🔥 API Endpoint

## GET `/birth-info`

### Example

```text
http://127.0.0.1:8000/birth-info?date=1995-07-14
```

---

# 📥 Example Response

```json
{
  "birth_date": "1995-07-14",
  "day_of_week": "Friday",
  "zodiac_sign": "Cancer",
  "personality": "Protective, emotional, caring, and intuitive."
}
```

---

# 🌐 Frontend Setup

Simply open:

```bash
zodiacbirth-api.html
```

in your browser.

Make sure the FastAPI server is running first.

---

# 🧠 Technologies Used

- Python
- FastAPI
- Uvicorn
- HTML5
- CSS3
- JavaScript

---

# 🚀 Future Improvements

- Chinese zodiac support
- Horoscope generation
- Astrology charts
- Database storage
- User authentication
- AI personality analysis
- Docker deployment

---

# ☁️ Deployment Options

You can deploy this project using:

- Render
- Railway
- Vercel (frontend)
- Netlify (frontend)
- Docker
- AWS
- DigitalOcean

---


# 📜 License

MIT License
