import './App.css';
import {Route, Routes} from "react-router-dom"
import NewGame from './pages/NewGame'
import GameChoice from './pages/GameChoice';
import SetGame from './pages/SetGame';
import Game from './pages/Game';
import EndGame from './pages/EndGame';

function App() {
  return (
    <Routes>
      <Route path='/' exact element={<NewGame />}/>
      <Route path='/gamechoice' element={<GameChoice />} />
      <Route path='/setgame' element={<SetGame />} />
      <Route path='/game' exact element={<Game />} />
      <Route path='/endgame' element={<EndGame />} />
    </Routes>
  );
}

export default App;
