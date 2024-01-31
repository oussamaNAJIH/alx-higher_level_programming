#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');

request(url, function (error, response, body) {
  if (!error) {
    fs.writeFile(path, body, function (err) {
      if (err) {
        console.log(err);
      }
    });
  } else {
    console.log(error);
  }
});
