const client = require('./rpc-client')

client.moreNewsForUser({user: 'sholvoir.he@gmail.com'}, (response) => {
    console.assert(response.length > 0)
    cossole.log('moreNewsForUser test passed!')
})