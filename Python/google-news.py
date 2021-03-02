from pygooglenews import GoogleNews

gn = GoogleNews(lang = 'pt')
top = gn.top_news()

for item in top['entries']:
    print(item.title)