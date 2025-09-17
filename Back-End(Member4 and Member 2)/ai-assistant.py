import cv2
import pytesseract
import paho.mqtt.client as mqtt
import pyttsx3
import requests
import datetime
import pytesseract

# ---------------- CONFIG ----------------
BROKER = "broker.hivemq.com"
ENTRY_TOPIC = "techfusion2k25/parking/entry"
EXIT_TOPIC = "techfusion2k25/parking/exit"
GATE_TOPIC = "techfusion2k25/parking/gate"

BACKEND_URL = "http://127.0.0.1:5000"   # Member 3 Flask server
TELEGRAM_URL = "http://127.0.0.1:8000"  # Member 4 bot service (notification API)

# Path to Tesseract (adjust if installed elsewhere)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Initialize text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 160)

# ---------------- FUNCTIONS ----------------
def speak(text):
    print("AI Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def capture_plate():
    """Capture car plate using camera + OCR"""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()
    if not ret:
        return None

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate_text = pytesseract.image_to_string(gray, config="--psm 8")
    plate_text = "".join(filter(str.isalnum, plate_text))
    return plate_text if plate_text else "UNKNOWN"

def register_entry():
    speak("Welcome to Suraksha Parking! Please wait while we capture your details.")
    plate = capture_plate()

    name = "Guest User"
    phone = "9999999999"
    entry_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    payload = {
        "name": name,
        "phone": phone,
        "plate": plate,
        "entry_time": entry_time
    }

    # Save in backend
    try:
        r = requests.post(f"{BACKEND_URL}/entry", json=payload)
        if r.status_code == 200:
            speak(f"Your car {plate} has been registered. Proceed to your slot.")
            # Notify Telegram bot
            requests.post(f"{TELEGRAM_URL}/notify", json={"msg": f"Entry: {payload}"})
            # Open gate
            mqtt_client.publish(GATE_TOPIC, "open")
        else:
            speak("Error while saving entry details.")
    except Exception as e:
        speak("Backend not reachable.")

def register_exit():
    speak("Please wait while we calculate your bill.")
    plate = capture_plate()

    exit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    payload = {"plate": plate, "exit_time": exit_time}

    try:
        r = requests.post(f"{BACKEND_URL}/exit", json=payload)
        if r.status_code == 200:
            data = r.json()
            bill = data.get("bill", 10)
            duration = data.get("duration", "1 hr")
            speak(f"Car {plate}, you parked for {duration}. Your bill is {bill} rupees.")

            # Notify Telegram bot
            requests.post(f"{TELEGRAM_URL}/notify", json={"msg": f"Exit Bill: {data}"})

            # Simulate payment confirmation (later Member 4 will confirm)
            paid = True
            if paid:
                speak("Payment received. Thank you for parking with us.")
                mqtt_client.publish(GATE_TOPIC, "open")
            else:
                speak("Please complete payment to exit.")
        else:
            speak("Error while processing exit.")
    except Exception as e:
        speak("Backend not reachable.")

# ---------------- MQTT HANDLERS ----------------
def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(ENTRY_TOPIC)
    client.subscribe(EXIT_TOPIC)

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()

    if topic == ENTRY_TOPIC and payload == "car_detected":
        register_entry()
    elif topic == EXIT_TOPIC and payload == "car_detected":
        register_exit()

# ---------------- MAIN ----------------
mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(BROKER, 1883, 60)
speak("AI Assistant is online and ready.")

mqtt_client.loop_forever()
