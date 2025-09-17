
---

## **2️⃣ Hardware (Member 1)**

**Path:** `Hardware/`  

```markdown
# Hardware (Member 1)

This folder contains the hardware and IoT code for the Smart Parking System.

## Purpose
- Controls and monitors parking slots
- Uses IR sensors for slot occupancy detection
- Uses ultrasonic sensors for vehicle detection at entry and exit points
- Operates LEDs to indicate free/occupied slots
- Controls servo motor barrier for vehicle entry/exit
- Communicates with AI assistant (Member 2) via MQTT

## Files
- `esp32_parking.ino` : Main ESP32 code to handle sensors, LEDs, and servo
- `utils/` : Helper code for sensor readings and MQTT communication
- `config/` : WiFi and MQTT broker configuration files

## Hardware Components
- ESP32 development board
- IR sensors (one per parking slot)
- Ultrasonic sensors (for entry and exit detection)
- LEDs for slot availability
- Servo motor for entry/exit barrier
- Jumper wires, breadboard, and power supply

## How to Upload Code
1. Install Arduino IDE and add ESP32 board support
2. Connect ESP32 to your PC via USB
3. Open `esp32_parking.ino` in Arduino IDE
4. Select correct board and COM port
5. Upload the code
6. Ensure WiFi and MQTT settings are configured correctly in `config/`
