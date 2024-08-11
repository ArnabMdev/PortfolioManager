import React, { useState, useEffect } from 'react';
import './css/Transactions.css';

const Transactions = () => {
  const [transactions, setTransactions] = useState([]);
  const [visibleRows, setVisibleRows] = useState(10); // Initial number of visible rows

  useEffect(() => {
    // Fetch current transactions data from the API
    fetch('https://7d17-13-233-233-6.ngrok-free.app/api/transactions', {
      method: 'GET',
      headers: new Headers({
        "ngrok-skip-browser-warning": "69420"
      })
    })
    .then(response => response.json())
    .then(data => {
      setTransactions(data);
    })
    .catch(error => console.error('Error fetching transactions data:', error));
  }, []);

  const handleLoadMore = () => {
    setVisibleRows(transactions.length); // Show all rows
  };

  return (
    <div className="transactions-container">
      <div className="content">
        <div className="table-container">
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <h2>Transactions</h2>
          </div>
          <table className="transactions-table">
            <thead>
              <tr>
                <th>Ticker</th>
                <th>Transaction Type</th>
                <th>Quantity</th>
                <th>Price Rate</th>
              </tr>
            </thead>
            <tbody>
              {transactions.slice(0, visibleRows).map((transaction, index) => (
                <tr key={index}>
                  <td>{transaction.ticker}</td>
                  <td>{transaction.txn_type}</td>
                  <td>{transaction.qty}</td>
                  <td>₹{transaction.price_rate.toFixed(2)}</td>
                </tr>
              ))}
            </tbody>
          </table>
          {visibleRows < transactions.length && (
            <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '10px' }}>
              <button onClick={handleLoadMore} className="load-more-button">
                Load More
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Transactions;
