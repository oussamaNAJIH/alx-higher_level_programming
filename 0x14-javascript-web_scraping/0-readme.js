#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    console.log(body);
  } else {
    console.error(error);
  }
});
