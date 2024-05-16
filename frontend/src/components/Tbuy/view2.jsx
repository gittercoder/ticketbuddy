import React, { useState, useEffect } from "react";
import axios from "axios";
import PaymentOptions from "./payment";

const cells = Array.from({ length: 100 }, (_, index) => (
  <div key={index} className="bidlist-cell"></div>
));

let bidend = true;

function View2(props) {
  const [auctionResults, setAuctionResults] = useState([]);
  const [bidamt, setBidamt] = useState("0");

  const selectedEventId = localStorage.getItem("selectedEventId");
  console.log(selectedEventId);
  useEffect(() => {
    // Fetch auction results based on e_id and category from backend
    axios
      .post("http://localhost:5000/auction_result", {
        e_id: selectedEventId,
      })
      .then((response) => {
        setAuctionResults(response.data);
        console.log(auctionResults);
      })
      .catch((error) => {
        console.error("Error fetching auction results:", error);
      });
  }, []);

  const handleBidConfirm = () => {
    // Store the value of the text field in bidamt variable
    const bidAmount = document.querySelector(".input-field").value;
    setBidamt(bidAmount);
    // You can perform any additional logic here
  };

  return (
    <div class="bottom_view2">
      <div>
        <div className="bid">
          <div className="bidlist">
            <div class="xyz">
              <p className="column">Position</p>
              <p className="column">Bid Amount</p>
              <p className="column">User ID</p>
            </div>
            {auctionResults.map((result, index) => (
              <div key={index} class="xyz">
                <p className="column">{index + 1}</p>
                <p className="column">{result.bid_amount}</p>
                <p className="column">{result.u_id}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div class="buy">
        {bidend ? (
          <div>
            <h1>{props.bid}</h1>
            <h1>MAKE BID</h1>
            <input
              type="text"
              className="input-field"
              placeholder="Bid Amount"
              required
            />
            <button onClick={handleBidConfirm}>Confirm</button>
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
