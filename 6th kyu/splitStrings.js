function solution(str){
    // odd
    if (str.length % 2 === 1) {
      str = str + "_";
    }
    let result = str.match(/.{1,2}/g) ?? [];
    return result;
}