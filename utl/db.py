#Hannah Fried
#SoftDev
#Helper fxns for Smallpox Stories
#Oct 21 2019
import sqlite3   #enable control of an sqlite database


connector = sqlite3.connect("smallpox.db", check_same_thread=False)
curse = connector.cursor()
curse.execute("CREATE TABLE IF NOT EXISTS users(Username TEXT UNIQUE PRIMARY KEY, Password TEXT);")#create table of users with a username and password tab
curse.execute("CREATE TABLE IF NOT EXISTS stories(Title TEXT UNIQUE PRIMARY KEY, Entries TEXT, Author TEXT);")#create stories table with title, entries and author columns

def uniqueTitle(title):#return a boolean for whether or not a given title matches one already in the table.
    repeats = curse.execute("SELECT Title FROM stories;")
    for titleS in repeats:
        if (names[0] == title):
            return False
    return True

def uniqueUsername(username): #return a boolean for whether or not a given username matches one already in the table
    repeats = curse.execute("SELECT Username FROM users;")
    for names in repeats:
        if (names[0] == username):
            return False
    return True

def addUser(username, password):# add a row to the users database, with the given username/passwrd combo. Return nothing.
    curse.execute("INSERT INTO users (Username, Password) VALUES("+username+","+password+");")

def addEntry(title, entry, author):# add a row to the stories database, with the given title/entry/author combo. Return nothing.
    curse.execute("INSERT INTO stories (Title, Entries, Author) VALUES("+title+","+entry+","+author+");")

def authenticate(username, password):#return true if the username/password combo exists within the database, otherwise return false.
    givenUser = (username, password)
    accountTuple = curse.execute("SELECT Password FROM departments WHERE Username = %s;" % username)
    for accounts in accountTuple:
        if (accounts != password):
            return False
        else:
            return True
    #I must change return values to case specific errors at some point

def getContributedStories(username):
    contributedStories = []
    return contributedStories

def getFullStory(title):
    textEntries = []
    return textEntries

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
