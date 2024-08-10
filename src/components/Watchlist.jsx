import React, { useState, useEffect, useCallback } from 'react';
import './css/Watchlist.css';
import QuantityModal from './QuantityModal';
import ResponseModal from './ResponseModal';

const Watchlist = () => {
  const [watchlist, setWatchlist] = useState([]);
  const [selectedStock, setSelectedStock] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);
  const [responseModalVisible, setResponseModalVisible] = useState(false);
  const [responseMessage, setResponseMessage] = useState('');
  const [responseType, setResponseType] = useState('success');

  useEffect(() => {
    // Fetch watchlist data
    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/watchlist', {
      method: 'GET',
      headers: new Headers({
        "ngrok-skip-browser-warning": "69420"
      })
    })
    .then(response => response.json())
    .then(data => {
      const formattedWatchlist = Object.keys(data).map(ticker => ({
        ticker,
        avg_price: data[ticker].close[0]
      }));
      setWatchlist(formattedWatchlist);
    })
    .catch(error => console.error('Error fetching watchlist data:', error));
  }, []);

  const handleAddToHoldings = useCallback((stock) => {
    setSelectedStock(stock);
    setModalVisible(true);
  }, []);

  const handleModalSubmit = useCallback((quantity) => {

    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/transactions', {
      method: 'POST',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ticker: selectedStock.ticker,
      txn_type: 'buy',
      qty: quantity,
      price_rate: selectedStock.avg_price,
      }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        setResponseMessage('Transaction successful!');
        setResponseType('success');
      } 
      setResponseModalVisible(true);
      setModalVisible(false);
    })
    .catch(error => {
      console.error('Error posting transaction:', error);
      setResponseMessage('Transaction failed. Please try again.');
      setResponseType('error');
      setResponseModalVisible(true);
      setModalVisible(false);
    });
  }, [selectedStock]);

  const handleResponseModalClose = useCallback(() => {
    setResponseModalVisible(false);
  }, []);

  return (
    <div className="watchlist-container">
      <div className="content">
        <div className="table-container">
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
            <h2>Watchlist</h2>
          </div>
          <table className="watchlist-table">
            <thead>
              <tr>
                <th>Ticker</th>
                <th>Current Price</th>
                <th>Add to Holdings</th>
              </tr>
            </thead>
            <tbody>
              {watchlist.length > 0 ? (
                watchlist.map((stock, index) => (
                  <tr key={index}>
                    <td>{stock.ticker}</td>
                    <td>₹{stock.avg_price.toFixed(2)}</td>
                    <td>
                      <button onClick={() => handleAddToHoldings(stock)}>
                        Add to Holdings
                      </button>
                    </td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="3">No watchlist data available</td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {modalVisible && (
        <QuantityModal 
          stock={selectedStock} 
          onClose={() => setModalVisible(false)} 
          onSubmit={handleModalSubmit} 
        />
      )}

      {responseModalVisible && (
        <ResponseModal 
          message={responseMessage} 
          type={responseType} 
          onClose={handleResponseModalClose} 
        />
      )}
    </div>
  );
};

export default Watchlist;
