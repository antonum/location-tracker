import React, { useState, useEffect } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement,
} from 'chart.js';
import { Bar, Pie } from 'react-chartjs-2';
import { locationService } from '../services/api';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
  ArcElement
);

const LocationChart = ({ refreshTrigger }) => {
  const [stats, setStats] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [chartType, setChartType] = useState('bar');

  useEffect(() => {
    fetchStats();
  }, [refreshTrigger]);

  const fetchStats = async () => {
    try {
      setLoading(true);
      const data = await locationService.getUserStats();
      setStats(data);
    } catch (err) {
      setError('Failed to load statistics');
    } finally {
      setLoading(false);
    }
  };

  const generateColors = (count) => {
    const colors = [
      '#FF6384', '#36A2EB', '#FFCE56', '#4BC0C0', '#9966FF',
      '#FF9F40', '#C9CBCF', '#4BC0C0', '#FF6384', '#36A2EB',
      '#FFCE56'
    ];
    return colors.slice(0, count);
  };

  const chartData = {
    labels: stats.map(stat => stat.location),
    datasets: [
      {
        label: 'Number of Users',
        data: stats.map(stat => stat.count),
        backgroundColor: generateColors(stats.length),
        borderColor: generateColors(stats.length),
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: chartType === 'pie' ? 'right' : 'top',
      },
      title: {
        display: true,
        text: 'Users by Location (Top 10 + Others)',
      },
    },
    scales: chartType === 'bar' ? {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 1,
        },
      },
    } : {},
  };

  if (loading) {
    return (
      <div className="data-section">
        <h2>Location Statistics</h2>
        <div className="loading">Loading statistics...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="data-section">
        <h2>Location Statistics</h2>
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="data-section">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2>Location Statistics</h2>
        <div>
          <button 
            className={`btn ${chartType === 'bar' ? 'active' : ''}`}
            onClick={() => setChartType('bar')}
            style={{ marginRight: '10px', backgroundColor: chartType === 'bar' ? '#45a049' : '#4CAF50' }}
          >
            Bar Chart
          </button>
          <button 
            className={`btn ${chartType === 'pie' ? 'active' : ''}`}
            onClick={() => setChartType('pie')}
            style={{ backgroundColor: chartType === 'pie' ? '#45a049' : '#4CAF50' }}
          >
            Pie Chart
          </button>
        </div>
      </div>
      
      {stats.length === 0 ? (
        <p>No data available.</p>
      ) : (
        <div className="chart-container">
          {chartType === 'bar' ? (
            <Bar data={chartData} options={chartOptions} />
          ) : (
            <Pie data={chartData} options={chartOptions} />
          )}
        </div>
      )}
    </div>
  );
};

export default LocationChart;
