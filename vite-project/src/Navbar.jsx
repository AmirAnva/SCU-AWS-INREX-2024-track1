// Navbar.jsx
import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav style={styles.navbar}>
      <ul style={styles.navList}>
        <li style={styles.navItem}>
          <Link to="/" style={styles.navLink}>Home</Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/product" style={styles.navLink}>Product</Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/future" style={styles.navLink}>Future</Link>
        </li>
        <li style={styles.navItem}>
          <Link to="/scalablilty" style={styles.navLink}>Scalablilty</Link>
        </li>
      </ul>
    </nav>
  );
};

// Simple styles for the navbar
const styles = {
  navbar: {
    backgroundColor: '#333',
    padding: '10px',
  },
  navList: {
    listStyleType: 'none',
    display: 'flex',
    justifyContent: 'space-around',
    margin: 0,
    padding: 0,
  },
  navItem: {
    margin: '0 15px',
  },
  navLink: {
    color: 'white',
    textDecoration: 'none',
    fontSize: '18px',
  }
};

export default Navbar;
