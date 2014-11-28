# Import Environment Variables, this is required for authenticating against Keystone and is more secure than hard coding
# You should source your ADMIN-openrc.sh file
from os import environ as env
import keystoneclient.v2_0.client as ksclient
import keystoneclient.v2_0.tenants as kstenants

keystone = ksclient.Client(auth_url=env['OS_AUTH_URL'],
        username=env['OS_USERNAME'],
        password=env['OS_PASSWORD'],
        tenant_name=env['OS_TENANT_NAME'])

# Store Auth token for later use
auth_ref = keystone.auth_ref

def createTenants(userlist):
    for user in userlist:
        kstenants.TenantManager.create(user,auth_ref)
        print("Created tenant: ", user)
