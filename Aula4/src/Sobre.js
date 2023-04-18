import React from 'react';
import { Link, useParams } from 'react-router-dom';

export default function Sobre (){
    const { id } = useParams();
    return (
        <div>
            <h1>Sobre: {id} </h1>
            <Link to="/">Voltar</Link>
        </div>
    );
}