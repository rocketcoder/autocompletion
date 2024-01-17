import logo from './logo.svg';
import './App.css';
import { useState } from 'react'
import axios from 'axios'
function App() {
  const [userInput, setUserInput] = useState('')
  const [completion, setCompletion] = useState([])
  async function changeInput(event){
    setUserInput(event.target.value)
    console.log(event.target.value)
      const body = {
        'msg': event.target.value
      }
      const request = await axios.post('http://localhost:5000', body)
      setCompletion(request.data)
  }
  return (
    <div className="App">
      <input onChange={changeInput}/>
      <p>{userInput}</p>
      {completion.map((item, index) => (
  <p key={index}>{item}</p>
))}
    </div>
  );
}

export default App;
