import React from 'react'
import { object } from 'prop-types'
import { withStyles } from 'material-ui/styles'
import Grid from 'material-ui/Grid'
import Chip from 'material-ui/Chip'

const styles = {
    newsCard: {
        paddingBottom: '10px'
    },
    imgCol: {
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        overflow: 'hidden'
    },
    introCol: {
        display: 'inline-flex',
        height: '100%',
        width: '100%'
    },
    imgPanel: {
        flexShrink: 0,
        minWidth: '100%',
        maxHeight: '250px',
        objectFit: 'cover'
    },
    introPanel: {
        margin: 'auto 10px',
        textAlign: 'left'
    },
    newsDescription: {
        textAlign: 'left',
        '&>p': {
            fontSize: '18px'
        }
    },
    newsChip: {
        margin: '0 10px',
        fontSize: '18ps'
    }
}

const NewsCard = ({classes, news}) => (
    <Grid container spacing={8}>
        <Grid item xs={4}>
            <div className={classes.imgCol}>
                <img className={classes.imgPanel} src={news.urlToImage} alt="news"/>
            </div>
        </Grid>
        <Grid item xs={8}>
            <div className={classes.introCol}>
                <div className={classes.introPanel}>
                    <h4>{news.title}</h4>
                    <div className={classes.newsDescription}>
                        <p>{news.description}</p>
                        <div>
                            {news.source && <Chip className={classes.newsChip} label={news.source} />}
                            {new Date(news.publishedAt).getDate() == new Date().getDate() && 
                                <Chip className={classes.newsChip} label='today' />}
                        </div>
                    </div>
                </div>
            </div>
        </Grid>
    </Grid>
)

/*{news.reason && <Chip className={classes.newsChip} label={news.reason} />}*/

NewsCard.propTypes = {
    news: object.isRequired
}

export default withStyles(styles)(NewsCard)
