// return masked string
function maskify(cc) {
  let maskedStr = "";
  for (let i = 0; i < cc.length - 4; i ++) {
    maskedStr += "#";
  }
  maskedStr += cc.substring(cc.length-4);
  return maskedStr;
}
