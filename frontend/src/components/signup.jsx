import React, { useState } from "react";
import ReactDOM from "react-dom";
import Card from "./Card";
import Card2 from "./Card2";
import Card3 from "./Card3";

function Signup() {
  const [showCard2, setShowCard2] = useState(false);
  const [showCard3, setShowCard3] = useState(false);

  const handleNextClick = () => {
    if (showCard2) {
      setShowCard3(true);
    } else {
      setShowCard2(true);
    }
  };

  return (
    <div className="centered-card">
      {showCard3 ? (
        <Card3 />
      ) : showCard2 ? (
        <Card2 onNextClick={handleNextClick} />
      ) : (
        <Card onButtonClick={handleNextClick} />
      )}
    </div>
  );
}

export default Signup;
