import datetime
import pytz
from telegram import Bot

# ------------------ CONFIG ------------------
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your bot token
CHAT_ID = "YOUR_CHAT_ID_HERE"           # Replace with your numeric Telegram ID
PRICE_PER_HOUR = 10                      # ₹10 per hour

bot = Bot(token=TELEGRAM_TOKEN)

# ------------------ BILLING FUNCTION ------------------
def calculate_bill(entry_time, exit_time):
    duration = exit_time - entry_time
    total_minutes = duration.total_seconds() / 60
    hours = total_minutes / 60
    # Minimum 1 hour charge
    amount = int((hours if hours > 1 else 1) * PRICE_PER_HOUR)
    return duration, amount

# ------------------ SEND BILL ------------------
def send_bill(name, phone, car_plate, entry_time, exit_time):
    duration, amount = calculate_bill(entry_time, exit_time)
    
    message = f"""
🚗 *Suraksha Smart Parking*

👤 Name: {name}
📞 Phone: {phone}
🚘 Car: {car_plate}

🕒 Entry: {entry_time.strftime("%Y-%m-%d %H:%M:%S")}
🕒 Exit: {exit_time.strftime("%Y-%m-%d %H:%M:%S")}
⏳ Duration: {str(duration).split('.')[0]}

💰 Total Amount: ₹{amount}

✅ Pay via UPI: `upi://pay?pa=parking@upi&pn=SurakshaParking&am={amount}`
"""
    bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")
    print("✅ Bill sent via Telegram!")

# ------------------ TEST ------------------
if __name__ == "__main__":
    tz = pytz.timezone("Asia/Kolkata")
    
    # Dummy test data
    entry_time = datetime.datetime(2025, 9, 17, 10, 30, tzinfo=tz)
    exit_time = datetime.datetime(2025, 9, 17, 12, 45, tzinfo=tz)
    
    send_bill(
        name="Jeevan",
        phone="9876543210",
        car_plate="KA01AB1234",
        entry_time=entry_time,
        exit_time=exit_time
    )
