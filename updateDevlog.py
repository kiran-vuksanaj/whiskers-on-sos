# Matthew Chan (PM), Hannah Fried, Coby Sontag, Jionghao Wu [Team SOS]
# SoftDev1 pd2
# P00 -- Da Art of Storytellin'
# 2019-10-28

import datetime # used to get the current date and time

# opens the devlog first as read to see if a newline is needed between entries
f = open('doc/devlog.txt', 'r')
if (f.read()[-1] == '\n'):
    needNewLine = False
else:
    needNewLine = True


# opens the devlog as append to add the new entry
f = open('doc/devlog.txt', 'a')

# takes in name of user submitting the entry
fullName = input('Input your full name: ')
# formats the name correcty assumeing a format of "first last"
formattedName = fullName.split(' ')[1].lower() + fullName.split(' ')[0][0].capitalize()

# takes in the entry using \n as newlines
entry = input('Input your devlog entry (use \\n for new lines):\n')
# translates "\n" to actual newline characters
entry = entry.replace('\\n', '\n')

print('\n')
print('Inputted entry:')
print(entry)
if (input('Confirm entry [y/n]: ') == 'y'): # confirms if entry is correct
    if (needNewLine): # adds newline if necessary
        f.write('\n')
    f.write('\n')
    f.write(formattedName + ' -- ') # adds name
    f.write(datetime.datetime.now().strftime('%Y-%m-%d %H:%M')) # adds current date
    f.write('\n')
    f.write(entry) # adds entry
    print('Entry Successful')
else:
    print('Entry Cancelled')

f.close()