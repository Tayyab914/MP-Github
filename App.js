import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import StudentDashboard from './pages/StudentDashboard';
import TeacherDashboard from './pages/TeacherDashboard';

function App() {
  return (
    
      <div className="App">
        {/* Define the Routes for different pages */}
        <Router>
        <Routes>
          
          <Route path="/" element={<LoginPage />} />
          <Route path="/sd" element={<StudentDashboard />} />
          <Route path="/td" element={<TeacherDashboard />} />

          
          
        </Routes>
      
        </Router>
    
    </div>
  );
}

export default App;
