from Framework.Permission import *


def execute(server, caller, args):
    if args[0] == 'admin' and args[1] == open('bin/password.txt').read():
        caller.permission = ADMIN
        caller.attributes['name'] = 'ADMIN'
        return 'Logged in as ADMIN.'
    return 'Invalid login!'
