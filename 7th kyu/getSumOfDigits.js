function getSumOfDigits(integer) {
    var sum = null;
    var digits =  Math.floor(integer).toString();
    
    // run 3 times
    for(var ix = 0; ix < digits.length; ix++) {
        sum += Number(digits[ix]);
    }
    return sum;
}