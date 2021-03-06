#!python3/bin/python3

import sys, logging
import loaduserscsv, keystone


def main():
    #Configure Logging
    logging.basicConfig(filename='output.log', level=logging.DEBUG)
    logging.info('Started')
    users = sys.argv[1]
    userlist = loaduserscsv.read(users)
    print(userlist[1])
    keystone.createTenants(userlist)
    logging.info('Finished')


if __name__ == '__main__':
    main()
