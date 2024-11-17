import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import MyMap from './map'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';

const Home = () => <h2>Home Page</h2>;
const Product = () => <h2>About Page</h2>;
const Future = () => <h2>Services Page</h2>;
const Scalablilty = () => <h2>Contact Page</h2>;

function App() {
  const [count, setCount] = useState(0)

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



      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
        
    </>
  )
}

export default App
