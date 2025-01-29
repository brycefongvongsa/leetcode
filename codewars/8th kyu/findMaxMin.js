var min = function(list){
    let minNum;
    for( let i = 0; i < list.length; i++) {
        if (i == 0) {
            minNum = list[i];
        }
        if (minNum > list[i]) {
            minNum = list[i];
        }
    }
    return minNum;
  }
  var max = function(list){
    let maxNum;
    for( let i = 0; i < list.length; i++) {
        if (i == 0) {
            maxNum = list[i];
        }
        if (maxNum < list[i]) {
            maxNum = list[i];
        }
    }
    return maxNum;
}