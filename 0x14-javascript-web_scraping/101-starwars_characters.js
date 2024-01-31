#!/usr/bin/node
const request = require('request');

const movieId = parseInt(process.argv[2]);
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId + '/';

request(movieUrl, async function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const data = JSON.parse(body);
    const characters = data.characters;

    // Using async/await to make requests in order
    for (let index = 0; index < characters.length; index++) {
      try {
        const characterResponse = await new Promise((resolve, reject) => {
          request(characters[index], function (error, response, body) {
            if (!error) {
              resolve(body);
            } else {
              reject(error);
            }
          });
        });

        const character = JSON.parse(characterResponse);
        console.log(character.name);
      } catch (error) {
        console.log(error);
      }
    }
  } else {
    console.log(error);
  }
});
