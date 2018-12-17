const modal = (state = {}, action) => {
  switch (action.type) {
    case 'SET_QUERY': {
      return {
        ...state,
        query: action.query,
      }
    }
    case 'SET_RESPONSE': {
      return {
        ...state,
        response: action.response,
      }
    }
    default:
      return state
  }
}
 
export default modal
