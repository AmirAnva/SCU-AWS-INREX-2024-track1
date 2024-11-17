import { useState } from 'react'
import './App.css'
import MyMap from './map'
import axios from 'axios';

function App() {
  const [id, setId] = useState(1)

  const [img, setImg] = useState(null)
  
  const handleIdChange = (e) => {
    const val = e.target.value;
    const number = parseInt(val, 10) || 1;
    if (!isNaN(number)) {
      setId(Math.max(1, number));
    }
  };

  function getData() {
    axios({
      method: "GET",
      url: `http://172.31.146.192:8080/${id}`
    })
    .then((response) => {
      const res =response.data
      setImg(({
        id: res.Id,
        image: `data:image/jpeg;base64,${res.Image}`,
        status: res.Status,
        content: res.Content}))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}


    

  return (
    <>
      <h1>Transportation Data</h1>
      <div className="card">
        <form onSubmit={(e) => {
          e.preventDefault();
          getData();
        }}>
         <input type="number" value={id} onChange={handleIdChange} style={{ marginBottom: '10px' }} min="1" />
         <br />
        <button type="submit">Fetch Data</button>
        </form>
        <p>
          Camera ID: {id}
        </p>
      </div>
   
        <MyMap />
        <div>
        {img && (
          <div>
            <p>ID: {img.id}</p>
            {img.image && <img src={img.image} alt={`Camera ${img.id}`} style={{ width: "300px", height: "auto" }} />}
            <p>Status: {img.status}</p>
            <div>
              <p>Congestion: {img.content.Congestion}</p>
              <p>Car Accident: {img.content["Car Accident"]}</p>
              <p>Weather: {img.content.Weather}</p>
            </div>
          </div>
        )}
        </div>
    </>
  )
}

export default App
