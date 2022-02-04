import React from 'react';
import TodoItem from './TodoItem';

export default function TodoListView(props) {
  return (
    <ul>
      {props.todoList.map(todo => (
        <TodoItem todo={todo} />
      ))}
    </ul>
  );
}
