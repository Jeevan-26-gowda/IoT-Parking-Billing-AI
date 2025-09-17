# Backend (Member 3)

This folder contains the backend API code for the IoT Smart Parking System.

## Purpose
- Handles requests from AI Assistant (Member 2)
- Manages parking slot assignment
- Logs car entry and exit times
- Calculates parking fees for billing (Member 4)
- Provides data for real-time monitoring and slot availability

## Files
- `backend_member3.py` : Main backend API server (Flask or FastAPI)
- `database/` : SQLite database files to store car entries, exits, and slots
- `utils/` : Helper functions for slot assignment and fee calculation

## Dependencies
- Python 3.10+
- `flask` or `fastapi`
- `requests`
- `sqlite3` (built-in)
- `pydantic` (if using FastAPI)

Install dependencies:
```bash
pip install -r requirements.txt
