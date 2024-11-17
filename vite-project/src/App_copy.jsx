import { useState } from 'react'
import './App.css'
import MyMap from './map'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import axios from 'axios';

const Home = () => <h2>Home Page</h2>;
const Product = () => <h2>About Page</h2>;
const Future = () => <h2>Services Page</h2>;
const Scalablilty = () => <h2>Contact Page</h2>;

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
      //url: `http://127.0.0.1:8080/?id=${id}`, // Explicitly define the URL
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
  
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(success, error);
    } else {
      console.log("Geolocation not supported");
    }
    
    function success(position) {
      const latitude = position.coords.latitude;
      const longitude = position.coords.longitude;
      console.log(`Latitude: ${latitude}, Longitude: ${longitude}`);
    }
    
    function error() {
      console.log("Unable to retrieve your location");
    }

  return (
    <>
    <Router>
      <Navbar />
      <div style={{ padding: '20px' }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/product" element={<Product />} />
          <Route path="/future" element={<Future />} />
          <Route path="/scalablilty" element={<Scalablilty />} />
        </Routes>
      </div>
    </Router>

      
      
      <MyMap/>
    
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


      
        
    </>
  )
}

export default App
