import './assets/App.css';
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
      if (event.target.value === ''){
        setCompletion([])
      }
  }

  function setValue(item){
    setUserInput(item)
    setCompletion([])
  }
  return (
    <div className="App">
      <input onChange={changeInput} value={userInput}/>
      <p>{userInput}</p>
      <div style={{marginLeft: "41%"}}>
      {completion.map((item, index) => (
        <div style={{backgroundColor: "white", boxShadow: "1.5px 1.5px 1.5px lightblue", width: "30%"}}>
  <p key={index} onClick={() => setValue(item)}>{item}</p>
  </div>
))}
      </div>
    </div>
  );
}

export default App;
