import React, { useState, useEffect } from "react";
import axios from "axios";
import tickettypes from "../../data";
import TTypes from "./TTypes";

function View1() {
  const [tickets, setTickets] = useState([]);
  const [selectedSeats, setSelectedSeats] = useState([]);

  useEffect(() => {
    // Fetch tickets based on e_id from backend
    axios
      .get(`http://localhost:5000/api/tickets?e_id=${1}`)
      .then((response) => {
        setTickets(response.data);
      })
      .catch((error) => {
        console.error("Error fetching tickets:", error);
      });
  }, []);

  // Function to determine the number of seats
  const calculateNumSeats = () => {
    if (tickets.length === 0) return 0;
    const lowestTId = Math.min(...tickets.map((ticket) => ticket.t_id));
    const highestTId = Math.max(...tickets.map((ticket) => ticket.t_id));
    return highestTId - lowestTId + 1;
  };

  // Helper function to check if a seat is selectable based on ticket data
  const isSeatSelectable = (seatId) => {
    const ticket = tickets.find((ticket) => ticket.t_id === seatId);
    return ticket ? !ticket.f_owner : true;
  };

  // Function to handle seat selection
  const handleSeatSelection = (seatId) => {
    setSelectedSeats((prevSelectedSeats) => {
      if (prevSelectedSeats.includes(seatId)) {
        return prevSelectedSeats.filter((id) => id !== seatId);
      } else {
        return [...prevSelectedSeats, seatId];
      }
    });
  };

  // Render the seats
  const renderSeats = () => {
    const numSeats = calculateNumSeats();
    const seats = [];
    for (let i = 1; i <= numSeats; i++) {
      const isSelectable = isSeatSelectable(i);
      const isSelected = selectedSeats.includes(i);
      const isPremium = tickets.some(
        (ticket) => ticket.t_id === i && ticket.category === "Premium"
      );
      const isBooked = tickets.some(
        (ticket) => ticket.t_id === i && ticket.f_owner
      );
      seats.push(
        <div
          key={i}
          className={`seat ${isSelectable ? "selectable" : ""} ${
            isSelected ? "selected" : ""
          } ${isPremium ? "premium" : ""} ${isBooked ? "booked" : ""}`}
          onClick={() => isSelectable && handleSeatSelection(i)}
        >
          {i}
        </div>
      );
    }
    return seats;
  };

  return (
    <div>
      <div className="venue">
        {/* Seat container */}
        <div className="seat-container">
          {/* Render seats */}
          {renderSeats()}
          <h2 className="stage">Stage</h2>
        </div>
      </div>
      <div>{tickettypes.map(TTypes)}</div>
    </div>
  );
}

export default View1;
