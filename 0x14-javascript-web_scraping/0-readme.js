#!/usr/bin/node

// Import the fs module
const fs = require('fs');

// Get the file path from the command line arguments
const filePath = process.argv[2];

// Read the file content
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
