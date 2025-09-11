// src/app/page.tsx
export default function DashboardPage() {
  const availableSlots = 5; // We will make this number dynamic later

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="p-4 bg-white border-b shadow-sm">
        <h1 className="text-2xl font-bold text-gray-800">
          IoT Parking Dashboard
        </h1>
        <p className="text-gray-600">
          Welcome, Lion! There are{" "}
          <span className="font-bold text-green-600">{availableSlots}</span> slots
          available.
        </p>
      </header>

      {/* Main Content Area */}
      <main className="p-8">
        <h2 className="text-xl font-semibold text-gray-700 mb-4">
          Parking Lot Overview
        </h2>
        {/* The Parking Map component will go here later */}
        <p className="text-gray-500">Loading parking map...</p>
      </main>
    </div>
  );
}