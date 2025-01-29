function arrayPlusArray(arr1, arr2) {
    let sum = 0;
    for (num in arr1) {
      sum += arr1[num];
    }
    for (num in arr2) {
      sum += arr2[num];
    }
    return sum;
}