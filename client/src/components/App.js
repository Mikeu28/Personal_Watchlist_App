import React from 'react';
import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom"
import '../styling/App.css';
import Home from './Home';
import LogIn from './LogIn';
import SignUp from './SignUp';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
          <Route path = "/Home" element = { <Home/> } />
          <Route path = "*" element = { <Navigate to = "/Home" replace /> }/>
          <Route path = "/Login" element = { <LogIn/> } />
          <Route path = "/SignUp" element = { <SignUp/> } />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
