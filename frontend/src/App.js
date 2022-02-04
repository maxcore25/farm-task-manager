import './App.css';
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [todoList, setTodoList] = useState([{}]);
  const [title, setTitle] = useState('');
  const [desc, setDesc] = useState('');

  useEffect(() => {
    axios
      .get('http://127.0.0.1:8000/api/todo')
      .then(res => setTodoList(res.data));
  }, []);

  return (
    <div
      className='App list-group-item justify-content-center align-items-center mx-auto'
      style={{ width: 400, backgroundColor: 'white', marginTop: 15 }}>
      <h1
        className='card text-white bg-primary mb-1'
        style={{ maxWidth: '20rem' }}>
        Task Manager
      </h1>
      <h6 className='card text-white bg-primary mb-3'>
        FastAPI - React - MongoDB
      </h6>
      <div className='card-body'>
        <h5 className='card text-white bg-dark mb-3'>Add Your Task</h5>
        <span className='card-text'>
          <input
            type='text'
            className='mb-2 form-control titleIn'
            placeholder='Title'
          />
          <input
            type='text'
            className='mb-2 form-control desIn'
            placeholder='Description'
          />
          <button
            className='btn btn-outline-primary mx-2 mb-3'
            style={{ borderRadius: 50, fontWeight: 'bold' }}>
            Add Task
          </button>
        </span>
        <h5 className='card text-white bg-dark mb-3'>Your Tasks</h5>
        <div>{/* todo items */}</div>
      </div>
      <h6 className='card text-dark bg-warning py-1 mb-0'>
        Copyright 2022, All rights reserved &copy;
      </h6>
    </div>
  );
}

export default App;
