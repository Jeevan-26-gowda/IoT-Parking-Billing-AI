Title:
IoT-Driven Smart Parking & Automated Billing System with AI Assistance

Overview:
This project is designed to solve urban parking problems by integrating IoT sensors, a cloud-based backend, an AI-powered chatbot, and an automated billing system.
It allows users to find available parking slots, book them, pay automatically, and get help from a chatbot.

Features:

Real-time parking detection (Green = Free, Red = Occupied)

Slot booking with confirmation

Automated time-based billing with Razorpay integration

AI chatbot to check availability, guide booking, and show payment details

Admin dashboard to monitor parking status, revenue, and IoT devices

Project Structure:

Back-End: Node.js + Express + Firebase backend code

Front-End: React.js dashboard with Tailwind CSS

IoT-Code: ESP32 / Arduino parking sensor firmware

ChatBot: Dialogflow or GPT-powered chatbot configuration

Docs: System architecture, flowcharts, and screenshots

Tech Stack:

Frontend: React.js, Tailwind CSS

Backend: Node.js, Express, Firebase

IoT: ESP32, Ultrasonic Sensors

Chatbot: Dialogflow / GPT API

Payments: Razorpay or Paytm

How to Run:

Clone the repository using
git clone <repo-link>

Go into the folder using
cd Iot-Parking_Billing

Setup backend:

Run npm init -y

Install required packages (npm install express cors firebase-admin)

Run node server.js

Setup frontend:

Use npx create-react-app dashboard inside Front-End folder

Install required packages (npm install axios react-router-dom)

Run frontend using npm start

Demo Flow:

Open the app to see parking layout

Chatbot shows available slots when asked

User selects a slot and books it

Billing starts automatically

When user exits, app shows amount due → pay via Razorpay → slot becomes free

Team Roles:

IoT Engineer: Sensor setup and programming

Backend Developer: API creation and database integration

UI Developer: Dashboard, booking flow, and chatbot widget

AI Specialist: Chatbot training and natural language processing setup

License:
MIT License (free to use and modify).

Contribution:

Fork the repo

Create a feature branch

Commit your changes

Submit a pull request

Support:
If you like this project, star it on GitHub.
