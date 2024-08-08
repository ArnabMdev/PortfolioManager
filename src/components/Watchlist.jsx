import React, { useContext } from 'react';
import { StockContext } from '../StockContext';
import './css/Watchlist.css';

const Watchlist = () => {
  const { holdings, setHoldings, watchlist, setWatchlist } = useContext(StockContext);

  const moveToHoldings = (stock) => {
    const newHolding = {
      ticker: stock.ticker,
      stock_name: 'Placeholder Name',
      user_id: '001',
      asset_type: 'Equity',
      qty: 10,
      avg_price: stock.avg_price,
    };

    setHoldings([...holdings, newHolding]);
    setWatchlist(watchlist.filter(item => item.ticker !== stock.ticker));
  };

  return (
    <div className="watchlist-container">
      <div className="watchlist-table-container">
        <h2>Watchlist</h2>
        <table className="watchlist-table">
          <thead>
            <tr>
              <th>Ticker</th>
              <th>Average Price</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody>
            {watchlist.map((stock, index) => (
              <tr key={index}>
                <td>{stock.ticker}</td>
                <td>${stock.avg_price.toFixed(2)}</td>
                <td>
                  <button onClick={() => moveToHoldings(stock)}>Move to Holdings</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="news-cards-container">
        <h2>Latest News</h2>
        {watchlist.map((stock, index) => (
          <div key={index} className="news-card">
            <h3>{stock.ticker} News</h3>
            <p>News content for {stock.ticker}...</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Watchlist;
