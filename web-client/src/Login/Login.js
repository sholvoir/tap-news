import React from 'react'
import PropTypes from 'prop-types'
import Button from 'material-ui/Button';
import TextField from 'material-ui/TextField';
import render from '../LoginSignupRender'

const Login = ({
    classes,
    email,
    password,
    errors,
    signUpPath,
    onEmailChange,
    onPasswordChange,
    toSignUp,
    onLogin
}) => (
    <div className={classes.panel}>
        <div className={classes.title}>Login</div>
        {errors.summary && <div className={classes.error}>{errors.summary}</div>}
        <div>
            <TextField
                className={classes.email}
                error={errors.email ? true : false}
                id="email"
                label="email"
                value={email}
                margin="normal"
                onChange={onEmailChange}
                helperText={errors.email}/>
        </div>
        <div>
            <TextField
                className={classes.password}
                error={errors.password ? true : false}
                id="password"
                label="Password"
                type="password"
                value={password}
                margin="normal"
                onChange={onPasswordChange}
                helperText={errors.password}/>
        </div>
        <div className={classes.rightAlign}>
            <Button variant="raised" color="primary" onClick={onLogin}>Log In</Button>
        </div>
        <div className={classes.rightAlign}>
            New to Top News?
            <Button onClick={toSignUp}>Sign Up</Button>
        </div>
    </div>
)

export default render(Login)