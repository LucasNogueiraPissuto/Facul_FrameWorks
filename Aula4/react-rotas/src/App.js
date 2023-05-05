import './App.css';
import { Link, Routes, Route } from 'react-router-dom';
import Usuario from './Usuario';
import Sobre from './Sobre';
import CallApi from './ApiCall';

function App() {
  return (
    <>
    <header>
      <Link to='/usuario'>Usuario</Link> <br></br>
      <Link to='/sobre/6'>Sobre</Link> <br></br>
      <Link to='/tasks'>Tarefas</Link>
    </header>
    <main>
      <Routes>
        <Route path='/usuario' Component={Usuario}/>
        <Route path='/sobre/:id?' Component={Sobre}/>
        <Route path='/tasks' Component={CallApi}/>
      </Routes>
    </main>
    </>
  );
}

export default App;
