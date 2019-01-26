def get_summary(news):
    result = ''
    if 'source' in news and news['source']:
        result += news['source'] + '\n'
    if 'author' in news and news['author']:
        result += news['author'] + '\n'
    if 'title' in news and news['title']:
        result += news['title'] + '\n'
    if 'description' in news and news['description']:
        result += news['description'] + '\n'
    if 'url' in news and news['url']:
        result += news['url'] + '\n'
    if 'text' in news and news['text']:
        result += news['text']
    return result