import React, { useState } from "react";
import axios from "axios"; // Import Axios for making HTTP requests

function Card({ onButtonClick }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showError, setShowError] = useState(false);

  const handleNextClick = async (event) => {
    event.preventDefault(); // Prevent the form from submitting

    if (password !== confirmPassword) {
      setShowError(true);
    } else {
      try {
        // Send POST request to backend API
        const response = await axios.post("http://localhost:5000/signup", {
          username,
          password,
        });
        // If successful response
        localStorage.setItem("username", username);
        console.log(response.data); // Log the response
        setShowError(false);
        onButtonClick(); // Call the onButtonClick function passed from the parent
      } catch (error) {
        console.error("Error:", error); // Log any errors
      }
    }
  };

  return (
    <div className="login-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleNextClick}>
        <input
          type="text"
          className="input-field"
          placeholder="Username"
          name="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          className="input-field"
          placeholder="Password"
          name="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <input
          type="password"
          className="input-field"
          placeholder="Confirm Password"
          name="password-confirm"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
        />
        {showError && <p style={{ color: "red" }}>Passwords do not match!</p>}
        <button type="submit" className="login-button">
          Next
        </button>
      </form>
      <a href="/" className="signup-link">
        Already have an account? Sign in.
      </a>
    </div>
  );
}

export default Card;
