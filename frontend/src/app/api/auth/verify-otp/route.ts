// src/app/api/auth/verify-otp/route.ts
import { NextResponse } from 'next/server';
import twilio from 'twilio';

const accountSid = process.env.TWILIO_ACCOUNT_SID;
const authToken = process.env.TWILIO_AUTH_TOKEN;
const verifyServiceSid = process.env.TWILIO_VERIFY_SERVICE_SID;

const client = twilio(accountSid, authToken);

export async function POST(request: Request) {
  const { phoneNumber, otp } = await request.json();

  if (!phoneNumber || !otp || !verifyServiceSid) {
    return NextResponse.json({ message: 'Missing required fields' }, { status: 400 });
  }

  try {
    const verification_check = await client.verify.v2.services(verifyServiceSid)
      .verificationChecks
      .create({ to: phoneNumber, code: otp });

    if (verification_check.status === 'approved') {
      // TODO: Add session creation logic here next
      return NextResponse.json({ success: true, message: 'OTP verified' });
    } else {
      return NextResponse.json({ success: false, message: 'Invalid OTP' }, { status: 400 });
    }

  } catch (error) {
    console.error('Twilio API error:', error);
    return NextResponse.json({ success: false, message: 'Failed to verify OTP' }, { status: 500 });
  }
}