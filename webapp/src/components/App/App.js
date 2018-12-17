import React from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';

import style from './App.scss';
import NavBar from './../NavBar';
import List from './../List';
/**
 * App Component
 * @type {Class}
 */
class App extends React.Component {
  componentWillMount () {
    let that = this;
    fetch(`http://localhost:5000/world`)
      .then(function(response) {
        console.log(response);
      })
  }

  /**
   * Render function for App Component
   * @return {JSX} Component to render
   */
  render () {
    return (
      <div>
        <Router>
          <div className={style.App}>
            <Route path='/' component={NavBar} />
            <Route path='/' component={List} />
          </div>
        </Router>
      </div>
    );
  }
}

export default App;
