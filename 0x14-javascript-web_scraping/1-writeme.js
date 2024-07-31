#!/usr/bin/node

// Import fsModule
const fs = require('fs');

// Call for the file path and string from the cmd line arguments
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

// Write the string in the file
fs.writeFile(filePath, stringToWrite, 'utf-8', (err) => {
  if (err) {
	  console.error(err);
  }
});
