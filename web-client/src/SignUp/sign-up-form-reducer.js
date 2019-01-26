import isEmail from 'validator/lib/isEmail'
import {SIGN_UP_FORM_CHANGE, SIGN_UP_FORM_RESET} from './sign-up-form-action'

const initSignUpFormData = {
    email: '',
    password: '',
    confirm: '',
    errors: {}
}

export default (signUpFormData = initSignUpFormData, {type, payload}) => {
    switch (type) {
        case SIGN_UP_FORM_CHANGE:
            let data = Object.assign({}, signUpFormData, payload)
            if (payload.email) {
                data.errors.email = isEmail(payload.email) ? '' : 'Not an Email'
            }
            if (payload.password) {
                data.errors.password = payload.password.length > 8 ? '' : 'Password Need at least 8 Characters'
            }
            if (payload.confirm) {
                data.errors.confirm = data.password == data.confirm ? '' : 'Not Match'
            }
            return data
        case SIGN_UP_FORM_RESET:
            return initSignUpFormData
        default:
            return signUpFormData
    }
}