import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Sidebar from './components/Sidebar';
import HoldingsTable from './components/HoldingsTable';
import Watchlist from './components/Watchlist';
import Transactions from './components/Transactions';
import './App.css';

const App = () => {
  return (
    <Router>
      <div className="app">
        <Sidebar />
        <div className="content">
          <Routes>
            <Route path="/" element={<HoldingsTable />} />
            <Route path="/watchlist" element={<Watchlist />} />
            <Route path="/transactions" element={<Transactions />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
};

export default App;
