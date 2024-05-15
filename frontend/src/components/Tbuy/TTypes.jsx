import React from "react";
import { totalPrice } from "./view1";

let a = false;

function TTypes(props) {
  const handleClick = () => {
    a = !a;
  };

  return (
    <div class="ticktype">
      <p>TOTAL</p>
      <p>{props.totalPrice}</p>
      <button onCick={handleClick}>Buy Ticket</button>
    </div>
  );
}

export default TTypes;
export { a };
