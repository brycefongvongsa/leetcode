function stairsIn20(s){
    //your code here
    let total = 0;
    for(let i = 0; i < s.length; i++) {
        for (let j = 0; j < s[i].length; j++) {
            total += s[i][j];
        }
    }
    return total *= 20;
}