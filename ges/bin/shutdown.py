
def execute(server, caller, arguments):
    if caller.get_permissions().check(3):
        server.shutdown()
        return 'Goodbye.'
    return 'Invalid Permissions!'
