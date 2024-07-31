#!/usr/bin/node

// Import the request module
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
