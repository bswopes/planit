import sqlite3

db = 'data.db'
cxn = sqlite3.connect(db)
cursor = cxn.cursor()

def init():
    c.execute("create table people (username, userID)")
    c.execute("create table events (eventname, eventID, description, start, end)")
    c.execute("create table activities (activityname, activityID, description, start, end, hashtag)")
    c.execute("create table friendships (userID1, userID2)")
    c.execute("create table plans (userID, eventID)")
    c.execute("create table intents (userID, activityID)")
    
def addEvent(name): 
    cursor.execute('INSERT INTO events (name) VALUES("' + name + '")')
    cxn.commit()

def events():
    cursor.execute('SELECT * FROM events')
    entries = cursor.fetchall()
    return entries
