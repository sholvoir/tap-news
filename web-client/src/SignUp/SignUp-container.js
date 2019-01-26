import {connect} from 'react-redux'
import {withRouter} from 'react-router'
import {doSignUpFormChange, doSignUpFormReset} from './sign-up-form-action'
import SignUp from './SignUp'

const SIGN_UP_URL = 'http://' +  window.location.hostname + ':3000' + '/auth/signup'
const LOGIN_PATH = '/login'

const mergeProps = ({email, password, confirm, errors}, {dispatch}, {history, ...rest}) => ({
    email, password, confirm, errors, ...rest,
    onChange: ({target: {value: password}}) => dispatch(loginFormChange({email})),
    onPasswordChage: ({target: {value: password}}) => dispatch(loginFormChange({password})),
    onConfirmChage: ({target: {value: confirm}}) => dispatch(loginFormChange({confirm})),
    onLinkTo: (targer) => history.replace(target),
    onSubmit: () => fetch(new Request(SIGN_UP_URL, {
        method: 'POST',
        headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
        body: JSON.stringify({email, password})
    })).then(res => {
        if (res.status == 200) {
            dispatch(doSignUpFormReset())
            history.replace(LOGIN_PATH)
        } else res.json().then(result => {
            console.log(result)
            const errors = result.errors || {}
            errors.summary = result.message
            dispatch(doSignUpFormChange({errors}))
        })
    })
})

export default withRouter(connect(state => state.signUp, null, mergeProps)(SignUp))