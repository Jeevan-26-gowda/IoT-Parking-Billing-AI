# Front-End (Member 2: AI Assistant)

This folder contains the AI assistant code for our IoT Smart Parking System.

## Purpose
- Handles voice interaction with users (speech-to-text & text-to-speech)
- Captures car details via OCR from camera
- Communicates with ESP32 (Member 1) via MQTT
- Sends parking and exit info to backend (Member 3)

## Files
- `ai-assistant.py` : Main AI assistant script
- `utils/` : Helper functions for OCR, MQTT, etc.
- `tts/` and `stt/` : Text-to-speech and speech-to-text modules

## How to Run
1. Activate virtual environment:
   ```bash
   python -m venv venv
   source venv/Scripts/activate   # Windows
