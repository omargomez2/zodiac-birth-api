# app.py
# FastAPI example
# Install:
# pip install fastapi uvicorn

from fastapi import FastAPI
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import calendar

app = FastAPI(title="Birth Info API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ZODIAC_SIGNS = [
    ((1, 20), "Capricorn", "Disciplined, ambitious, practical, and responsible."),
    ((2, 19), "Aquarius", "Independent, creative, intelligent, and visionary."),
    ((3, 21), "Pisces", "Empathetic, intuitive, artistic, and emotional."),
    ((4, 20), "Aries", "Energetic, courageous, competitive, and confident."),
    ((5, 21), "Taurus", "Reliable, patient, loyal, and determined."),
    ((6, 21), "Gemini", "Curious, adaptable, communicative, and witty."),
    ((7, 23), "Cancer", "Protective, emotional, caring, and intuitive."),
    ((8, 23), "Leo", "Charismatic, proud, passionate, and generous."),
    ((9, 23), "Virgo", "Analytical, organized, practical, and detail-oriented."),
    ((10, 23), "Libra", "Diplomatic, charming, balanced, and sociable."),
    ((11, 22), "Scorpio", "Intense, determined, mysterious, and passionate."),
    ((12, 22), "Sagittarius", "Optimistic, adventurous, honest, and freedom-loving."),
    ((12, 32), "Capricorn", "Disciplined, ambitious, practical, and responsible.")
]


def get_zodiac(month: int, day: int):
    for (end_month, end_day), sign, personality in ZODIAC_SIGNS:
        if (month, day) < (end_month, end_day):
            return sign, personality
    return "Unknown", "Unknown personality"


@app.get("/birth-info")
def birth_info(date: str):
    """
    Example:
    /birth-info?date=1995-07-14
    """

    try:
        birth_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return {
            "error": "Invalid date format. Use YYYY-MM-DD"
        }

    weekday = calendar.day_name[birth_date.weekday()]
    zodiac, personality = get_zodiac(
        birth_date.month,
        birth_date.day
    )

    return {
        "birth_date": date,
        "day_of_week": weekday,
        "zodiac_sign": zodiac,
        "personality": personality
    }