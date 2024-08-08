import React, { createContext, useState } from 'react';

// Create a context
export const StockContext = createContext();

// Create a provider component
export const StockProvider = ({ children }) => {
  const [holdings, setHoldings] = useState([
    {
      ticker: 'AAPL',
      stock_name: 'Apple Inc.',
      user_id: '001',
      asset_type: 'Equity',
      qty: 50,
      avg_price: 150.00,
    },
    {
      ticker: 'GOOGL',
      stock_name: 'Alphabet Inc.',
      user_id: '002',
      asset_type: 'Equity',
      qty: 30,
      avg_price: 2800.50,
    },
    {
      ticker: 'TSLA',
      stock_name: 'Tesla Inc.',
      user_id: '003',
      asset_type: 'Equity',
      qty: 20,
      avg_price: 720.75,
    },
  ]);

  const [watchlist, setWatchlist] = useState([
    { ticker: 'NFLX', avg_price: 510.00 },
    { ticker: 'AMZN', avg_price: 3200.50 },
    { ticker: 'MSFT', avg_price: 285.70 },
  ]);

  return (
    <StockContext.Provider value={{ holdings, setHoldings, watchlist, setWatchlist }}>
      {children}
    </StockContext.Provider>
  );
};
