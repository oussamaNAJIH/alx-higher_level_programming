#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  for (let index = list.length - 1; index >= 0; index--) {
    myList.push(list[index]);
  }
  return myList;
};
