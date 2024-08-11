import React, { useState, useEffect } from 'react';
import './css/Transactions.css';

const Transactions = () => {
  const [transactions, setTransactions] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const rowsPerPage = 7;

  useEffect(() => {
    // Fetch current holdings data from the API
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

  // Calculate the transactions to display on the current page
  const indexOfLastTransaction = currentPage * rowsPerPage;
  const indexOfFirstTransaction = indexOfLastTransaction - rowsPerPage;
  const currentTransactions = transactions.slice(indexOfFirstTransaction, indexOfLastTransaction);

  // Change page
  const paginate = (pageNumber) => setCurrentPage(pageNumber);

  // Calculate total pages
  const totalPages = Math.ceil(transactions.length / rowsPerPage);

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
              {currentTransactions.length > 0 ? (
                currentTransactions.map((transaction, index) => (
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
          <div className="pagination">
            {Array.from({ length: totalPages }, (_, index) => (
              <button
                key={index + 1}
                onClick={() => paginate(index + 1)}
                className={currentPage === index + 1 ? 'active' : ''}
              >
                {index + 1}
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Transactions;
