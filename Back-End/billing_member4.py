# billing_member4.py
import asyncio
from datetime import datetime
from telegram import Bot

# ---------------- CONFIG ----------------
TELEGRAM_TOKEN = "7802179029:AAG719GDn35vTZvobCzO2W-0SVlNLw2d6dU"
CHAT_ID = "5564840058"
RATE_PER_HOUR = 10  # 10 rupees per hour

bot = Bot(token=TELEGRAM_TOKEN)

async def send_bill(name, phone, car_number, entry_time, exit_time):
    """
    Sends a bill via Telegram with UPI payment link
    """
    # Calculate parking duration in hours (rounded up)
    duration_seconds = (exit_time - entry_time).total_seconds()
    duration_hours = max(1, int(duration_seconds // 3600) + (1 if duration_seconds % 3600 > 0 else 0))
    amount = duration_hours * RATE_PER_HOUR

    # Format UPI link (replace YOURUPIID with your UPI ID)
    upi_link = f"upi://pay?pa=6361698991@ybl={name}&am={amount}&cu=INR"

    # Prepare message
    message = f"""*Suraksha Parking Bill*
    
*Name:* {name}
*Phone:* {phone}
*Car Number:* {car_number}
*Entry Time:* {entry_time.strftime('%d-%m-%Y %H:%M:%S')}
*Exit Time:* {exit_time.strftime('%d-%m-%Y %H:%M:%S')}
*Duration:* {duration_hours} hour(s)
*Amount:* ₹{amount}

Click here to pay: [Pay via UPI]({upi_link})
"""

    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
    print("✅ Bill sent via Telegram!")

# ---------------- DEMO / TEST ----------------
if __name__ == "__main__":
    # Sample data
    name = "Jeevan"
    phone = "6361698991"
    car_number = "KA41S8055"
    entry_time = datetime.now().replace(hour=10, minute=0, second=0)
    exit_time = datetime.now().replace(hour=12, minute=30, second=0)

    asyncio.run(send_bill(name, phone, car_number, entry_time, exit_time))
