function nameShuffler(str){
    //Shuffle It
    str = str.split(" ");
    let temp = str[0];
    str[0] = str[1];
    str[1] = temp;
    str = str.join(" ");
    return str;
}