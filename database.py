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
    cursor.execute('INSERT INTO events (name) VALUES(%s)',name)
    cxn.commit()

def events():
    cursor.execute('SELECT * FROM events')
    entries = cursor.fetchall()
    return entries

def addActivity(event_id, activityName, startTime, endTime):
    stmt = 'INSERT INTO activities (name, startTime, endTime, event_id) VALUES (%s,%s,%s,%s)'
    cursor.execute(stmt,(activityName,startTime,endTime,event_id))
    print cursor._last_executed

def activities():
    cursor.execute('SELECT * FROM activities')
    entries = cursor.fetchall()
    return entries

def addUser(name):
    cursor.execute('INSERT INTO USERS (name) VALUES (%s)',name)

def users():
    cursor.execute('SELECT * FROM users')
    entries = cursor.fetchall()
    return entries

def activitiesInEvent(event_id):
    stmt = 'SELECT * FROM activities WHERE event_id = %s'
    cursor.execute(stmt,event_id)
    entries = cursor.fetchall()
    return entries
