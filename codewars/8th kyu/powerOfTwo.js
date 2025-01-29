function powersOfTwo(n){
    let result = [];
    let num = 1;
    for(let i = 0; i <= n; i++) {
        if (i === 0) {
            result.push(num);
        }
        else {
            num = num * 2;
            result.push(num);
        }
    }
    return result;
}