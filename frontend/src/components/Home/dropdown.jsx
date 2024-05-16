import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function DropdownMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div className="dropdown">
      <button onClick={toggleMenu} className="dropdown-toggle">
        ≡
      </button>
      {isOpen && (
        <div className="dropdown-menu">
          <a href="/view_tickets">View Tickets</a>
          <a href="/">Logout</a>
        </div>
      )}
    </div>
  );
}

export default DropdownMenu;
