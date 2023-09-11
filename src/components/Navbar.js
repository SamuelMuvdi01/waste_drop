import { NavLink } from "react-router-dom";
import React, { useState } from "react";
import '../css/NavBar.css'



const Navbar =()=>{
    const [click, setClick] = useState(false);

    const handleClick = () => setClick(!click);

    return(
        <nav className ='navbar'>
        <div className='nav-container'>
        <NavLink exact to ='/' className= 'nav-logo'>
        </NavLink>
        
        <ul className ={click ? "navbar-menu active" : "navbar-menu"}>
            <li className='navbar-item'>
            <NavLink exact to ='/Home' activeClassName = 'active' className= 'navbar-links' onClick={handleClick}>
            Home
            </NavLink>
            </li>

            <li className='navbar-item'>
            <NavLink exact to ='/Login' activeClassName = 'active' className= 'navbar-links' onClick={handleClick}>
            Login
            </NavLink>
            </li>

            <li className='navbar-item'>
            <NavLink exact to ='/SignUp' activeClassName = 'active' className= 'navbar-links' onClick={handleClick}>
            SignUp
            </NavLink>
            </li>

            <li className='navbar-item'>
            <NavLink exact to ='/About' activeClassName = 'active' className= 'navbar-links' onClick={handleClick}>
            About
            </NavLink>
            </li>


        </ul>

        <div className="nav-icon" onClick={handleClick}>
        <i className ={click ? "fas fa-times" : "fa-solid fa-bars-staggered"}></i>
        </div>

        </div>
        </nav>
    )
}
export default Navbar;
