import React, { useState, useEffect } from 'react';
import './css/Transactions.css';

const Transactions = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    // Fetch current holdings data from the API
    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/transactions', {
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
            {transactions.length > 0 ? (
              transactions.map((transaction, index) => (
                <tr key={index}>
                  <td>{transaction.ticker}</td>
                  <td>{transaction.txn_type}</td>
                  <td>{transaction.qty}</td>
                  <td>₹{transaction.price_rate.toFixed(2)}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="4">No transaction data available</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
    </div>
  );
};

export default Transactions;
