import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import { StockProvider } from './StockContext';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <StockProvider>
      <App />
    </StockProvider>
  </React.StrictMode>,
  document.getElementById('root')
);
