import React from "react";
import { Link, useParams } from "react-router-dom";

export default function Sobre(){
    const {id} = useParams();
    return(
        <div>
            <h1>Essa é a pagina sobre. ID: {id}</h1>
            <Link to="/usuario">ir para pagina usuario</Link> <br></br>
            <Link to="/App">ir para pagina Incial</Link>
        </div>
    );
}