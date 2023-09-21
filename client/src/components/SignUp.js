import React from 'react';
import { useState } from 'react';
import Navbar from './Navbar';

function SignUp () {

    const [ form, setForm ] = useState( {} )
    const [ baseForm, setBaseForm ] = useState( {
        name: 'Username',
        password: 'Password',
    } );

    function updateForm ( e ) {
        setForm(f => {
            return {...f, [ e.target.name ]: e.target.value }
        } )
    }

    function handleSubmit ( e ) {
        e.preventDefault()
        fetch( 'http://127.0.0.1:5555/users', {
            method: "POST",
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify( form )
        } )
        .then( r => {
            if ( r.ok ) {
                r.json().then( console.log )
            } else {
                console.error( "Something went wrong" )
                console.error( 'POST /users status:', r.status )
                r.text().then( console.warn )
            }
        } )
    }
    
    return (
        <div>
            <Navbar />
            <h1>Sign Up:</h1>
            <form onSubmit = { handleSubmit } >
                <input name = "username" type = "text" placeholder = "Username" onChange = { updateForm } />
                <input name = "password" type = "password" placeholder = "Password" onChange = { updateForm } />
                <button type = "submit" >Submit</button>
            </form>
        </div>
    )
}

export default SignUp;