import React from 'react';
import './css/ResponseModal.css'; // Add your own styling

const ResponseModal = ({ message, type, onClose }) => {
  return (
    <div className="modal-overlay">
      <div className={`modal-content ${type}`}>
        <h2>{type === 'success' ? 'Success' : 'Error'}</h2>
        <p>{message}</p>
        <button onClick={onClose}>OK</button>
      </div>
    </div>
  );
};

export default ResponseModal;
