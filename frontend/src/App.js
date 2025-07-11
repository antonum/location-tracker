import React, { useState, useEffect } from 'react';
import UserForm from './components/UserForm';
import RecentUsers from './components/RecentUsers';
import LocationChart from './components/LocationChart';
import { locationService } from './services/api';

function App() {
  const [refreshTrigger, setRefreshTrigger] = useState(0);
  const [backendStatus, setBackendStatus] = useState('checking');

  useEffect(() => {
    checkBackendHealth();
  }, []);

  const checkBackendHealth = async () => {
    try {
      await locationService.healthCheck();
      setBackendStatus('healthy');
    } catch (error) {
      setBackendStatus('unhealthy');
    }
  };

  const handleUserAdded = () => {
    // Increment refresh trigger to update components
    setRefreshTrigger(prev => prev + 1);
  };

  return (
    <div className="container">
      <header className="header">
        <img 
          src="https://console.cloud.timescale.com/assets/tiger-cloud-logo-EtpbKf2C.svg" 
          alt="Timescale Cloud" 
          style={{ height: '60px', marginBottom: '20px' }}
        />
        <h1>Location Tracker</h1>
        <p>Track user locations and view statistics</p>
        <div style={{ fontSize: '14px', color: backendStatus === 'healthy' ? '#4CAF50' : '#f44336' }}>
          Backend Status: {backendStatus === 'checking' ? 'Checking...' : 
                          backendStatus === 'healthy' ? '✅ Connected' : '❌ Disconnected'}
        </div>
      </header>

      <main>
        <UserForm onUserAdded={handleUserAdded} />
        <RecentUsers refreshTrigger={refreshTrigger} />
        <LocationChart refreshTrigger={refreshTrigger} />
      </main>

      <footer style={{ textAlign: 'center', marginTop: '40px', color: '#666' }}>
        <p>© 2025 Location Tracker App</p>
      </footer>
    </div>
  );
}

export default App;
