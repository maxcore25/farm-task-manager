import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  return (
    <div className='App'>
      <div
        className='App list-group-item justify-content-center align-items-center mx-auto'
        style={{ width: 400, backgroundColor: 'white', marginTop: 15 }}>
        <h1
          className='card text-white bg-primary mb-1'
          styleName='max-width: 20rem;'>
          Task Manager
        </h1>
      </div>
    </div>
  );
}

export default App;
