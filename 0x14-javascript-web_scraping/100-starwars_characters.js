#!/usr/bin/node

// Import the required module
const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Define the URL for the Star Wars API with the given Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch characters from the API and print their names
function fetchCharacters(movieUrl) {
  request(movieUrl, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching the API:', error);
      return;
    }

    // Check if the movie data is available
    if (body && body.characters) {
      let characterNames = [];

      // Iterate over the character URLs
      body.characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (error, response, character) => {
          if (error) {
            console.error('Error fetching character data:', error);
            return;
          }

          // Add the character name to the list
          characterNames.push(character.name);

          // If all character requests are complete, sort and print names
          if (characterNames.length === body.characters.length) {
            characterNames.sort(); // Sort names alphabetically
            characterNames.forEach(name => console.log(name));
          }
        });
      });
    } else {
      console.log('No characters found for this movie.');
    }
  });
}

// Run the function with the provided Movie ID
fetchCharacters(url);

