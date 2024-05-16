import React, { useState, useEffect } from "react";
import axios from "axios";
import tickettypes from "../../data";
import TTypes from "./TTypes";

let price;
let normc;
let premc;

function View1() {
  const [tickets, setTickets] = useState([]);
  const [selectedSeats, setSelectedSeats] = useState([]);
  const [totalPrice, setTotalPrice] = useState(0);

  const selectedEventId = localStorage.getItem("selectedEventId");
  useEffect(() => {
    // Fetch tickets based on e_id from backend
    axios
      .get(`http://localhost:5000/api/tickets?e_id=${selectedEventId}`)
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

  // Function to determine total price
  function computeTotalPrice() {
    let totalPrice = 0;
    for (const seatId of selectedSeats) {
      // Find the ticket with the corresponding t_id (assuming t_id is the seat ID)
      const ticket = tickets.find((ticket) => ticket.t_id === seatId);
      if (ticket) {
        // If ticket is found, add its price to totalPrice
        totalPrice += ticket.price;
      }
    }
    return totalPrice;
  }
  // Update total price whenever selectedSeats change
  useEffect(() => {
    const newTotalPrice = computeTotalPrice();
    setTotalPrice(newTotalPrice);
  }, [selectedSeats]);

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
          } ${isPremium ? "premium" : ""} ${
            isPremium && isSelected ? "premium selected" : ""
          }  ${isBooked ? "booked" : ""}`}
          onClick={() => isSelectable && handleSeatSelection(i)}
        >
          {i}
          {console.log("Total price:", totalPrice)}
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
        </div>
        <h2 className="stage">Stage</h2>
      </div>
      <div>{<TTypes totalPrice={totalPrice} />}</div>
    </div>
  );
}

export default View1;
