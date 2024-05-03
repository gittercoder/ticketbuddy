import React from "react";

function PaymentOptions() {
  return (
    <div>
      <input type="radio" name="payment" value="UPI" id="upi" />
      <label htmlFor="upi">UPI</label>
      <br />
      <input type="radio" name="payment" value="Card" id="card" />
      <label htmlFor="card">Card</label>
      <br />
      <input
        type="radio"
        name="payment"
        value="Online Transaction"
        id="online"
      />
      <label htmlFor="online">Online Transaction</label>
    </div>
  );
}

export default PaymentOptions;
