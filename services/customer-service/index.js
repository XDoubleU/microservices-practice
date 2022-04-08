var express = require('express')
const db = require('./queries')
var app = express()
app.use(express.json())
var port = 4002

app.get('/', db.getCustomers)
app.get('/:id', db.getCustomer)
app.post('/', db.addCustomer)

app.listen(port, function () {
  console.log('app listening on port ${port}!')
})