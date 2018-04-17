export const USER_LOGIN = 'USER_LOGIN'
export const USER_LOGOUT = 'USER_LOGOUT'

export const doUserLogin = (userData) => ({
    type: USER_LOGIN,
    payload: userData
})

export const doUserLogout = () => ({
    type: USER_LOGOUT
})