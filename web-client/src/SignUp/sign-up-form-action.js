export const SIGN_UP_FORM_CHANGE = 'SIGN_UP_FORM_CHANGE'
export const SIGN_UP_FORM_RESET = 'SIGN_UP_FORM_RESET'

export const doSignUpFormChange = (signUpFormData) => ({
    type: SIGN_UP_FORM_CHANGE,
    payload: signUpFormData
})

export const doSignUpFormReset = () => ({
    type: SIGN_UP_FORM_RESET
})