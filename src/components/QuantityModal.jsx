import React, { useState } from 'react';
import './css/QuantityModal.css'; // Add your own styling

const QuantityModal = ({ stock, onClose, onSubmit }) => {
  const [quantity, setQuantity] = useState(1);

  const handleIncrement = () => {
    setQuantity(prev => prev + 1);
  };

  const handleDecrement = () => {
    if (quantity > 1) {
      setQuantity(prev => prev - 1);
    }
  };

  const handleSubmit = () => {
    onSubmit(quantity);
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <h2>Add to Holdings</h2>
        <p>How many quantities do you want to add?</p>
        <div className="quantity-control">
          <button onClick={handleDecrement}>-</button>
          <span>{quantity}</span>
          <button onClick={handleIncrement}>+</button>
        </div>
        <button onClick={handleSubmit}>Add</button>
        <button onClick={onClose}>Cancel</button>
      </div>
    </div>
  );
};

export default QuantityModal;
