import React from "react";
import PaymentOptions from "./payment";

const cells = Array.from({ length: 100 }, (_, index) => (
  <div key={index} className="bidlist-cell"></div>
));

let bidend = true;

function View2(props) {
  return (
    <div class="bottom_view2">
      <div class="bid">
        <div class="bidlist">{cells}</div>
        <p>You are at position #{props.position}</p>
      </div>

      <div class="buy">
        {bidend ? (
          <div>
            <h1>{props.bid}</h1>
            <h1>BUY TICKET</h1>
            <p>Choose your medium of payment.</p>
            <PaymentOptions />
          </div>
        ) : (
          <h1>
            Bidding period has not elapsed! Come back later or make a new bid.
          </h1>
        )}
      </div>
    </div>
  );
}

export default View2;
