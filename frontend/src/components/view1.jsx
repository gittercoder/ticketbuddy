import React from "react";
import tickettypes from "../data";
import TTypes from "./TTypes";

function View1() {
  return (
    <div>
      <div class="venue">
        <img src="https://www.rateyourseats.com/seatingcharts/events/jennifer-lopez-ubs-arena-seating-chart-august-9-2024-4823188.jpg" />
      </div>
      <div>{tickettypes.map(TTypes)}</div>
    </div>
  );
}

export default View1;
