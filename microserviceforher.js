const express = require('express');
const app = express();
app.use(express.json());

const goodSkills = ["node.js", "python", "javascript", "Front-End Developer Intern at TechCraft Studios", "Volunteer Teacher at Mary Coding Camp", "Quality Assurance Job Shadow at Intell", "Blogging Platform with Firebase Authentication", "Portfolio Website using React"];
const mehSkills = ["Microsoft Excel", "Graphic Design", "Data Entry", "Customer Service", "MATLAB", "Data Entry Job at FebEx", "Barista at Storbucks", "Customer Service Spreadsheet", "Entrepreneurial Mindset Vlog Channel on Youtube"];


app.post('/apply', (req, res) => {
    const skills = req.body.skills;
    let points = 0;

    // Calculate points
    for (let category in skills) {
        for (let skill of skills[category]) {
            if (goodSkills.includes(skill)) {
                points += 1;
            }
        }
    }

    
    // Check if user passes
    const pass = points >= 9;

    // Send response
    res.json({ pass: pass, points: points });
});

const port = process.env.PORT || 3000;
app.listen(port, () => console.log(`Server running on port ${port}`));