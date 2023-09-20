import React from 'react';
import { NavLink } from "react-router-dom";

function Navbar () {

    return (
        <nav>
            <div>
                <NavLink to = "/Home">Home</NavLink>
                <NavLink to = "/Login">Log in</NavLink>
                <NavLink to = "/SignUp">Sign Up</NavLink>
            </div>
        </nav>
    )
}

export default Navbar;