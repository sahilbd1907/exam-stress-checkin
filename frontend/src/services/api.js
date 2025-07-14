import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000", // Connect to your backend later
});

export const analyzeJournal = (data) => API.post('/analyze', data);
export const fetchDashboard = () => API.get('/dashboard');
export const checkAlerts = (data) => API.post('/alert', data);
