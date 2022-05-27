from __future__ import absolute_import
from __future__ import print_function
import csv
import sys,json

import duo_client
from six.moves import input

argv_iter = iter(sys.argv[1:])
def get_next_arg(prompt):
    try:
        return next(argv_iter)
    except StopIteration:
        return input(prompt)


admin_api = duo_client.Admin(
    ikey=get_next_arg('Admin API Integration Key ("DI....."): '),
    skey=get_next_arg('Integration Secret Key: '),
    host=get_next_arg('API Hostname ("api-....duosecurity.com"): '),
)
username = input('Enter the username which has to be deleted from the Org : ')
print("Fetching user information for ",username)
try:
    user_data = admin_api.get_users_by_name(username)
# Retrieve user info from API:
    userdata = user_data[0]
    userid = userdata['user_id']
    print("The user id for ",username," is : ",userid)
    admin_api.delete_user(userid)
    print("User ",username, " with user_id ", userid, "is deleted from DUO Org")
except:
    print("Error Fetching user details for ",username, " and hence could not be deleted. Pilease delete it manually")
