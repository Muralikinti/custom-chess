# Microservice Communication Contract
## **How to Request Data**

To request data from the microservice, you need to send a POST request to the /apply endpoint with a JSON body containing the skills. 

      const axios = require('axios');
      
      const skills = {
          category1: ["node.js", "python", "javascript"],
          category2: ["Volunteer Teacher at Mary Coding Camp"],
          category3: ["Blogging Platform with Firebase Authentication"]
      };
      
      axios.post('http://localhost:3000/apply', { skills: skills })
          .then(response => {
              console.log(response.data);
          })
          .catch(error => {
              console.error(`Error: ${error}`);
          });

In this example, axios.post is used to send a POST request to the /apply endpoint of the microservice. The second argument to axios.post is the data to be sent in the request body, which in this case is an object containing the selected skills. The then method is used to handle the response from the server, and the catch method is used to handle any errors that occur during the request.

## **How to Receive Data**
When you send a request to the microservice, it processes the request and sends back a response. This response contains data that your application can use. In the context of your microservice, the response is a JSON object containing the result of the application and the total points.

## **UML Sequence Diagram**
