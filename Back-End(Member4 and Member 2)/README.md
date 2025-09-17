# Back-End (Member 2 & Member 4)

This folder contains the backend code for the IoT Smart Parking System, handling API endpoints, data storage, and communication with AI assistant and billing system.

## Purpose
- Receives parking and exit details from AI assistant (Member 2)
- Stores car entry, exit, and billing information
- Provides available parking slots to AI assistant
- Integrates with Telegram bot for billing notifications (Member 4)

## Files
- `backend_member3.py` : Main backend server (Flask or FastAPI)
- `billing_member4.py` : Handles Telegram billing messages & UPI link
- `database/` : Stores SQLite or JSON database files
- `utils/` : Helper functions for data validation, calculations, and formatting

## Dependencies
- Python 3.10+
- `flask` or `fastapi`
- `requests`
- `python-telegram-bot`
- `asyncio`
- `sqlite3` (built-in)

Install dependencies:
```bash
pip install -r requirements.txt
