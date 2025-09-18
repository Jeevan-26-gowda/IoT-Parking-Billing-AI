# billing_member4.py
import asyncio
from datetime import datetime
from telegram import Bot
import qrcode

# ---------------- CONFIG ----------------
TELEGRAM_TOKEN = "7802179029:AAG719GDn35vTZvobCzO2W-0SVlNLw2d6dU"   # Your bot token
CHAT_ID = "5564840058"   # Your chat ID
RATE_PER_HOUR = 10        # Parking rate (₹10 per hour)
UPI_ID = "6361698991@ybl" # Replace with your actual UPI ID

bot = Bot(token=TELEGRAM_TOKEN)


def generate_upi_qr(upi_link, filename="upi_qr.png", size=6):
    """Generate QR code for UPI link with medium size"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,  # box_size controls the size of QR
        border=4
    )
    qr.add_data(upi_link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    return filename


async def send_bill(name, phone, car_number, entry_time, exit_time):
    """Sends a bill via Telegram with UPI payment link and QR code"""
    # Calculate parking duration in hours (rounded up)
    duration_seconds = (exit_time - entry_time).total_seconds()
    duration_hours = max(1, int(duration_seconds // 3600) + (1 if duration_seconds % 3600 > 0 else 0))
    amount = duration_hours * RATE_PER_HOUR

    # UPI payment link
    upi_link = f"upi://pay?pa={UPI_ID}&pn={name}&am={amount}&cu=INR"

    # Prepare message with clickable link
    message = f"""Suraksha Parking Bill

Name: {name}
Phone: {phone}
Car Number: {car_number}
Entry Time: {entry_time.strftime('%d-%m-%Y %H:%M:%S')}
Exit Time: {exit_time.strftime('%d-%m-%Y %H:%M:%S')}
Duration: {duration_hours} hour(s)
Amount: ₹{amount}

👉 Pay via UPI: [Click here to pay]({upi_link})
"""

    # Send message (Markdown format for clickable link)
    await bot.send_message(chat_id=CHAT_ID, text=message, parse_mode="Markdown")

    # Generate and send QR code (medium size)
    qr_file = generate_upi_qr(upi_link, size=6)
    await bot.send_photo(
        chat_id=CHAT_ID,
        photo=open(qr_file, "rb"),
        caption=f"Scan this QR to pay ₹{amount} instantly 📲"
    )

    print("✅ Bill sent via Telegram!")


# ---------------- DEMO / TEST ----------------
if __name__ == "__main__":
    # Sample data for testing
    name = "Jeevan"
    phone = "6361698991"
    car_number = "KA41S8055"
    entry_time = datetime.now().replace(hour=10, minute=0, second=0)
    exit_time = datetime.now().replace(hour=12, minute=30, second=0)

    asyncio.run(send_bill(name, phone, car_number, entry_time, exit_time))
