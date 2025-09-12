// src/app/api/auth/verify-otp/route.ts
import { NextResponse } from 'next/server';

export async function POST(request: Request) {
  const { phoneNumber, otp } = await request.json();
  if (!phoneNumber || !otp) {
    return NextResponse.json({ message: 'Phone number and OTP are required' }, { status: 400 });
  }
  // MOCK LOGIC: We'll accept any 6-digit code as valid for this demo.
  console.log(`(Mock API) Verifying OTP ${otp} for ${phoneNumber}`);
  if (otp.length === 6) {
    return NextResponse.json({ success: true, message: 'OTP verified' });
  } else {
    return NextResponse.json({ success: false, message: 'Invalid OTP' }, { status: 400 });
  }
}