import React, { useState, useEffect } from "react";
import axios from "axios";

function YourTickets() {
  const [tickets, setTickets] = useState([]);

  useEffect(() => {
    // Get user ID from local storage
    const u_id = localStorage.getItem("u_id");

    // Fetch tickets using Axios
    axios
      .get(`http://localhost:5000/gte?u_id=${u_id}`)
      .then((response) => {
        setTickets(response.data);
      })
      .catch((error) => {
        console.error("Error fetching tickets:", error);
      });
  }, []); // Empty dependency array ensures useEffect only runs once

  const handleCancelTicket = (ticketId) => {
    axios
      .post("http://localhost:5000/cancel_ticket", { t_id: ticketId })
      .then((response) => {
        console.log(response.data); // Log success message
        window.location.reload();
      })
      .catch((error) => {
        console.error("Error canceling ticket:", error);
      });
  };

  return (
    <div className="your_tickets">
      {tickets.map((ticket) => (
        <div key={ticket.t_id} className="ticket_info">
          <p>{ticket.event_name}</p>{" "}
          {/* Assuming event name is available in the ticket object */}
          <p>{ticket.event_date}</p>{" "}
          {/* Assuming event date is available in the ticket object */}
          <p>{ticket.t_id}</p>
          <div className="buttons">
            <button onClick={() => handleCancelTicket(ticket.t_id)}>
              Cancel
            </button>
          </div>
        </div>
      ))}
    </div>
  );
}

export default YourTickets;
