const config = require('../config/config.json')
const path = require('path')
const express = require('express')
const app = express()

require('./models/main').connect(config.mongoDBUser.uri)

app.use(require('cors')())

const passport = require('passport')
const localSignUpStrategy = require('./passport/signup-passport')
const localLoginStrategy = require('./passport/login-passport')

app.use(passport.initialize())
passport.use('local-signup', localSignUpStrategy)
passport.use('local-login', localLoginStrategy)

const authRoute = require('./routes/auth')
app.use('/auth', authRoute)

const authCheckerMiddleware = require('./middleware/auth-checker')
const newsRoute = require('./routes/news')
app.use('/news', authCheckerMiddleware, newsRoute)

const root = path.join(__dirname, ...config.webServer.staticPath)
app.use('/', express.static(root))

app.use((req, res) => res.sendFile('index.html', {root}))

const printStartInfo = () => console.log(`Example app listening on port ${config.webServer.listenPort}!`)
app.listen(config.webServer.listenPort, printStartInfo)
