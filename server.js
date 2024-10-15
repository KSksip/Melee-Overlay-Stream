const path = require('path').join(__dirname, 'overlay')
const express = require('express')
const PORT = 3000

const app = express()

app.use(express.json())
app.use(express.static(path))


const fs = require('fs');

app.get('/getinfo', (req, res) => {

    fs.readFile('./data/info.json', (err, json) => {
        let obj = JSON.parse(json);
        res.json(obj);
    });
});


//express server
app.listen(PORT, () => {
    console.log(`Server is running on http://127.0.0.1:${PORT}`)
  })
  