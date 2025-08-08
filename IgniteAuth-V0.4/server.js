const express = require('express');

const cors = require('cors');

const path = require('path');

const app = express();

const PORT = 3001;


// middleware 

app.use(cors());
app.use(express.urlencoded({extended: true}));

app.use(express.json());





// static serving 

app.use(express.static(path.join(__dirname,'public')));


// error code 
/*
app.get('/',(req,res)=>{

    res.send('IgniteAuth Test Engines Live');

    
});



app.use((req,res,next)=>{

        res.status(404).sendFile(path.join(__dirname,'public','404.html'));


    
});*/

// routing 

const router = require('./routes/routes.js');

app.use('/',router);






app.listen(PORT, ()=>{


    console.log(`listening at ${PORT}`);
});
