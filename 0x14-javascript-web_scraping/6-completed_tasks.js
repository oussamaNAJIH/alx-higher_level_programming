#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (!error) {
    const results = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed) {
        const userId = todo.userId.toString();
        results[userId] = (results[userId] || 0) + 1;
      }
    }
    console.log(results);
  } else {
    console.log(error);
  }
});
