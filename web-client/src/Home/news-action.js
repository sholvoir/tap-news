export const MORE_NEWS = 'MORE_NEWS'
export const CLEAR_NEWS = 'CLEAR_NEWS'

export const doMoreNews = (news) => ({
    type: MORE_NEWS,
    payload: news
})

export const doClearNews = (news) => ({
    type: CLEAR_NEWS,
    payload: news
})