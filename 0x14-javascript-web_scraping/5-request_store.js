#!/usr/bin/node

// Import the required modules
const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Function to fetch the webpage and store it in a file
function fetchAndStore(url, filePath) {
  request(url, (error, response, body) => {
    if (error) {
      console.error('Error fetching the URL:', error);
      return;
    }

    // Write the response body to the specified file
    fs.writeFile(filePath, body, 'utf8', (err) => {
      if (err) {
        console.error('Error writing to file:', err);
        return;
      }
      console.log(`Content successfully saved to ${filePath}`);
    });
  });
}

// Run the function with the provided URL and file path
fetchAndStore(url, filePath);
