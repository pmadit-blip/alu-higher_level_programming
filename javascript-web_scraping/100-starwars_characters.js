#!/usr/bin/node
const request = require('request');
request('https://swapi-api.alx-tools.com/api/films/' + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (const url of characters) {
      request(url, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
