#!python3/bin/python3

import os, sys, logging

# Configure logging
## Set logging output level INFO, DEBUG
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
## Create a file handler
handler = logging.FileHandler('output.log')
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)


def loadUsers(users):
    # Check if users file exists, if not throw error
    if os.path.isfile(users):
        logger.info('Reading users from %s', users)
        userlist = [line.strip() for line in open(users)]
        logger.debug('Users: %s', userlist)
        return userlist
    else:
        logger.error("Cannot find file specified %s, please try again.", users, exc_info=True)

def addUserGroup(userlist):
    for user in userlist:
        print(user)

users = sys.argv[1]
userlist = loadUsers(users)
addUserGroup(userlist)
