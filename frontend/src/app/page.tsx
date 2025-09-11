// src/app/page.tsx
'use client'; // Add this line at the top, it's important

import { useState } from 'react';
import ParkingSlot, { type Slot } from './components/ParkingSlot';

// Mock data that would normally come from your IoT sensors
const mockParkingSlots: Slot[] = [
  { id: 'A-01', status: 'occupied' }, { id: 'A-02', status: 'available' },
  { id: 'A-03', status: 'available' }, { id: 'A-04', status: 'occupied' },
  { id: 'A-05', status: 'available' }, { id: 'B-01', status: 'available' },
  { id: 'B-02', status: 'occupied' }, { id: 'B-03', status: 'available' },
  { id: 'B-04', status: 'available' }, { id: 'B-05', status: 'occupied' },
];

export default function DashboardPage() {
  const [slots, setSlots] = useState<Slot[]>(mockParkingSlots);
  const availableSlots = slots.filter(s => s.status === 'available').length;
  
  const handleSlotClick = (slot: Slot) => {
    // We will add the booking modal logic here later
    alert(`You clicked on available slot: ${slot.id}`);
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="p-4 bg-white border-b shadow-sm">
        <h1 className="text-2xl font-bold text-gray-800">IoT Parking Dashboard</h1>
        <p className="text-gray-600">
          Welcome, Lion! There are{" "}
          <span className="font-bold text-green-600">{availableSlots}</span> slots available.
        </p>
      </header>
      
      <main className="p-8">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">Parking Lot Overview</h2>
        
        {/* The Parking Map Grid */}
        <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5">
          {slots.map((slot) => (
            <ParkingSlot key={slot.id} slot={slot} onClick={handleSlotClick} />
          ))}
        </div>
      </main>
    </div>
  );
}