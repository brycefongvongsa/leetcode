function lastSurvivor(letters, coords) {
  for (let i = 0; i < coords.length; i++){
    // if it's 0, we get everything after
    if (coords[i] === 0) {
      letters = letters.slice(coords[i]+1)
    }
    // if it's the end of the string, we get everything before
    else if (coords[i] === letters.length - 1) {
      letters = letters.slice(0, coords[i])
      console.log(letters.slice(0, coords[i]))
    }
    // if coords[i] is in between
    else {
      letters = letters.slice(0, coords[i]) + letters.slice(coords[i]+1)
    }
  }
  return letters;
}

/*
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.
*/

/* top solution
function lastSurvivor(letters, coords) {
         letters = letters.split('');
         for (let i = 0; i < coords.length; i++) {
            letters.splice(coords[i], 1)
         }
         return letters.join('')
      }
*/
