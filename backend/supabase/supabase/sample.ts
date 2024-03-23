const keyArray = ["a", "b", "c", "d", "e"];
const valueArray = [1, 2, 3, 4, 5];
const json: any  = {};  //"noImplicitAny": false とすればanyは省略可能

valueArray.forEach((item, index) => {
  json[keyArray[index]] = item;
});

console.log(json); //{a: 1, b: 2, c: 3, d: 4, e: 5}