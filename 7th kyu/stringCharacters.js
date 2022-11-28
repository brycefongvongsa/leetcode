function solve(s){
    //..
    var letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    var numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    var specialCharacters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '{', '}', ':', ';', '.', ',', '/', '<', '>', '|', '"', "'", "?", "_", '+', '[', ']', "\\", '`', '~']
    var results = [0, 0, 0, 0];
    for (var i = 0; i < s.length; i++) {
    // letters
    for (var j = 0; j < letters.length; j++) {
            if (s[i] === letters[j].toUpperCase()) {
            results[0] = results[0] + 1;
        }
            else if (s[i] === letters[j]) {
                results[1] = results[1] + 1;
            }
        }
        // numbers
        for (var j = 0; j < numbers.length; j++) {
            if (s[i] === numbers[j]) {
                results[2] = results[2] + 1;
            }
        }
        // special characters
        for (var j = 0; j < specialCharacters.length; j++) {
            if (s[i] === specialCharacters[j]) {
                results[3] = results [3] + 1;
                console.log(specialCharacters[j])
            }
        }
    }
    return results;
}