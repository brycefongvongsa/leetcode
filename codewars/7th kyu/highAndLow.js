function highAndLow(numbers){
  // numbers is a string of numbers. This splits the string into an array of strings and then turns the strings into numbers
  numbers = numbers.split(" ").map(num => {
    return Number(num)
  });
  let high = -99999;
  let low = 99999;
  // case if length is 1
  if (numbers.length === 1) {
    high = numbers[0];
    low = numbers[0];
  }
  
  // logic - check if the number is higher or lower than what we have set. 
  for (num of numbers) {
    if (high < num) {
      high = num;
    }
    if (low > num) {
      low = num;
    }
  }
  return `${high} ${low}`;
}

// In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
// All numbers are valid Int32, no need to validate them.
// There will always be at least one number in the input string.
// Output string must be two numbers separated by a single space, and highest number is first.
