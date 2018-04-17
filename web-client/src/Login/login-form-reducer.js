import isEmail from 'validator/lib/isEmail'
import {LOGIN_FORM_CHANGE, LOGIN_FORM_RESET} from './login-form-action'

const initLoginFormData = {
    email: '',
    password: '',
    errors: {}
}

export default(loginFormData = initLoginFormData, action) => {
    switch (action.type) {
        case LOGIN_FORM_CHANGE:
            const data = Object.assign({}, loginFormData, action.payload)
            if (action.payload.email) {
                data.errors.email = isEmail(action.payload.email) ? '' : 'Not an Email'
            }
            return data
        case LOGIN_FORM_RESET:
            return initLoginFormData
        default:
            return loginFormData
    }
}