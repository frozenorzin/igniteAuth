// server.js
require('dotenv').config();

const cors = require('cors');
const express = require('express');
const path = require('path');

const app = express();
const PORT = process.env.PORT || 3500;

// --- Middleware
app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Static files (CSS, images, etc.)
app.use('/', express.static(path.join(__dirname, 'public')));

// HTML files are not static-served automatically — routed via /routes/route.js
app.use('/', require('./routes/route'));

// 404 handler
app.all(/.*/, (req, res) => {
  res.status(404);
  if (req.accepts('html')) {
    res.sendFile(path.join(__dirname, 'html', '404.html'));
  } else if (req.accepts('json')) {
    res.json({ message: '404 Not Found' });
  } else {
    res.type('txt').send('404 Not Found');
  }
});

app.listen(PORT, () => console.log(`🚀 Server running on http://localhost:${PORT}`));
