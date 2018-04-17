const express = require('express')
const router = express.Router()
const rpcClient = require('../rpc-client/rpc-client')

router.get('/more', (req, res) => {
    console.log(`Get /news/more?${req.query}`)
    rpcClient.moreNewsForUser(req.query, news => res.json(news))
})

router.get('/clear', (req, res) => {
    rpcClient.clearNewsForUser(req.query, news => res.json(news))
})

router.post('/log', (req, res) => {
    rpcClient.logNewsClickForUser(req.query)
    res.status(200).end()
})
module.exports = router