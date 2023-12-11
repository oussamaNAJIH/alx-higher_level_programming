#!/usr/bin/node
const { argv } = require('process');
let myVar = parseInt(argv[2]);
if (isNaN(myVar)) {
  console.log('Missing number of occurrences');
} else {
  while (myVar > 0) {
    console.log('C is fun');
    myVar--;
  }
}
