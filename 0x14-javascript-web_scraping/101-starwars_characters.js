#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/people/';
const movieId = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(url, function (error, response, body) {
  if (!error) {
    const data = JSON.parse(body);
    const people = data.results;
    for (const character of people) {
      if (character.films.includes(movieUrl)) {
        console.log(character.name);
      }
    }
  } else {
    console.log(error);
  }
});
