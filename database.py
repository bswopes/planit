import sqlite3

c = sqlite3.connect("data.db").cursor()

def init():
    c.execute("create table people (username, userID)")
    c.execute("create table events (eventname, eventID, description, start, end)")
    c.execute("create table activities (activityname, activityID, description, start, end, hashtag)")
    c.execute("create table friendships (userID1, userID2)")
    c.execute("create table plans (userID, eventID)")
    c.execute("create table intents (userID, activityID)")
    

def 
