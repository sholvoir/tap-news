export const LOGIN_FORM_RESET = 'LOGIN_FORM_RESET'
export const LOGIN_FORM_CHANGE = 'LOGIN_FORM_CHANGE'

export const doLoginFormChange = (loginFormData) => ({
    type: LOGIN_FORM_CHANGE,
    payload: loginFormData
})


export const doLoginFromReset = () => ({
    type: LOGIN_FORM_RESET
})