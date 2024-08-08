import React, { useContext } from 'react';
import { StockContext } from '../StockContext';
import './css/HoldingsTable.css';

const HoldingsTable = () => {
  const { holdings } = useContext(StockContext);

  return (
    <div className="table-container">
      <h2>Stock Holdings</h2>
      <table className="holdings-table">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Stock Name</th>
            <th>User ID</th>
            <th>Asset Type</th>
            <th>Quantity</th>
            <th>Average Price</th>
          </tr>
        </thead>
        <tbody>
          {holdings.map((holding, index) => (
            <tr key={index}>
              <td>{holding.ticker}</td>
              <td>{holding.stock_name}</td>
              <td>{holding.user_id}</td>
              <td>{holding.asset_type}</td>
              <td>{holding.qty}</td>
              <td>${holding.avg_price.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default HoldingsTable;
