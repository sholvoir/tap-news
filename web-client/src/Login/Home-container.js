import {connect} from 'react-redux'
import {withRouter} from 'react-router'
import {doUserLogin} from '../Base'
import {doLoginFormChange, doLoginFromReset} from './login-form-action'
import Login from './Login'

const LOGIN_URL = 'http://' +  window.location.hostname + ':3000' + '/auth/login'
const SIGN_UP_PATH = '/signup'

const mergeProps = ({email, password, errors}, {dispatch}, {history, ...rest}) => ({
    email, password, errors, ...rest,
    onEmailChange: ({target: {value: email}}) => dispatch(doLoginFormChange({email})),
    onPasswordChange: ({target: {value: password}}) => dispatch(doLoginFormChange({password})),
    toSignUP: () => history.replace(SIGN_UP_PATH),
    onLogin: () => {
        fetch(new Request(LOGIN_URL, {
            method: 'post',
            headers: {'Accept': 'application/json', 'Content-Type': 'application/json'},
            body: JSON.stringify({email, password})
        })).then(res => {
            if (res.status === 200) {
                dispatch(doLoginFromReset())
                res.json().then(({token}) => {
                    dispatch(doUserLogin({email, token}))
                    history.replace('/')
                })
            } else {
                console.log('Login Failed!')
                res.json().then(result => {
                    const errors = result.errors || {}
                    errors.summary = result.message
                    dispatch(doLoginFormChange({errors}))
                })
            }
        })
    }
})

export default withRouter(connect(state => state.login, null, mergeProps)(Login))