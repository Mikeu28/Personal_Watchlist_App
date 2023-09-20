import React from 'react';
import { useState } from 'react';
import Navbar from './Navbar';

function SignUp () {

    const [ form, setForm ] = useState( {} )

    function updateForm ( e ) {
        setForm(f => {
            return {...f, [ e.target.name ]: e.target.value }
        } )
    }

    function handleSubmit ( e ) {
        e.preventDefault()
        fetch( '/users', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify( form )
        } )
        .then( r => {
            if ( r.ok ) {
                r.json().then( console.log )
            } else {
                console.error( "Something went wrong" )
                console.error( 'POST /users status:', r.satus )
                r.text().then( console.warn )
            }
        } )
    }
    
    return (
        <div>
            <Navbar />
            <h1>Sign Up:</h1>
            <form onSubmit = { handleSubmit } >
                <input name = "name" type = "text" placeholder = "Username" onChange = { updateForm } />
                <input name = "password" type = "password" placeholder = "Password" onChange = { updateForm } />
            </form>
        </div>
    )
}

export default SignUp;