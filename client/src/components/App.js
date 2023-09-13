import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom"
import '../styling/App.css';
import Home from './Home';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path = "/Home" element = { <Home/> } />
          <Route path = "*" element = { <Navigate to = "/Home" replace /> }/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
