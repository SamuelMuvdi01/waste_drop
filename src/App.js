import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import { Home } from './pages/Home';
import './css/App.css';

const App = () => {
  return (
    <div>
    <Router>
  <Navbar />
  <div className="pages">
<Routes>
<Route path='/Home' element={<Home />}/>
</Routes>
</div>
</Router>
</div>
  );
}

export default App;

