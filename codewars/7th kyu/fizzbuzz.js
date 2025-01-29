// Return an array
// Fizz = divisible by 3
// Buzz = divisible by 5
// FizzBuzz = divisble by both 3 and 5
function fizzbuzz(n) {
  let arr = [];
  for (let i = 0; i < n; i++){ 
    arr.push(i+1);
  }
  console.log(arr);
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 3 === 0 && arr[i] % 5 === 0) {
      arr[i] = "FizzBuzz";
    }
    else if (arr[i] % 3 === 0) {
      arr[i] = "Fizz";
    }
    else if (arr[i] % 5 === 0) {
      arr[i] = "Buzz"
    }
  }
  return arr;
}
