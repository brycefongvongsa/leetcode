function isPalindrome(x) {
    // your code here
    x = x.toLowerCase();
    let test = x.split('').reverse().join('')
    return test === x
}