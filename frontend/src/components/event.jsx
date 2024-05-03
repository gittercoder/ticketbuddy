import React from "react";

function Event(props) {
  return (
    <div class="event-card">
      <img src={props.img} />
      <h3>{props.Name}</h3>
      <p>{props.Genre}</p>
      <a href="/tbuy">Get Tickets</a>
    </div>
  );
}

export default Event;
