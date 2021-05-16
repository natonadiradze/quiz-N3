import requests
import json
import sqlite3

conn = sqlite3.connect('ghibliapi.sqlite')
c = conn.cursor()

c.execute('''CREATE TABLE anime

(id INTEGER PRIMARY KEY AUTOINCREMENT,
title VARCHAR(50),
director VARCHAR(100),
release_date FLOAT);''')

curl = 'https://ghibliapi.herokuapp.com/films/58611129-2dbc-4a81-a72f-77ddfc1b1b49'
r = requests.get(curl)
res = r.json()

with open('ghibli.json', 'w')as f:
    json.dump(res, f,  indent=4)

a_id = '58611129-2dbc-4a81-a72f-77ddfc1b1b49'
a_title = 'My Neighbor Totoro'
a_director = 'Hayao Miyazaki'
a_release_date = 1988
c.execute('INSERT INTO anime (id, title, director, release_date) VALUES (?, ?, ?, ?)', (a_id, a_title, a_director, a_release_date))
conn.commit()
#შევქმენი ცხრილი anime და შევინახე ჩემთვის სასურველი ინფორმაცია მასში(id, title, director, release_date

print(r.status_code)
print(r.headers)
res = json.loads(r.text)
print(json.dumps(res, indent=4))
print(f'title is:  {res["title"]}')
print(f'description: \n{res["description"]}')
print(f'release date: {res["release_date"]}')



