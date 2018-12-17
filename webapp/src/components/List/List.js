import React from 'react';
import style from './List.scss';
import { ListGroup, ListGroupItem } from 'react-bootstrap';
import { connect } from 'react-redux'


/**
 * UI Component
 * @type {Class}
 */
class List extends React.Component {
  /**
   * Constructor for UI Component
   * @param  {Object} props  Props passed to this class
   * @return {void}
   */
  constructor (props) {
    super(props);
    this.state = {
      request: null,
      query: null,
    };
  }

  // componentDidMount () {
  //   let that = this;
  //   fetch('http://localhost:5000/hello', {mode: 'cors'})
  //     .then(function(response) {
  //       response.text().then(function (text) {
  //         that.setState({request: text});
  //       });
  //     })
  // }

  // componentWillMount () {
  //   let that = this;
  //   fetch('http://localhost:5000/hello?test=fuckmisdf')
  //     .then(function(response) {
  //       return response.json();
  //     })
  //     .then(function(myresponse) {
  //       console.log(myresponse);
  //       that.setState({request: myresponse})
  //     })
  // }

  componentDidUpdate () {
    console.log(this.props.response);
  }

  /**
   * Render function for UIComponent Component
   * @return {JSX} Component to render
   */
  render () {

    return (
      <div className={style.container}>
        <ListGroup>
          {Array.isArray(this.props.response) ? this.props.response.map(element => <ListGroupItem><p>user: {element.username}</p> <p>text: {element.text}</p> <p>score: {element.score}</p><p>time: {element.time}</p></ListGroupItem>) : null}
        </ListGroup>
      </div>
    );
  }
}

const mapStateToProps = state => ({
  query: state.query || {},
  response: state.response || {},
})
 
export default connect(mapStateToProps, null)(List)
