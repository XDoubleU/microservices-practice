const Pool = require('pg').Pool
const pool = new Pool({
  user: 'postgres',
  host: 'host.docker.internal',
  database: 'microservices_db',
  password: 'example',
  port: 6543,
})

const getCustomers = (request, response) => {
    pool.query('SELECT * FROM public.customers ORDER BY id ASC', (error, results) => {
      if (error) {
        throw error
      }
      response.status(200).json(results.rows)
    })
}

const getCustomer = (request, response) => {
    const id = parseInt(request.params.id)

    pool.query('SELECT * FROM public.customers WHERE id = $1', [id],(error, results) => {
      if (error) {
        throw error
      }
      response.status(200).json(results.rows[0])
    })
}

const addCustomer = (request, response) => {
    const { firstname, lastname } = request.body
  
    pool.query('INSERT INTO public.customers (firstname, lastname) VALUES ($1, $2) RETURNING *', [firstname, lastname], (error, result) => {
      if (error) {
        throw error
      }
      response.status(201).json(result.rows[0])
    })
  }

module.exports = {
getCustomers,
getCustomer,
addCustomer
}