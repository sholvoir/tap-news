import React from 'react'
import {withStyles} from 'material-ui/styles'
import logo from './logo.svg'
import NewsPanel from '../NewsPanel'

const styles = {
    logo: {
        display: 'block',
        margin: '0 auto 20px auto',
        paddingTop: '30px',
        width: '20%'
    }
}

const Home = ({classes}) => <div>
    <img className={classes.logo} src={logo}/>
    <NewsPanel/>
</div>

export default withStyles(styles)(Home)
