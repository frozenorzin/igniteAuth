// routes/route.js
const express = require('express');
const router = express.Router();
const path = require('path');
const jwt = require('jsonwebtoken');
const { execFile } = require('child_process');

// ---- Helpers
function requireAuth(req, res, next) {
  const authHeader = req.headers.authorization || '';
  const [scheme, token] = authHeader.split(' ');
  if (scheme !== 'Bearer' || !token) {
    return res.status(403).json({ message: 'No token provided' });
  }
  jwt.verify(token, process.env.JWT_SECRET, (err, user) => {
    if (err) return res.status(401).json({ message: 'Invalid token' });
    req.user = user; // { username, iat, exp }
    next();
  });
}

// ---- HTML routes
// Smart client-side redirect: / → index.html (decide login or dashboard via localStorage)
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'html', 'index.html'));
});

// Login page
router.get(['/login', '/igniteauth.html'], (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'html', 'igniteauth.html'));
});

// Dashboard page (no server-side auth to avoid header issues on plain GET)
router.get('/dashboard', (req, res) => {
  res.sendFile(path.join(__dirname, '..', 'html', 'dashboard.html'));
});

// ---- API routes
// Login → returns JWT
router.post('/login', (req, res) => {
  const { username, password } = req.body || {};
  if (!username || !password) {
    return res.status(400).json({ message: 'username and password are required' });
  }

  if (
    username === process.env.ADMIN_USERNAME &&
    password === process.env.ADMIN_PASSWORD
  ) {
    const token = jwt.sign({ username }, process.env.JWT_SECRET, { expiresIn: '1h' });
    return res.json({ message: 'Login successful', token });
  }

  return res.status(401).json({ message: 'Invalid credentials' });
});

// Trigger command (JWT required) → child process exec
router.post('/trigger-command', requireAuth, (req, res) => {
  const { targetNode, intent, command } = req.body || {};

  if (!targetNode || !intent || !command) {
    return res.status(400).json({
      message: 'Missing required fields: targetNode, intent, command'
    });
  }

  // Path to your executable wrapper that understands [targetNode, intent, command]
  const execPath = path.join(__dirname, '..', 'bin', 'reboot_firmware');
  const args = [targetNode, intent, command];

  execFile(execPath, args, (error, stdout, stderr) => {
    if (error) {
      console.error('Exec error:', error);
      return res.status(500).json({ message: 'Execution failed', error: error.message, stderr: (stderr || '').toString() });
    }

    return res.json({
      message: '✅ Command executed successfully!',
      output: (stdout || '').toString().trim(),
    });
  });
});

module.exports = router;
