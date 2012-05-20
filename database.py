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

def addActivity(event_id, activityName, startTime, endTime):
    stmt = 'INSERT INTO activities (name, startTime, endTime, event_id) VALUES ("'
    stmt += activityName + '", "'
    stmt += startTime + '", "'
    stmt += endTime + '", ' + str(event_id) + ')'
    print stmt
    cursor.execute(stmt)

def activities():
    cursor.execute('SELECT * FROM activities')
    entries = cursor.fetchall()
    return entries

def addOneActivity():
    addActivity(1, 'liquid nitrogen ice cream', '2012-04-20 04:20', '2012-04-20 05:20')
