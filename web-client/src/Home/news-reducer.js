import {MORE_NEWS, CLEAR_NEWS} from './news-action'

const initNews = []

export default (news = initNews, action) => {
    switch (action.type) {
        case MORE_NEWS:
            return news.concat(action.payload)
        case CLEAR_NEWS:
            return initNews.concat(action.payload)
        default:
            return news
    }
}