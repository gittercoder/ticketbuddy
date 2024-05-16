import React, { useState, useEffect } from "react";
import axios from "axios";

function Banner(props) {
  const [event, setEvent] = useState({});
  const selectedEventId = localStorage.getItem("selectedEventId");

  useEffect(() => {
    // Fetch event details based on e_id from backend
    axios
      .get(`http://localhost:5000/ee?e_id=${selectedEventId}`)
      .then((response) => {
        setEvent(response.data);
      })
      .catch((error) => {
        console.error("Error fetching event details:", error);
      });
  }, [selectedEventId]);
  return (
    <div>
      {/* Use the fetched event data */}
      <h2>{event.name}</h2>
      <h3>{event.genre}</h3>
      <h3 id="date">{event.date}</h3>
      <img className="banner-img" src={event.image_link} alt="Event" />
    </div>
  );
}

export default Banner;
