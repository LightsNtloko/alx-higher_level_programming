#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Wedge Antilles character ID
const wedgeId = 18;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    let count = 0;
    data.results.forEach(film => {
      if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${wedgeId}/`)) {
        count++;
      }
    });
    console.log(count);
  } else {
    console.error('Error:', response.statusCode);
  }
});
