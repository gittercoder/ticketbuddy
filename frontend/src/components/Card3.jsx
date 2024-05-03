import React from "react";

function Card3(){
    return(
        <div class="login-container">
        <h2>Sign Up</h2>
        <h3>An O.T.P. has been sent to your phone number/email address.</h3>
        <form action="#" method="post">
        <input type="text" class="input-field" placeholder="Enter One Time Password" name="username" required></input>
        <div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY"></div>
        <button type="submit" class="login-button">Finish</button>
        </form>
        </div>
    )
}

export default Card3;