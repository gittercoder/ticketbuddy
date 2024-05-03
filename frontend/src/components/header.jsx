import React from "react";

function Header(){
    return(
        <div>
            <header>
                <h1>TicketBuddy</h1>
                <form action="#">
                <input type="text" id="search" placeholder="Search for events"></input>
                <button type="submit">Find Tickets</button>
                </form>
            </header>
        </div>
    )
}

export default Header;