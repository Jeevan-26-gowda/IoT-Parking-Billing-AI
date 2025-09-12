// src/app/api/auth/send-otp/route.ts
import { NextResponse } from 'next/server';
import twilio from 'twilio';

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const verifyServiceSid = process.env.TWILIO_VERIFY_SERVICE_SID;

const client = twilio(accountSid, authToken);

export async function POST(request: Request) {
  const { phoneNumber } = await request.json();

  if (!phoneNumber || !verifyServiceSid) {
    return NextResponse.json({ message: 'Missing required fields' }, { status: 400 });
  }

  try {
    await client.verify.v2.services(verifyServiceSid)
      .verifications
      .create({ to: phoneNumber, channel: 'sms' });

    return NextResponse.json({ success: true, message: 'OTP sent successfully' });

  } catch (error) {
    console.error('Twilio API error:', error);
    return NextResponse.json({ success: false, message: 'Failed to send OTP' }, { status: 500 });
  }
}