import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Link, NavLink } from 'react-router-dom'
import './index.css';
import registerServiceWorker from './registerServiceWorker';
import Releases from './components/releases'
import Merch from './components/merch'
import Videos from './components/videos'
import Home from './components/home'
import { ConnectedRouter } from 'react-router-redux'
import store, { history } from './store'
import { Provider } from 'react-redux'
import navigation_logo from './navigation-logo.png'
import { Col, Grid } from 'react-bootstrap'


ReactDOM.render(
  <div>
    <Provider store={store}>
      <ConnectedRouter history={history}>
        <div id={'page'}>
          <Grid id={'navigation-bar'}>
            <Col md={2}>
              <img alt={"img-logo"} src={navigation_logo}/>
            </Col>
            <Col md={10}>
              <div className={'links'}>
                <NavLink activeClassName="selected" to="/releases">Releases</NavLink>
                <span className='link-seperator'/>
                <NavLink activeClassName="selected" to="/merch">Merch</NavLink>
                <span className='link-seperator'/>
                <NavLink activeClassName="selected" to="/videos">Videos</NavLink>
              </div>
            </Col>
          </Grid>
          <Grid id='content'>
            <Route exact path="/" component={Home} />
            <Route exact path="/releases" component={Releases} />
            <Route exact path="/merch" component={Merch} />
            <Route exact path="/videos" component={Videos} />
          </Grid>
        </div>
      </ConnectedRouter>
    </Provider>
  </div>
  ,document.getElementById('root')
);

registerServiceWorker();
