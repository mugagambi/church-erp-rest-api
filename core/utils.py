import socket

from decouple import config
import xmlrpc.client
import http.client

erp_url = config('ERP_URL', default='http://localhost:8069')
erp_database = config('ERP_DATABASE', default='church_erp')
erp_admin_username = config('ADMIN_USERNAME')
erp_admin_password = config('ADMIN_PASSWORD')


# Authenticate
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(erp_url))
admin_uid = common.authenticate(erp_database, erp_admin_username, erp_admin_password, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(erp_url))
