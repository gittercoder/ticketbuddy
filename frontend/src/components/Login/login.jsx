import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [showError, setShowError] = useState(false);
  const navigate = useNavigate(); // Get the navigate function for navigation

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_name: username, password: password }),
      });

      const data = await response.json();

      if (response.ok) {
        // Login successful, redirect to home page
        localStorage.setItem("username", username);
        navigate("/home");
      } else {
        // Login failed, display error message
        console.error(data.message);
        setShowError(true);
      }
    } catch (error) {
      console.error("Error:", error);
    }
  };
  const [passwordVisible, setPasswordVisible] = useState(false);

  const togglePasswordVisibility = () => {
    setPasswordVisible(!passwordVisible);
  };

  return (
    <div className="login-container">
      <h2>Sign In</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          className="input-field"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type={passwordVisible ? "text" : "password"}
          className="input-field"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <div className="eye password-toggle" onClick={togglePasswordVisibility}>
          👁
        </div>
        {showError && (
          <p style={{ color: "red" }}>Wrong Password or Username!</p>
        )}
        <button type="submit" className="login-button">
          Login
        </button>
      </form>
      <Link to="/signup" className="signup-link">
        New user? Sign up.
      </Link>
    </div>
  );
}

export default Login;
