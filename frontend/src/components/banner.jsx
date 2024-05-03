import React from "react";

function Banner(props) {
  return (
    <div>
      <h2>{props.name}</h2>
      <h3>{props.genre}</h3>
      <h3 id="date">{props.date}</h3>
      <img class="banner-img" src={props.img} />
    </div>
  );
}

export default Banner;
