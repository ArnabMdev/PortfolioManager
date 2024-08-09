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
  const [stockNews, setStockNews] = useState({});
  const [loadingNews, setLoadingNews] = useState(false);
  const [newsError, setNewsError] = useState('');

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

  useEffect(() => {
    // Fetch all news data
    setLoadingNews(true);
    setNewsError('');
    
    fetch('https://7147-3-110-131-210.ngrok-free.app/api/stock_news', {
      method: 'GET',
      headers: new Headers({
        'Access-Control-Allow-Origin': '*',
        "ngrok-skip-browser-warning": "69420"
      })
    })
    .then(response => response.json())
    .then(data => {
      setStockNews(data);
      setLoadingNews(false);
    })
    .catch(error => {
      console.error('Error fetching news:', error);
      setLoadingNews(false);
      setNewsError('Failed to load news');
    });
  }, []);

  const handleAddToHoldings = useCallback((stock) => {
    setSelectedStock(stock);
    setModalVisible(true);
  }, []);

  const handleModalSubmit = useCallback((quantity) => {
    const transactionData = {
      ticker: selectedStock.ticker,
      txn_type: 'buy',
      qty: quantity,
      price_rate: selectedStock.avg_price,
    };

    fetch('https://7147-3-110-131-210.ngrok-free.app/api/transactions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(transactionData),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        setResponseMessage('Transaction successful!');
        setResponseType('success');
      } else {
        setResponseMessage('Transaction failed. Please try again.');
        setResponseType('error');
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
        <div className="table-news-container">
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

          <div className="news-cards">
            {loadingNews ? (
              <p>Loading news...</p>
            ) : newsError ? (
              <p>{newsError}</p>
            ) : Object.keys(stockNews).length > 0 ? (
              Object.keys(stockNews).map(ticker => (
                <div key={ticker} className="news-section">
                  <h2>News for {ticker}</h2>
                  {stockNews[ticker].map((item, index) => (
                    <div key={index} className="news-card">
                      <h3>{item.title}</h3>
                      <p>{item.content}</p>
                      <a href={item.url} target="_blank" rel="noopener noreferrer">Read more</a>
                    </div>
                  ))}
                </div>
              ))
            ) : (
              <p>No news available</p>
            )}
          </div>
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
