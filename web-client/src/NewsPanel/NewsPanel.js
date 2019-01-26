import React from 'react'
import PropTypes from 'prop-types'
import Grid from 'material-ui/Grid'
import NewsCard from '../NewsCard'

const NewsPanel = ({newsList, onShowNews}) => newsList.length
    ? <Grid container spacing={8}>{newsList.map((news) =>
        <Grid item xs={12} key={news.digest} onClick={() => onShowNews(news)}>
            <NewsCard news={news}/>
        </Grid>)}
    </Grid>
    : <div>Loading...</div>

NewsPanel.propTypes = {
    newsList: PropTypes.arrayOf(PropTypes.object).isRequired
}

export default NewsPanel
