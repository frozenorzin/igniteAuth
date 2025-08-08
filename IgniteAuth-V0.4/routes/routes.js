// routes/route.js
const express = require('express');
const router = express.Router();
const path = require('path');
const jwt = require('jsonwebtoken');
const { execFile } = require('child_process');

// 🔐 Login HTML page -  small correction needed , if requested main server at '/' redirect to '/login' - > new feature needed 
router.get(['/login', '/html', '/igniteauth.html'], (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'html', 'igniteauth.html'));
});

// 🔐 Login endpoint — return JWT if credentials match
router.post('/login', (req, res) => {
  const { username, password } = req.body;

  if (
    username === process.env.ADMIN_USERNAME &&
    password === process.env.ADMIN_PASSWORD
  ) {
    const token = jwt.sign({ username }, process.env.JWT_SECRET, { expiresIn: '1h' });
    res.json({ message: 'Login successful', token });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
}); 

// 🚀 Command trigger route (child process)
router.post('/trigger-command', (req, res) => {
  const { targetNode, intent, command, token } = req.body;

  if (!token) return res.status(403).json({ message: 'No token provided' });  // highly critical bugs ,, token not fetched from local stores yet 

  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(401).json({ message: 'Invalid token' });

    // ✅ Valid token — call executable
    const execPath = path.join(__dirname, '..', 'bin', 'command_exec'); // Adjust path if needed
    const args = [targetNode, intent, command];

    execFile(execPath, args, (error, stdout, stderr) => {
      if (error) {
        console.error(`Exec error: ${error.message}`);
        return res.status(500).json({ message: 'Execution failed', error: error.message });
      }

      res.json({
        message: '✅ Command executed successfully!',
        output: stdout.trim()
      });
    });
  });
});

module.exports = router; // exporting is essential here .... 
