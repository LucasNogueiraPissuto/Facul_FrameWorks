import './App.css';
import {Switch, Route, Link} from 'react-router-dom';
import Usuario from './Usuario';
import Home from "./Home";
import Sobre from "./Sobre";

function App() {
  return (
    <>
    <header>
      <Link to='/usuario'>Usuário</Link><br/>
      <Link to="/sobre/1">Sobre</Link>
    </header>
    <main>
      <Switch>
        <Route path="/home" component= {Home} />
        <Route path="/usuario" component= {Usuario} />
        <Route path="/sobre/:id?" component= {Sobre} />
      </Switch>
    </main>
    </>
  );
}

export default App;
