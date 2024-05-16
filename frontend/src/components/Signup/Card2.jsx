import React, { useState } from "react";
import axios from "axios";

function Card2({ onNextClick }) {
  const username = localStorage.getItem("username");
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [email, setEmail] = useState("");
  const [verification, setVerification] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");

  const handleNextClick = async (event) => {
    event.preventDefault();
    try {
      // Send POST request to backend API
      const response = await axios.post("http://localhost:5000/signup", {
        username,
        name,
        phone,
        email,
        age,
        gender,
      });
      localStorage.setItem("email", email);
      onNextClick();
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="login-container">
      <h2>Tell us more about yourself!</h2>
      <form onSubmit={handleNextClick}>
        <input
          type="text"
          className="input-field"
          placeholder="Name"
          name="username"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />
        <input
          type="text"
          className="input-field"
          placeholder="Phone"
          name="phone"
          value={phone}
          onChange={(e) => setPhone(e.target.value)}
        />
        <input
          type="email"
          className="input-field"
          placeholder="Email Address"
          name="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <div className="verification-container">
          <div className="verification-radio">
            <input
              type="radio"
              id="phone-verification"
              name="verification"
              value="phone"
              checked={verification === "phone"}
              onChange={() => setVerification("phone")}
            />
            <label htmlFor="phone-verification">Phone Verification</label>
          </div>
          <div className="verification-radio">
            <input
              type="radio"
              id="email-verification"
              name="verification"
              value="email"
              checked={verification === "email"}
              onChange={() => setVerification("email")}
            />
            <label htmlFor="email-verification">Email Verification</label>
          </div>
        </div>
        <br></br>
        <label htmlFor="age">Age:</label>
        <input
          type="date"
          id="age"
          name="age"
          value={age}
          onChange={(e) => setAge(e.target.value)}
          required
        />
        <label htmlFor="gender">Gender:</label>
        <select
          name="gender"
          id="gender"
          value={gender}
          onChange={(e) => setGender(e.target.value)}
          required
        >
          <option value="">Select Gender</option>
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="non-binary">Non-Binary</option>
        </select>
        <br></br>
        <br></br>
        <button type="submit" className="login-button">
          Next
        </button>
      </form>
      <a href="/home" className="home">
        Not interested? Skip
      </a>
    </div>
  );
}

export default Card2;
