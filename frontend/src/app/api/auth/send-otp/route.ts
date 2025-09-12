// src/app/api/auth/send-otp/route.ts
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  const { phoneNumber } = await request.json();
  if (!phoneNumber) {
    return NextResponse.json({ message: 'Phone number is required' }, { status: 400 });
  }
  // MOCK LOGIC: In a real app, you would use Twilio here.
  console.log(`(Mock API) Sending OTP to ${phoneNumber}`);
  return NextResponse.json({ success: true, message: 'OTP sent successfully' });
}