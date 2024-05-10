import React, { useEffect } from "react";
import "./home.css";
import Header from "../header";
import events from "../../events";
import Event from "./event";
import Footer from "../footer";

const Home = () => {
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
      <section class="featured-events">
        <h2>Featured Events</h2>
        {events.map(Event)}
      </section>
      <Footer year={new Date().getFullYear()} />
    </div>
  );
};

export default Home;
