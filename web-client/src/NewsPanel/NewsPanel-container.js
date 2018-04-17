import { connect } from 'react-redux'
import NewsPanel from './NewsPanel'

const mergeProps = ({news: newsList, user: {email, token}}, {dispatch}) => ({
    newsList,
    onShowNews: (news) => {
        const url = `http://${window.location.hostname}:3000/news/log?user=${email}&news=${news.digest}`
        fetch(new Request(encodeURI(url), {method: 'POST', headers:{'Authorization': `bearer ${token}`}}))
        window.open(news.url, '_blank')
    }
})

export default connect(state => state, null, mergeProps)(NewsPanel)