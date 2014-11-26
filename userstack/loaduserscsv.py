import os, logging

def read(users):
    # Check if users file exists, if not throw error
    if os.path.isfile(users):
        logging.info('Reading users from %s', users)
        userlist = [line.strip() for line in open(users)]
        logging.debug('Users: %s', userlist)
        return userlist
    else:
        logging.error("Cannot find file specified, please try again.", exc_info=True)
