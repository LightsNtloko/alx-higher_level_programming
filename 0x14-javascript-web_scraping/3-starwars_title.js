#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL using the movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.error('Error:', response.statusCode);
  }
});
