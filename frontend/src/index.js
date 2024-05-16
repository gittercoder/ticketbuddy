import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./index.css";
import App from "./App";
import Home from "./components/Home/home";
import Login from "./components/Login/login";
import Signup from "./components/Signup/signup";
import Tbuy from "./components/Tbuy/tbuy";
import ViewTickets from "./components/ViewTickets/view_tickets";
import ViewCompensations from "./components/ViewCompensations/view_compensations";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <Router>
    <Routes>
      <Route path="/" element={<Login />} />
      <Route path="/home" element={<Home />} />
      <Route path="/signup" element={<Signup />} />
      <Route path="/tbuy" element={<Tbuy />} />
      <Route path="/view_tickets" element={<ViewTickets />} />
      <Route path="/view_compensations" element={<ViewCompensations />} />
    </Routes>
  </Router>
);
