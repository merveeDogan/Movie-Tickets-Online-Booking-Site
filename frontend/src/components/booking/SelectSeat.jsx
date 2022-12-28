import React from "react";
import Seat from "./Seat";
import "./select-seat.css";
import {useNavigate } from "react-router-dom";
const SelectSeat = () => {
  const navigate = useNavigate();
  const toPaymentPage = () => {
    navigate("/film-details/film-name/book-ticket/payment");
  };
  const rows = [];
  const cols = [];
  const seats = [];
  for (let i = 1; i <= 7; i++) {
    rows.push(String.fromCharCode(65 + i - 1));
  }
  for (let i = 1; i <= 15; i++) {
    cols.push(i);
  }

  for (let i = 0; i < rows.length; i++) {
    for (let j = 0; j < cols.length; j++) {
      seats.push({ rowNum: rows[i], colNum: cols[j], state: "available" });
    }
  }

  return (
    <div>
      {" "}
      <div className="seats">
        {seats.map((seat) => (
          <Seat
            key={seat.rowNum + seat.colNum}
            rowNum={seat.rowNum}
            colNum={seat.colNum}
            state={seat.state}
          />
        ))}
      </div>
      <button type="button" className="btn btn-primary get-ticket " onClick={toPaymentPage}>
        Get Ticket
      </button>
    </div>
  );
};

export default SelectSeat;
