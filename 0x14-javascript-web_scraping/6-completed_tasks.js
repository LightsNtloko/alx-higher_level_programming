// Import the required module
const request = require('request');

// Get the API URL from command line arguments
const apiUrl = process.argv[2];

// Function to fetch the tasks and compute completed tasks by user ID
function fetchCompletedTasks(url) {
  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error('Error fetching the API:', error);
      return;
    }

    // Initialize an object to store the count of completed tasks per user ID
    const userTasks = {};

    // Iterate over the tasks
    body.forEach(task => {
      if (task.completed) {
        if (!userTasks[task.userId]) {
          userTasks[task.userId] = 0;
        }
        userTasks[task.userId]++;
      }
    });

    // Filter out users with no completed tasks
    for (const userId in userTasks) {
      if (userTasks[userId] > 0) {
        console.log(`User ${userId}: ${userTasks[userId]}`);
      }
    }
  });
}

// Run the function with the provided API URL
fetchCompletedTasks(apiUrl);
