const axios = require('axios');

const skills = {
    category1: ["node.js", "python", "javascript"],
    category2: ["Volunteer Teacher at Mary Coding Camp", "Quality Assurance Job Shadow at Intell", "Data Entry Job at FebEx"],
    category3: ["Blogging Platform with Firebase Authentication", "Portfolio Website using React"]
};

axios.post('http://localhost:3000/apply', { skills: skills })
    .then(response => {
        console.log(`Application status: ${response.data.pass ? 'Passed' : 'Failed'}`);
        console.log(`Total points: ${response.data.points}`);
    })
    .catch(error => {
        console.error(`Error: ${error}`);
    });
