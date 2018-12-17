export function setQuery (query) {
  return dispatch => new Promise((resolve) => {
    return resolve(dispatch({
      type: 'SET_QUERY',
      query: query
    }));
  });
}

export function setResponse (response) {
  return dispatch => new Promise((resolve) => {
    return resolve(dispatch({
      type: 'SET_RESPONSE',
      response: response
    }));
  });
}
