import React from 'react'
import PropTypes from 'prop-types'
import {withStyles} from 'material-ui/styles'
import {Switch, Route, Redirect} from 'react-router-dom'

import AppBar from 'material-ui/AppBar'
import Toolbar from 'material-ui/Toolbar'
import Button from 'material-ui/Button'
import IconButton from 'material-ui/IconButton'
import Typography from 'material-ui/Typography'
import MenuIcon from 'material-ui-icons/Menu'

import Home from '../Home'
import Login from '../Login'
import SignUp from '../SignUp'

const styles = {
    base: {
        textAlign: 'center',
        margin: '0 10px'
    },
    bar: {
        flexGrow: 1
    },
    title: {
        flex: 1,
        textAlign: 'left'
    },
    bold: {
        fontWeight: 'bold'
    }
}

const Base = ({classes, isUserAuthenticated, email, onLogin, onLogout, onSignUp}) => (
    <div className={classes.base}>
        <AppBar position="static">
            <Toolbar className={classes.bar}>
                <IconButton color="inherit" aria-label="Menu">
                    <MenuIcon/>
                </IconButton>
                <Typography variant="title" color="inherit" className={classes.title}>
                    Top News
                </Typography>
                {
                    isUserAuthenticated ? [
                        <Typography key="email" variant="button" color="inherit" className={classes.bolder}>{email}</Typography>,
                        <Button key="logout" color="inherit" className={classes.bolder} onClick={onLogout}>Log Out</Button>
                    ] : [ 
                        <Button key="login" color="inherit" className={classes.bolder} onClick={onLogin}>Log in</Button>,
                        <Button key="signup" color="inherit" className={classes.bolder} onClick={onSignUp}>Sign Up</Button>
                    ]
                }
            </Toolbar>
        </AppBar>
        <Switch>
            <Route exact path="/" render={() => isUserAuthenticated ? <Home/> : <Redirect to="/login"/>}/>
            <Route path="/login" component={Login}/>
            <Route path="/signup" component={SignUp}/>
        </Switch>
    </div>
)

export default withStyles(styles)(Base)
