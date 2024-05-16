import React, { useState } from "react";
import axios from "axios";

function Card3({ onNextClick }) {
  const username = localStorage.getItem("username");
  const email = localStorage.getItem("email");
  const [otp, setOTP] = useState("");
  const handleNextClick = async (event) => {
    event.preventDefault();
    try {
      // Send POST request to backend API
      const response = await axios.post("http://localhost:5000/signup", {
        username,
        email,
        otp,
      });
      onNextClick();
    } catch (error) {
      console.error("Error:", error);
    }
  };
  return (
    <div class="login-container">
      <h2>Sign Up</h2>
      <h3>An O.T.P. has been sent to your phone number/email address.</h3>
      <form onSubmit={handleNextClick}>
        <input
          type="text"
          className="input-field"
          placeholder="Name"
          name="Enter One Time Password"
          value={otp}
          onChange={(e) => setOTP(e.target.value)}
          required
        />
        <button type="submit" class="login-button">
          Finish
        </button>
      </form>
    </div>
  );
}

export default Card3;
