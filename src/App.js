import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HoldingsTable from './components/HoldingsTable';
import Watchlist from './components/Watchlist';
import Sidebar from './components/Sidebar';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route path="/" element={<HoldingsTable />} />
            <Route path="/watchlist" element={<Watchlist />} />
            {/* You can add the Stocks page later */}
            <Route path="/stocks" element={<div>Stocks Page (Coming Soon)</div>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
