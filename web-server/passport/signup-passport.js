const User = require('mongoose').model('User')
const PassportLocalStrategy = require('passport-local').Strategy

module.exports = new PassportLocalStrategy({
    usernameField: 'email',
    passwordField: 'password',
    passReqToCallback: true
}, (req, email, password, done) => {
    const userData = {
        email: email.trim(),
        password
    }
    const newUser = new User(userData)
    newUser.save((err) => {
        if (err) done(err)
        else {
            console.log('Save new user!')
            done(null)
        }
    })
})