import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'

function App() {
  const [todos, setTodos] = useState([]);

  const res = axios.get('http://127.0.0.1:8000/api/')
    .then(res => { setTodos(res.data) }
    )
    .catch(err => {
     console.log(err);
    })
  return (

    <div>
      {todos.map(todo => (
        <div key={todo.id}>
          <h1>{todo.title}</h1>
          <p>{todo.body}</p>
        </div>
      ))}
    </div>
  )
}

export default App;
