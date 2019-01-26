import {withStyles} from 'material-ui/styles'

const styles = {
    panel: {
        margin: '50px auto',
        width: '40%',
        minWidth: 300,
        maxWidth: 400,
        '&>div': {
            margin: '20px 0'
        }
    },
    title: {
        textAlign: 'center',
        fontSize: '1.2em',
        fontWeight: 'bold'
    },
    error: {
        paddingLeft: '20px',
        color: 'red'
    },
    email: {
        width: '100%'
    },
    password: {
        width: '100%'
    },
    rightAlign: {
        textAlign: 'right'
    }
}

export default withStyles(styles)