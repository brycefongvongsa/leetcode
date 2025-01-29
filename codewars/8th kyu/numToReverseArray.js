function digitize(n) {
    //code here
    let arr = n.toString().split('').reverse();
    arr = arr.map(item => {
        return Number(item);
    });
    return arr;
}