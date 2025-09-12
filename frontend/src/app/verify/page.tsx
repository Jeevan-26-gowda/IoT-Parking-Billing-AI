// src/app/verify/page.tsx
'use client';
import { useState, type FormEvent, useEffect } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';

export default function VerifyPage() {
  const [otp, setOtp] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const router = useRouter();
  const searchParams = useSearchParams();
  const phone = searchParams.get('phone');

  useEffect(() => {
    if (!phone) router.push('/login');
  }, [phone, router]);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setLoading(true);
    setError('');
    const res = await fetch('/api/auth/verify-otp', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ phoneNumber: phone, otp }),
    });
    setLoading(false);
    if (res.ok) {
      router.push('/dashboard');
    } else {
      setError('Invalid OTP. Please try again.');
    }
  };

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="w-full max-w-md p-8 space-y-6 bg-white rounded-lg shadow-md">
        <div className="text-center">
          <h2 className="text-3xl font-extrabold text-gray-900">Verify Your Phone</h2>
          <p className="mt-2 text-sm text-gray-600">Enter the code sent to {phone}</p>
        </div>
        <form className="space-y-6" onSubmit={handleSubmit}>
          <div>
            <input id="otp" name="otp" type="text" maxLength={6} required value={otp}
              onChange={(e) => setOtp(e.target.value)}
              className="w-full px-3 py-2 text-lg tracking-widest text-center border border-gray-300 rounded-md"
              placeholder="_ _ _ _ _ _" />
          </div>
          {error && <p className="text-sm text-center text-red-600">{error}</p>}
          <div>
            <button type="submit" disabled={loading}
              className="w-full px-4 py-2 text-sm font-medium text-white bg-indigo-600 rounded-md hover:bg-indigo-700 disabled:bg-indigo-400">
              {loading ? 'Verifying...' : 'Verify & Login'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}