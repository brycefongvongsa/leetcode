reverse = function(array) {
  let temp = "";
  let dec = array.length-1;
  for (let i = 0; i < Math.ceil(array.length/2); i++){
    if (i != Math.ceil(array.length/2)) {
      temp = array[dec];
      array[dec] = array[i];
      array[i] = temp;
      dec--;
    }
  }
  return array;
}

// Clever solution
// reverse = function(array) {
// var newArr = [];
// for (var i = array.length-1; i>=0; i--){
// 	newArr.push(array[i]);
// }
// return newArr;
// }
