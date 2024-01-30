#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = 18;
let count = 0;

request(url, function (error, response, body) {
  if (!error) {
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      const characters = movie.characters;
      for (const character of characters) {
        if (character.endsWith(`/${characterId}/`)) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  } else {
    console.log(error);
  }
});
