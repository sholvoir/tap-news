import {USER_LOGIN, USER_LOGOUT} from './user-log-action'

const TOKEN = '____TOKEN----____'
const EMAIL = '____EMAIL----____'

const initUserData = {
    email: localStorage.getItem(EMAIL),
    token: localStorage.getItem(TOKEN)
}

export default (userData = initUserData, action) => {
    switch (action.type) {
        case USER_LOGIN:
            localStorage.setItem(EMAIL, action.payload.email)
            localStorage.setItem(TOKEN, action.payload.token)
            return Object.assign({}, userData, action.payload)
        case USER_LOGOUT:
            localStorage.removeItem(TOKEN)
            localStorage.removeItem(EMAIL)
            return {}
        default:
            return userData
    }
}