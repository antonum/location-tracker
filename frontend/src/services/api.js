import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const locationService = {
  // Get all available locations
  getLocations: async () => {
    try {
      const response = await api.get('/locations');
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch locations');
    }
  },

  // Add a new user
  addUser: async (userData) => {
    try {
      const response = await api.post('/users', userData);
      return response.data;
    } catch (error) {
      throw new Error('Failed to add user');
    }
  },

  // Get recent users
  getRecentUsers: async () => {
    try {
      const response = await api.get('/users/recent');
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch recent users');
    }
  },

  // Get user statistics
  getUserStats: async () => {
    try {
      const response = await api.get('/users/stats');
      return response.data;
    } catch (error) {
      throw new Error('Failed to fetch user statistics');
    }
  },

  // Health check
  healthCheck: async () => {
    try {
      const response = await api.get('/health');
      return response.data;
    } catch (error) {
      throw new Error('Backend service is not available');
    }
  }
};

export default api;
