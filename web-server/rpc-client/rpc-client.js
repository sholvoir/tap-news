const jayson = require('jayson')
const cfg = require('../../config/config.json')
const client = jayson.client.http({hostname: cfg.backendServer.host, port: cfg.backendServer.port})

const moreNewsForUser = ({user, page = 0}, callback) => {
    client.request('moreNewsForUser', [user, page], (err, error, response) => {
        if (err) throw err
        callback(response)
    })
}

const clearNewsForUser = ({user}, callback) => {
    client.request('clearNewsForUser', [user], (err, error, response) => {
        if (err) throw err
        callback(response)
    })
}

const logNewsClickForUser = ({user, news}) => {
    console.log(`logNewsClickForUser email:${user} news-digest:${news}`)
    client.request('logNewsClickForUser', [user, news], (err, error, response) => {
        if (err) throw err
        console.log(response)
    })
}

module.exports = { moreNewsForUser, clearNewsForUser, logNewsClickForUser }