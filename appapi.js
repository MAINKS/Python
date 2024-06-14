import React, { useState, useEffect } from 'react';

const AdvancedApp = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch('https://api.example.com/data');
      const jsonData = await response.json();
      setData(jsonData);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <h1>Advanced App</h1>
      {data.length > 0 ? (
        <ul>
          {data.map((item) => (
            <li key={item.id}>{item.name}</li>
          ))}
        </ul>
      ) : (
        <p>Loading data...</p>
      )}
    </div>
  );
};

export default AdvancedApp;

// index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { createStore } from 'redux';
import rootReducer from './reducers';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import NotFound from './components/NotFound';

const store = createStore(rootReducer);

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <Switch>
        <Route exact path="/" component={Home} />
        <Route path="/about" component={About} />
        <Route path="/contact" component={Contact} />
        <Route component={NotFound} />
      </Switch>
    </Router>
  </Provider>,
  document.getElementById('root')
);

// reducers.js
import { combineReducers } from 'redux';

const initialState = {
  user: null,
};

const userReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_USER':
      return {
        ...state,
        user: action.payload,
      };
    case 'CLEAR_USER':
      return {
        ...state,
        user: null,
      };
    default:
      return state;
  }
};

const rootReducer = combineReducers({
  user: userReducer,
});

// export default rootReducer;

// components/Home.js
import React from 'react';
import { connect } from 'react-redux';

const Home = ({ user }) => {
  return (
    <div>
      <h1>Welcome to the Home page!</h1>
      {user ? <p>Welcome, {user}!</p> : <p>Please log in.</p>}
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    user: state.user.user,
  };
};

// export default connect(mapStateToProps)(Home);

// components/About.js
import React from 'react';

const About = () => {
  return (
    <div>
      <h1>About Us</h1>
      <p>We are a leading company in the industry.</p>
    </div>
  );
};

// export default About;

// components/Contact.js
import React from 'react';

const Contact = () => {
  return (
    <div>
      <h1>Contact Us</h1>
      <p>Feel free to reach out to us for any inquiries.</p>
    </div>
  );
};

// export default Contact;

// components/NotFound.js
import React from 'react';

const NotFound = () => {
  return (
    <div>
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
    </div>
  );
};

// export default NotFound;
