import React from 'react';
import Navbar from './Navbar';

function LogIn () {

    
    return (
        <div>
            <Navbar />
            <h1>Log In:</h1>
            <form>
                <input type = "text" placeholder = "Username" />
                <input type = "password" placeholder = "Password" />
                <button type = "submit" >Submit</button>
            </form>
        </div>
    )
}

export default LogIn;