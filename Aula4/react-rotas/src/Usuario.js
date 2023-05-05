import React from "react";
import { Link } from "react-router-dom";

export default function Usuario(){
    return(
        <div>
            <h1>Usuário</h1>
            <Link to="/usuario">ir para pagina usuario</Link> <br></br>
            <Link to="/App">ir para pagina Incial</Link>
        </div>
    );
}