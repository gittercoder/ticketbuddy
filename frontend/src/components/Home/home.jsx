import React, { useState, useEffect } from "react";
import "./home.css";
import Header from "../header";
import Event from "./event";
import Footer from "../footer";

const Home = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    // Fetch events from backend when component mounts
    fetch("http://localhost:5000/api/events")
      .then((response) => response.json())
      .then((data) => setEvents(data))
      .catch((error) => console.error("Error fetching events:", error));
  }, []);
  useEffect(() => {
    // Add 'home' class to body when component mounts
    document.body.classList.add("home");

    return () => {
      // Remove 'home' class from body when component unmounts
      document.body.classList.remove("home");
    };
  }, []);

  return (
    <div>
      <Header />
      <section className="featured-events">
        <h2>Featured Events</h2>
        {events.map((event) => (
          <Event
            key={event.e_id}
            e_id={event.e_id}
            img={event.image_link}
            Name={event.name}
            Genre={event.genre}
          />
        ))}
      </section>
    </div>
  );
};

export default Home;
