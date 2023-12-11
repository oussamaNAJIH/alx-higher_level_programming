#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const myArray = [];
  for (let index = 2; index < argv.length; index++) {
    myArray.push(parseInt(argv[index]));
  }
  myArray.sort((a, b) => b - a);
  console.log(myArray[1]);
}
