import os, sys

users = sys.argv[1]

# Check if users file exists, if not throw error
if os.path.isfile(users):
    userlist = [line.strip() for line in open(users)]
    print(userlist)

else:
    print("Cannot find file specified, please try again.")


