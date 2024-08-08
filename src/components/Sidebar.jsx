import React from 'react';
import { Link } from 'react-router-dom';
import './css/Sidebar.css';
import profileImage from '../images/profile-img.png'; // Import the profile image

const Sidebar = () => {
  return (
    <div className="sidebar">
      <div className="profile">
        <img src={profileImage} alt="Profile" className="profile-image" />
        <h2 className="username">John Doe</h2>
      </div>
      <div className="nav-buttons">
        <Link to="/" className="nav-button">Holdings</Link>
        <Link to="/watchlist" className="nav-button">Watchlist</Link>
        <Link to="/stocks" className="nav-button">Stocks</Link>
      </div>
    </div>
  );
};

export default Sidebar;
