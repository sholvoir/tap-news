import {combineReducers} from 'redux'
import {applyNews} from './Home'
import {applyLoginForm} from './Login'
import {applySignUpForm} from './SignUp'
import {applyUserLog} from './Base'

export default combineReducers({
  news: applyNews,
  login: applyLoginForm,
  signUp: applySignUpForm,
  user: applyUserLog
})