import React from "react";
import DropdownMenu from "./dropdown.jsx";

function Header() {
  return (
    <div>
      <header>
        <DropdownMenu />
        <h1>TicketBuddy</h1>
        <form action="#" class="pari">
          <input
            type="text"
            id="search"
            placeholder="Search for events"
          ></input>
          <button type="submit">Find Tickets</button>
        </form>
      </header>
    </div>
  );
}

export default Header;
