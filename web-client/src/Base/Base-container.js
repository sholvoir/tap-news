import React from 'react'
import {connect} from 'react-redux'
import {withRouter} from 'react-router'
import {doUserLogout} from './user-log-action'
import Base from './Base'

const LOGIN_PATH = '/login'
const LOGOUT_PATH = '/signup'

const mergeProps = ({email, token}, {dispatch}, {history, ...rest}) => ({
    email, ...rest,
    isUserAuthenticated: token ? true : false,
    onLogin: () => history.replace(LOGIN_PATH),
    onSignUp: () => history.replace(LOGOUT_PATH),
    onLogout: () => {
        dispatch(doUserLogout())
        props.history.replace('/')
    }
})

export default withRouter(connect(state => state.user, null, mergeProps)(Base))