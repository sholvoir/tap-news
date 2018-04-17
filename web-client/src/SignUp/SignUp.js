import React from 'react'
import PropTypes from 'prop-types'
import Button from 'material-ui/Button'
import TextField from 'material-ui/TextField'
import render from '../LoginSignupRender'

const SignUp = ({
    classes,
    email,
    password,
    confirm,
    errors,
    loginPath,
    onChange,
    onSubmit,
    onLinkTo
}, { router }) => (
    <div className={classes.panel}>
        <div className={classes.title}>Sign Up</div>
        {errors.summary && <div className={classes.error}>{errors.summary}</div>}
        <div>
            <TextField
                className={classes.email}
                error={errors.email ? true : false}
                id="email"
                label="email"
                value={email}
                margin="normal"
                onChange={event => onChange({email: event.target.value})}
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
                onChange={event => onChange({password: event.target.value})}
                helperText={errors.password}/>
        </div>
        <div>
            <TextField
                className={classes.password}
                error={errors.confirm ? true : false}
                id="confirm"
                label="Confirm Password"
                type="password"
                value={confirm}
                margin="normal"
                onChange={event => onChange({confirm: event.target.value})}
                helperText={errors.confirm}/>
        </div>
        <div className={classes.rightAlign}>
            <Button variant="raised" color="primary" onClick={onSubmit}>Sign Up</Button>
        </div>
        <div className={classes.rightAlign}>
            Already have an account?
            <Button color="primary" onClick={() => onLinkTo(loginPath)}>Log In</Button>
        </div>
    </div>
)

SignUp.propTypes = {
    email: PropTypes.string,
    password: PropTypes.string,
    confirm: PropTypes.string,
    errors: PropTypes.object,
    onChange: PropTypes.func.isRequired,
    onSubmit: PropTypes.func.isRequired,
    onLinkTo: PropTypes.func.isRequired
}

SignUp.defaultProps = {
    email: '',
    password: '',
    confirm: '',
    errors: {}
}

export default render(SignUp)