// src/app/page.tsx
'use client';
import { useEffect } from 'react';
import { useRouter } from 'next/navigation';

export default function HomePage() {
  const router = useRouter();
  useEffect(() => {
    // For now, we'll just redirect everyone to the login page.
    router.replace('/login');
  }, [router]);

  return <div className="flex items-center justify-center min-h-screen"><p>Loading...</p></div>;
}