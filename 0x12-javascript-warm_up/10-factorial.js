#!/usr/bin/node
function fact (x) {
  if (x === 0 || isNaN(x)) {
    return 1;
  }
  return x * fact(x - 1);
}
const { argv } = require('process');
const num = parseInt(argv[2]);
console.log(fact(num));
