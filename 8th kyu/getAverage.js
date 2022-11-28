let getAverage = marks => Math.floor(marks.reduce( (accum, num) => accum + num, 0) / marks.length);
  //TODO : calculate the downward rounded average of the marks array