import React from 'react';
import axios from 'axios';

export default function TodoItem(props) {
  const deleteTodoHandler = title => {
    axios
      .delete(`http://127.0.0.1:8000/api/todo/${title}`)
      .then(res => console.log(res.data));
  };

  return (
    <div>
      <span style={{ fontWeight: 'bold, underline' }}>
        {props.todo.title}:{' '}
      </span>
      {props.todo.description}
      <button
        onClick={() => deleteTodoHandler(props.todo.title)}
        className='btn btn-outline-danger my-2 mx-2'
        style={{ borderRadius: 50 }}>
        X
      </button>
      <hr />
    </div>
  );
}
