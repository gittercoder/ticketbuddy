import React from "react";

function TicketInfo(props) {
  return (
    <div class="ticket_info">
      <p>Playboi Carti</p>
      <p>{props.date}</p>
      <p>{props.ticketid}</p>
      <div class="buttons">
        <button>Cancel</button>
      </div>
    </div>
  );
}

export default TicketInfo;
