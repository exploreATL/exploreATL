//Eshan Bhojane

//quick rough scketh of saving features so we can keep track of all places explored by user
//email: ebhojane1@student.gsu.edu , Discord: EmperorSupreme#3560

//we need an app.css



import logo from './logo.svg';
import './App.css';
import { checkoff } from './checkoff.js';
import { useState, useRef } from 'react';


function App() {

    const [places, setPlaces] = useState(["ATL", "JohnsCreek"]);
    const textInput = useRef(null);

    function onButtonClick() {
        let newItem = textInput.current.value;
        let newAreas = [...places, newItem];
        setPlaces(newAreas);
        textInput.current.value = "";
    }
    return (
        <div>
            <input ref={textInput} type="text" />
            <button onClick={onButtonClick}>Add an item</button>
            <ul>
                {places.map(i => <Explored areas={i} />)}
            </ul>
        </div>
    );
}


export default App;