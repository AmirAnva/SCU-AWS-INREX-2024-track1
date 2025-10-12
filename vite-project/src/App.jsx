import { useState } from 'react'
import './App.css'
import MyMap from './map'
import axios from 'axios';

function App() {
  // const [id, setId] = useState(1)

  
  // const handleIdChange = (e) => {
  //   const val = e.target.value;
  //   const number = parseInt(val, 10) || 1;
  //   if (!isNaN(number)) {
  //     setId(Math.max(1, number));
  //   }
  // };

  return (
    <>
      <h1>VisionFlow AI 🚦</h1>
        <MyMap />
    </>
  )
}

export default App
