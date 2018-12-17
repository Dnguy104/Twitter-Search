import React from 'react';
import { Button, FormGroup, FormControl } from 'react-bootstrap';

import style from './Search.scss';
import { setQuery, setResponse } from './../../../actions';
import { connect } from 'react-redux';



/**
 * UI Component
 * @type {Class}
 */
class Search extends React.Component {
  /**
   * Constructor for UI Component
   * @param  {Object} props  Props passed to this class
   * @return {void}
   */
  constructor (props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
    this.handleKeyPress = this.handleKeyPress.bind(this);
    this.state = {
      value: ''
    };
  }

  handleChange(e) {
   this.setState({ value: e.target.value });
  }

  handleKeyPress(target) {
    if(target.charCode==13){
      this.search();
    }
  }

  search() {
    //placeholder
    let value = this.state.value;

    let that = this;
    fetch(`http://localhost:5000/hello?query=${value}`)
      .then(function(response) {
        return response.json();
      })
      .then(function(myresponse) {
        that.props.setResponse(myresponse);
      })

    if (value != '') {
      this.props.setQuery(value);
    }
  }

  /**
   * Render function for UIComponent Component
   * @return {JSX} Component to render
   */
  render () {
    return (
      <div className={style.searchBar}>
        <FormGroup style={{paddingTop: '18px', color: 'ghostwhite'}}>
          <FormControl
            bsClass={style.search}
            placeholder="Query"
            onKeyPress={this.handleKeyPress}
            onChange={this.handleChange}
            />
          <Button
            bsClass={style.find}
            onClick={() => this.search()}>
            Search
          </Button>
        </FormGroup>
      </div>
    );
  }
}

const mapDispatchToProps = dispatch => ({
  setQuery: query => dispatch(setQuery(query)),
  setResponse: response => dispatch(setResponse(response)),
}) 
 
export default connect(null, mapDispatchToProps)(Search)
