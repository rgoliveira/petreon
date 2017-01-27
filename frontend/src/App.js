import React, { Component } from 'react';
import logo from './logo.svg';
import './App.sass';

// DO NOT USE, SIMPLE EXAMPLE TO ILLUSTRATE REACT
const Pet = ({imageURL, name}) => {
    return (
        <div>
            <img src={imageURL} alt={name} />
            <h2>{name}</h2>
        </div>
    )
};

class MainApp extends Component {
    render() {
    return (
        <div className="App">
            <div className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <h2>Welcome to Petreon!</h2>
            </div>
            <p className="App-intro">
                To get started, edit <code>src/App.js</code> and save to reload.
            </p>
            <Pet imageURL="http://orig15.deviantart.net/8661/f/2011/235/3/3/ballerina_by_deingel_dog_stock-d47kjyg.jpg"
                 name="Phil"/>
        </div>
    );
    }
}

export default MainApp;
