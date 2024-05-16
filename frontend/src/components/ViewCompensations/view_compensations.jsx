import React, { useEffect } from "react";
import Header from "../headert";
import YourCompensations from "./your_compensations";

let x = new Date().getDate();

function ViewCompensations() {
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
      <h1>YOUR COMPENSATIONS</h1>
      <YourCompensations />
    </div>
  );
}

export default ViewCompensations;
