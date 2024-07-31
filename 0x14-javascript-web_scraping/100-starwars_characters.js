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
      // Iterate over the character URLs
      body.characters.forEach(characterUrl => {
        request(characterUrl, { json: true }, (error, response, character) => {
          if (error) {
            console.error('Error fetching character data:', error);
            return;
          }

          // Print the character name
          console.log(character.name);
        });
      });
    } else {
      console.log('No characters found for this movie.');
    }
  });
}

// Run the function with the provided Movie ID
fetchCharacters(url);

