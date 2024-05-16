import React from "react";
import TicketInfo from "./ticket_info";
import your_tickets from "./mytickets";

function YourTickets() {
  return <div class="your_tickets">{your_tickets.map(TicketInfo)}</div>;
}

export default YourTickets;
