#!/usr/bin/node

const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Check if the URL is provided
if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API_URL>');
  process.exit(1);
}

// Define the URL for Wedge Antilles' data
const wedgeUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

// Function to count the number of films
const countFilms = (url) => {
  request(url, { json: true }, (err, res, body) => {
    if (err) {
      console.error(err);
      process.exit(1);
    }
    
    // Check if the API response contains films
    if (body && body.films) {
      console.log(body.films.length);
    } else {
      console.error('Error: No films found for the character.');
      process.exit(1);
    }
  });
};

// Call the function with the URL
countFilms(wedgeUrl);
