#Hannah Fried
#SoftDev
#Helper fxns for Smallpox Stories
#Oct 21 2019
import sqlite3   #enable control of an sqlite database


connector = sqlite3.connect("smallpox.db")
curse = connector.cursor()
curse.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT UNIQUE PRIMARY KEY, Password TEXT);")
curse.execute("CREATE TABLE IF NOT EXISTS stories(Title TEXT UNIQUE PRIMARY KEY, Entries TEXT, Author TEXT);")


def authenticate(username, password):
    return True

def addUser(username, password):
    connector.execute("SELECT name, id FROM students;")

def uniqueUsername(username):
    return True

def getContributedStories(username):
    contributedStories = []
    return contributedStories

def getFullStory(title):
    textEntries = []
    return textEntries

def uniqueTitle(title):
    return True

def addEntry(title, entry):
    connector.execute("SELECT name, id FROM students;")

def getOtherStories(username):
    notContributedStories = []
    return notContributedStories

connector.commit() #save changes
connector.close()  #close database
#Create new table
#c.execute("CREATE TABLE IF NOT EXISTS stu_avg(id integer, avg real);")

#Find each student
#kidList = c.execute("SELECT name, id FROM students;")

#courseList = c.execute("SELECT mark, id FROM courses;")

#gradeTot = 0
#numClasses = 0

#
# for kid in kidList: #For each student
#     print(kid)
#     currentKid=kid[1]
#     for uhClass in courseList: #Check each course
#         currentClass = uhClass[1]
#         if currentClass == currentKid: #To see if it's their grade
#             numClasses+=1
#             gradeTot+=int(uhClass[0]) #Add to average
#     c.execute("INSERT INTO stu_avg VALUES("+str(currentKid)+","+str(gradeTot/numClasses)+");")
#     print(kid[0]+", id "+str(kid[1])+": average "+str(gradeTot/numClasses))
#     gradeTot = 0
#     numClasses = 0 #reset counters
# #q = "yadddad {}".format(Hello)
# def addCourse(code, mark, myid):
#          c.execute("INSERT INTO courses VALUES("+code+","+mark+","+myid+");")
#
#
# #==========================================================
#
# db.commit() #save changes
# db.close()  #close database
