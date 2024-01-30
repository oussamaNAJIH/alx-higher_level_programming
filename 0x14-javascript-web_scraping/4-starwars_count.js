#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      const characters = movie.characters;
      for (const character of characters) {
        if (character === 'https://swapi-api.alx-tools.com/api/people/18/') {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
