import React from 'react';
import './App.css';
import {Routes} from "react-router-dom";
import MainView from "./components/MainView";

function App() {
    return (
        <div>
            {/*<Routes>*/}
            {/*    /!*<Route path="/" element={<Home />} />*!/*/}
            {/*</Routes>*/}
            <MainView/>
        </div>
    );
}

export default App;
