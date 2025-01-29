function getCount(str) {
    let count = 0;
    str.toLowerCase();
        for (letter of str) {
            if (letter === "a" || letter === "e" || letter === "i" || letter === "o" || letter === "u") {
            count++
        }
    }
    return count;
}
