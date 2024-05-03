import React, { useEffect } from "react";
import Header from "./header";
import Banner from "./banner";
import Footer from "./footer";
import View1 from "./view1";
import View2 from "./view2";
import { bidlist } from "../data";
import TTypes, { a } from "./TTypes";

function Tbuy() {
  useEffect(() => {
    // Dynamically import the CSS file when the component is mounted
    const removeStyles = import("./tbuystyles.css");

    // Cleanup function to remove styles when component is unmounted
    return () => {
      removeStyles.then((module) => module.default && module.default.remove());
    };
  }, []);

  return (
    <div>
      <Header />
      <Banner
        name="Kanye West"
        genre="Rap"
        img="https://images-cdn.ubuy.co.in/6523b2cba482e55f3222f1f6-ubuy-online-shopping.jpg"
        date="20-05-2025"
      />

      {a ? <View2 position={bidlist[0].position} /> : <View1 />}

      {/*<Footer year={new Date().getFullYear()} />*/}
    </div>
  );
}

export default Tbuy;
