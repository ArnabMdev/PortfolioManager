import React, { useState, useCallback } from 'react';
import './css/Watchlist.css';
import QuantityModal from './QuantityModal';
import ResponseModal from './ResponseModal';

const Watchlist = () => {
  const [watchlist] = useState([
    { ticker: 'ONGC.NS', avg_price: 150.75 },
    { ticker: 'TATAMOTORS.NS', avg_price: 430.60 },
    { ticker: 'ZOMATO.NS', avg_price: 82.15 }
  ]);
  const [selectedStock, setSelectedStock] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);
  const [responseModalVisible, setResponseModalVisible] = useState(false);
  const [responseMessage, setResponseMessage] = useState('');
  const [responseType, setResponseType] = useState('success');

  const stockNews = {
    "ONGC.NS": [
      {
        title: "ONGC Reports Record Profits in Q1",
        content: "Oil and Natural Gas Corporation (ONGC) has reported record profits for Q1, driven by higher oil prices and increased production.",
        url: "https://finance.yahoo.com/m/216f352c-fe72-34b7-a6a3-458185787a28/the-x-exodus-that-wasn%27t.html"
      },
      {
        title: "ONGC Expands Offshore Drilling Operations",
        content: "ONGC has announced a significant expansion in its offshore drilling operations, aiming to boost production by 20% over the next year.",
        url: "https://finance.yahoo.com/news/top-cd-rates-today-august-183000260.html"
      }
    ],
    "TATAMOTORS.NS": [
      {
        title: "Tata Motors Unveils New Electric Vehicle",
        content: "Tata Motors has unveiled its latest electric vehicle, which promises a range of over 500 km on a single charge.",
        url: "https://finance.yahoo.com/m/216f352c-fe72-34b7-a6a3-458185787a28/the-x-exodus-that-wasn%27t.html"
      },
      {
        title: "Tata Motors Sees Surge in Sales",
        content: "Tata Motors has reported a significant surge in sales, driven by strong demand for its SUVs and commercial vehicles.",
        url: "https://finance.yahoo.com/news/top-cd-rates-today-august-183000260.html"
      }
    ],
    "ZOMATO.NS": [
      {
        title: "Zomato Expands into Grocery Delivery",
        content: "Zomato has announced its expansion into grocery delivery, aiming to compete with other major players in the market.",
        url: "https://finance.yahoo.com/m/216f352c-fe72-34b7-a6a3-458185787a28/the-x-exodus-that-wasn%27t.html"
      },
      {
        title: "Zomato Reports Growth in Revenue",
        content: "Zomato has reported a strong growth in revenue for the last quarter, driven by an increase in online food orders.",
        url: "https://finance.yahoo.com/news/top-cd-rates-today-august-183000260.html"
      }
    ]
  };

  const handleAddToHoldings = useCallback((stock) => {
    setSelectedStock(stock);
    setModalVisible(true);
  }, []);

  const handleModalSubmit = useCallback((quantity) => {
    fetch('https://7d17-13-233-233-6.ngrok-free.app/api/transactions', {
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
      <div className="content" style={{ display: 'flex', justifyContent: 'space-between' }}>
        <div className="table-container" style={{ flex: '1', marginRight: '20px' }}>
          <h2 style={{ display: 'flex', justifyContent: 'left', alignItems: 'center', marginLeft: 170 }}>
            Watchlist
          </h2>
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
        <div className="news-cards-container">
          <h2>Latest News</h2>
          {watchlist.map((stock, index) => (
            <div key={index} className="news-card">
              <h3>{stock.ticker} News</h3>
              {stockNews[stock.ticker] ? stockNews[stock.ticker].map((news, idx) => (
                <div key={idx}>
                  <h4>{news.title}</h4>
                  <p>{news.content}</p>
                  <a href={news.url} target="_blank" rel="noopener noreferrer">Read more</a>
                </div>
              )) : <p>No news available for {stock.ticker}</p>}
            </div>
          ))}
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
