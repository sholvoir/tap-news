import React from 'react'
import debounce from 'lodash/debounce'
import {connect} from 'react-redux'
import {withRouter} from 'react-router'
import {doMoreNews, doClearNews} from './news-action'
import Home from './Home'

let user = null
let dispatch = null
let page = 0

const loadMoreNews = debounce(() => {
    let news_url = `http://${window.location.hostname}:3000/news/more?user=${user.email}`
    if (page) news_url += `&page=${page}`
    fetch(new Request(encodeURI(news_url), {method: 'GET', headers: {'Authorization': `bearer ${user.token}`}}))
        .then(res => res.json())
        .then(news => {
            page += 1
            dispatch(doMoreNews(news))
        })
}, 1000)

const clearNewsAndFetch = debounce(() => {
    let news_url = `http://${window.location.hostname}:3000/news/clear?user=${user.email}`
    fetch(new Request(encodeURI(news_url), {method: 'GET', headers: {'Authorization': `bearer ${user.token}`}}))
        .then(res => res.json())
        .then(news => {
            page = 1
            dispatch(doClearNews(news))
        })
}, 1000)

let oldScrollY = 0
const handleScroll = () => {
    console.log('scroll..')
    let scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop
    if (scrollY > oldScrollY && window.innerHeight + scrollY >= document.body.offsetHeight + 10) {
        console.log(`scrolling arrive at bottom ${window.innerHeight} ${scrollY} ${document.body.offsetHeight}`)
        loadMoreNews()
    }
    if (scrollY <= oldScrollY && scrollY <=6) {
        console.log(`scrolling arrive at top ${window.innerHeight} ${scrollY} ${document.body.offsetHeight}`)
        clearNewsAndFetch()
    }
    oldScrollY = scrollY
}

window.addEventListener('scroll', handleScroll)
handleScroll()

const mergeProps = (state, dispatchProps, {history, ...rest}) => {
    user = state.user
    dispatch = dispatchProps.dispatch
    return {}
}

export default withRouter(connect(state => state, null, mergeProps)(Home))