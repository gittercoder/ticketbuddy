import React, { useState, useEffect } from "react";
import "./home.css";
import DropdownMenu from "./dropdown.jsx";
import Event from "./event";
import Footer from "../footer";

const Home = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [events, setEvents] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch(
        `http://localhost:5000/api/event?search=${searchQuery}`
      );
      if (!response.ok) {
        throw new Error("Network response was not ok");
      }
      const eventData = await response.json();
      setEvents(eventData);
    } catch (error) {
      console.error("There was a problem with the fetch operation:", error);
    }
  };
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
      <div>
        <header>
          <DropdownMenu />
          <h1>TicketBuddy</h1>
          <form onSubmit={handleSearch} className="pari">
            <input
              type="text"
              id="search"
              placeholder="Search for events"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
            />
            <button type="submit">Find Tickets</button>
          </form>
        </header>
      </div>
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
