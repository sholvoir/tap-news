const express = require('express')
const passport = require('passport')
const validator = require('validator')
const jsonParser = require('body-parser').json()
const router = express.Router()

const validateLoginForm = payload => {
    console.log(payload)
    const errors = {}
    let isFormValid = true
    let message = ''
    if (!payload || typeof payload.email !== 'string' || payload.email.trim().length === 0) {
        isFormValid = false
        errors.email = 'Please provide your email address.'
    }
    if (!payload || typeof payload.password !== 'string' || payload.password.trim().length === 0) {
        isFormValid = false
        errors.password = 'Please provide your password.'
    }
    if (!isFormValid) {
        message = 'Check the form for errors'
    }
    return {success: isFormValid, message, errors}
}

router.post('/login', jsonParser, (req, res, next) => {
    const validationResult = validateLoginForm(req.body)
    if (!validationResult.success) {
        return res.status(400).json({
            success: false,
            message: validationResult.message,
            errors: validationResult.errors
        })
    }
    return passport.authenticate('local-login', (err, token, userData) => {
        if (err) {
            return res.status(400).json({
                success: false,
                message: (err.name == 'IncorrectCredentialsError' ? '': 'Could Not Process the Form')
                    + err.message
            })
        } else {
            return res.json({
                success: true,
                message: 'You have successfully logged in!',
                token,
                user: userData
            })
        }
    })(req, res, next)
})

const validateSignUpForm = (payload) => {
    console.log(payload)
    const errors = {}
    let isFormValid = true
    let message = ''
    if (!payload || typeof payload.email !== 'string' || !validator.isEmail(payload.email)) {
        isFormValid = false
        errors.email = 'Please provide a correct email address.'
    }
    if (!payload || typeof payload.password !== 'string' || payload.password.length < 8) {
        isFormValid = false
        errors.password = 'Password must have at least 8 characters.'
    }
    if (!isFormValid) {
        message = 'Check the form of errors.'
    }
    return {
        success: isFormValid,
        message,
        errors
    }
}

router.post('/signup', jsonParser, (req, res, next) => {
    const validationResult = validateSignUpForm(req.body)
    if (!validationResult.success) {
        console.log('Validation Result Failed!')
        return res.status(400).json({
            success: false,
            message: validationResult.message,
            errors: validationResult.errors
        })
    }
    return passport.authenticate('local-signup', err => {
        if (err) {
            console.log(err)
            if (err.code === 11000) {
                return res.status(409).json({
                    success: false,
                    message: 'Check the form for errors.',
                    errors: {
                        email: 'This email is already taken.'
                    }
                })
            }
            return res.status(400).json({
                success: false,
                message: 'Could not process the Form.'
            })
        }
        return res.status(200).json({
            success: true,
            message: 'You have successfully signed up! Now you can log in.'
        })
    })(req, res, next)
})

module.exports = router