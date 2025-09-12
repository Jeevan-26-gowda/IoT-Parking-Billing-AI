// src/app/components/ParkingSlot.tsx
import { MapPinIcon } from '@heroicons/react/24/outline';

// Define the shape of the data for a single slot
export type Slot = {
  id: string;
  status: 'available' | 'occupied';
};

// Define the props that the component will accept
type ParkingSlotProps = {
  slot: Slot;
  onClick: (slot: Slot) => void;
};

export default function ParkingSlot({ slot, onClick }: ParkingSlotProps) {
  const isAvailable = slot.status === 'available';

  // These are the base styles for all slots
  const baseClasses = 
    "flex flex-col items-center justify-center p-4 rounded-lg text-center font-bold transition-transform transform shadow-sm border";
  
  // These styles are applied conditionally based on the slot's status
  const statusClasses = isAvailable
    ? "bg-green-100 text-green-800 border-green-200 cursor-pointer hover:scale-105 hover:bg-green-200"
    : "bg-red-100 text-red-800 border-red-200 cursor-not-allowed opacity-60";

  return (
    <div 
      className={`${baseClasses} ${statusClasses}`} 
      onClick={() => {
        if (isAvailable) {
          onClick(slot);
        }
      }}
    >
      <MapPinIcon className="icon-size mb-2" />
      <span>{slot.id}</span>
    </div>
  );
}