const jwt = require('jsonwebtoken')
const User = require('mongoose').model('User')
const PassportLocalStrategy = require('passport-local').Strategy
const config = require('../../config/config.json')

module.exports = new PassportLocalStrategy({
    usernameField: 'email',
    passwordField: 'password',
    session: false,
    passReqToCallback: true
}, (req, email, password, done) => {
    const userData = {
        email: email.trim(),
        password
    }
    return User.findOne({email: userData.email}, (err, user) => {
        if (err) {
            return done(err)
        }
        if (!user) {
            const error = new Error('Incorrect Email or Password.')
            error.name = 'IncorrectCredentialsError'
            return done(error)
        }
        return user.comparePassword(userData.password, (passwordError, isMatch) => {
            if (passwordError) {
                return done(passwordError)
            }
            if (!isMatch) {
                const error = new Error('Incorrect Email or Password.')
                error.name = 'IncorrectCredentialsError'
                return done(error)
            }
            const payload = {
                sub: user._id
            }
            const token = jwt.sign(payload, config.jwtSecret)
            return done(null, token, null)
        })
    })
})