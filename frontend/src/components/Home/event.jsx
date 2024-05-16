import React from "react";

function Event(props) {
  const handleGetTicketsClick = (e_id) => {
    localStorage.setItem("selectedEventId", e_id);
    console.log(e_id);
  };

  return (
    <div class="event-card">
      <img src={props.img} />
      <h3>{props.Name}</h3>
      <p>{props.Genre}</p>
      <a href="/tbuy" onClick={() => handleGetTicketsClick(props.e_id)}>
        Get Tickets
      </a>
    </div>
  );
}

export default Event;
