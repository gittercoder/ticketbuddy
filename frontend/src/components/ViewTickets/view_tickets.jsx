import React, { useEffect } from "react";
import Header from "../headert";
import YourTickets from "./your_tickets";

let x = new Date().getDate();

function ViewTickets() {
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
      <h1>YOUR TICKETS</h1>
      <YourTickets />
    </div>
  );
}

export default ViewTickets;
