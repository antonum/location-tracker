import React, { useState, useEffect } from 'react';
import { locationService } from '../services/api';

const RecentUsers = ({ refreshTrigger }) => {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchRecentUsers();
  }, [refreshTrigger]);

  const fetchRecentUsers = async () => {
    try {
      setLoading(true);
      const data = await locationService.getRecentUsers();
      setUsers(data);
    } catch (err) {
      setError('Failed to load recent users');
    } finally {
      setLoading(false);
    }
  };

  const formatDate = (dateString) => {
    const date = new Date(dateString);
    return date.toLocaleString();
  };

  if (loading) {
    return (
      <div className="data-section">
        <h2>Recent Users</h2>
        <div className="loading">Loading recent users...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="data-section">
        <h2>Recent Users</h2>
        <div className="error">{error}</div>
      </div>
    );
  }

  return (
    <div className="data-section">
      <h2>Recent Users (Last 10)</h2>
      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <div className="table-container">
          <table className="users-table">
            <thead>
              <tr>
                <th>Name</th>
                <th>Location</th>
                <th>Date Added</th>
              </tr>
            </thead>
            <tbody>
              {users.map((user) => (
                <tr key={user.id}>
                  <td>{user.name}</td>
                  <td>{user.location}</td>
                  <td>{formatDate(user.timestamp)}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
};

export default RecentUsers;
