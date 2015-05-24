import urllib
import time
import web

def get_poster(id, url):
    pic = urllib.urlopen(url).read()
    file_name = 'poster/%d.jpg' % id
    f = file(file_name, "wb")
    f.write(pic)
    f.close()

db = web.database(dbn='sqlite', db='MovieSite.db')
movies = db.select('movie')
count = 0
for movie in movies:
    get_poster(movie.id, movie.image)
    count += 1
    print count, movie.title
    time.sleep(2)
