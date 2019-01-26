const mongoose = require('mongoose')
const bcrypt = require('bcrypt')

const UserSchema = new mongoose.Schema({
    email: {
        type: String,
        index: {
            unique: true
        }
    },
    password: String
})

UserSchema.methods.comparePassword = function(password, callback) {
    bcrypt.compare(password, this.password, callback)
}

UserSchema.pre('save', function saveHook(next) {
    const user = this
    bcrypt.hash(user.password, (err, hash) => {
        if (err) {
            next(err)
        } else {
            user.password = hash
            next()
        }
    })
})

module.exports = mongoose.model('User', UserSchema)
