import React from "react";

let a = false;

function TTypes(props) {
  const handleClick = () => {
    a = !a;
  };

  return (
    <div class="ticktype">
      <p>Premium</p>
      <button onCick={handleClick}>Buy Ticket</button>
    </div>
  );
}

export default TTypes;
export { a };
