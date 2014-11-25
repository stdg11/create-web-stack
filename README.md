create-web-stack
================

Create OpenStack Users, Tenants, Instances and NGINX Reverse Proxy Blocks

Python automation script with the aim to complete below objectives.

 * Import users from csv
 * Add user to openstack-users security group in AD (https://pypi.python.org/pypi/pyad)
 * Create a tenant for user with default quotas
 * Create a ubuntu instance
 * use cloud-init to set password (install packages?)
 * Return instance IP 
 * Write nginx server block
 * Return details of user, instance, block
