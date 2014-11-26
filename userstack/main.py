#!python3/bin/python3

import sys, logging
import loaduserscsv


def main():
    #Configure Logging
    logging.basicConfig(filename='output.log', level=logging.DEBUG)
    logging.info('Started')
    users = sys.argv[1]
    userlist = loaduserscsv.read(users)
    addUserGroup(userlist)
    logging.info('Finished')

def addUserGroup(userlist):
    for user in userlist:
        print(user)

if __name__ == '__main__':
    main()
