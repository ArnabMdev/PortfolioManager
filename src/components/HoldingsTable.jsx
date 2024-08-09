import React, { useState, useEffect } from 'react';
import './css/HoldingsTable.css';

const HoldingsTable = () => {
  const [currentHoldings, setCurrentHoldings] = useState([]);
  const [sellingQuantities, setSellingQuantities] = useState([]);
  const [previousHoldings, setPreviousHoldings] = useState([]);

  useEffect(() => {
    // Fetch current holdings data from the API
    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/current_holdings/', {
      method: 'GET',
      headers: new Headers({
        "ngrok-skip-browser-warning": "69420"
      })
    })
    .then(response => response.json())
    .then(data => {
      setCurrentHoldings(data);
      setSellingQuantities(new Array(data.length).fill(1));
    })
    .catch(error => console.error('Error fetching current holdings data:', error));

    // Fetch previous holdings data from the API
    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/previous_holdings/', {
      method: 'GET',
      headers: new Headers({
        "ngrok-skip-browser-warning": "69420"
      })
    })
    .then(response => response.json())
    .then(data => setPreviousHoldings(data))
    .catch(error => console.error('Error fetching previous holdings data:', error));
  }, []);

  const handleIncrement = (index) => {
    const currentQty = currentHoldings[index].qty;
    const newQuantities = [...sellingQuantities];
    if (newQuantities[index] < currentQty) {
      newQuantities[index] += 1;
      setSellingQuantities(newQuantities);
    }
  };

  const handleDecrement = (index) => {
    const newQuantities = [...sellingQuantities];
    if (newQuantities[index] > 1) {
      newQuantities[index] -= 1;
      setSellingQuantities(newQuantities);
    }
  };

  const handleSell = (index) => {
    const holding = currentHoldings[index];
    const sellingQty = sellingQuantities[index];
    const remainingQty = holding.qty - sellingQty;
    const sellingPrice = holding.avg_price * sellingQty;
    const profit = sellingPrice - holding.avg_price * sellingQty; // Calculate profit

    // Post to the transactions API
    fetch('https://c09d-13-233-161-181.ngrok-free.app/api/transactions', {
      method: 'POST',
      headers: {
        'Access-Control-Allow-Origin': '*',
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        ticker: holding.ticker,
        txn_type: 'sell',
        qty: sellingQty,
        price_rate: holding.avg_price,
      }),
    })
    .then(response => response.json())
    .then(data => {
      // Update previous holdings state with new data
      setPreviousHoldings(prevData => {
        const existingIndex = prevData.findIndex(p => p.ticker === holding.ticker);
        if (existingIndex !== -1) {
          const updatedData = [...prevData];
          updatedData[existingIndex] = {
            ...updatedData[existingIndex],
            qty: updatedData[existingIndex].qty + sellingQty,
            selling_price: updatedData[existingIndex].selling_price + sellingPrice,
            profit: updatedData[existingIndex].profit + profit,
          };
          return updatedData;
        } else {
          return [...prevData, {
            ticker: holding.ticker,
            selling_price: sellingPrice,
            profit: profit,
            qty: sellingQty,
          }];
        }
      });
    })
    .catch(error => console.error('Error posting to transactions API:', error));

    if (remainingQty > 0) {
      // Update the current holding with the remaining quantity
      const newHoldings = [...currentHoldings];
      newHoldings[index].qty = remainingQty;
      setCurrentHoldings(newHoldings);
    } else {
      // Remove the holding if all shares are sold
      const newHoldings = currentHoldings.filter((_, i) => i !== index);
      setCurrentHoldings(newHoldings);
    }

    // Reset selling quantity
    const newSellingQuantities = [...sellingQuantities];
    newSellingQuantities[index] = 1;
    setSellingQuantities(newSellingQuantities);
  };

  return (
    <div className="holdings-container">
      <div className="content">
    <div className="table-container">
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <h2>Holdings</h2>
      </div>
      <table className="holdings-table">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Current Price</th>
            <th>Asset Type</th>
            <th>Quantity</th>
            <th>Average Price</th>
            <th>Selling Quantity</th>
            <th>Sell</th>
          </tr>
        </thead>
        <tbody>
          {currentHoldings.length > 0 ? (
            currentHoldings.map((holding, index) => (
              <tr key={index}>
                <td>{holding.ticker}</td>
                <td>₹{holding.current_price.toFixed(2)}</td>
                <td>{holding.asset_type}</td>
                <td>{holding.qty}</td>
                <td>₹{holding.avg_price.toFixed(2)}</td>
                <td>
                  <div className="quantity-control">
                    <button onClick={() => handleDecrement(index)}>-</button>
                    <span>{sellingQuantities[index]}</span>
                    <button onClick={() => handleIncrement(index)}>+</button>
                  </div>
                </td>
                <td>
                  <button className="sell-button" onClick={() => handleSell(index)}>
                    Sell
                  </button>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="7">No holdings data available</td>
            </tr>
          )}
        </tbody>
      </table>

      <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
        <h2>Previous Holdings</h2>
      </div>
      <table className="holdings-table">
        <thead>
          <tr>
            <th>Ticker</th>
            <th>Quantity</th>
            <th>Selling Price</th>
            <th>Profit / Loss</th>
          </tr>
        </thead>
        <tbody>
          {previousHoldings.length > 0 ? (
            previousHoldings.map((holding, index) => (
              <tr key={index}>
                <td>{holding.ticker}</td>
                <td>{holding.qty}</td>
                <td>₹{holding.avg_sell_price.toFixed(2)}</td>
                <td
                  style={{
                    color: (holding.avg_sell_price - holding.avg_buy_price) < 0 ? 'red' : 'green',
                  }}
                >
                  ₹{(holding.avg_sell_price - holding.avg_buy_price).toFixed(2)}
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="4">No previous holdings data available</td>
            </tr>
          )}
        </tbody>
      </table>
    </div>
    </div>
    </div>
  );
};

export default HoldingsTable;
