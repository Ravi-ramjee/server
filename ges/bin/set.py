
def execute(server, caller, args):
    if args[0] == 'name':
        name = args[1]
        caller.attributes['name'] = name
        return 'Name set to: ' + name + '.'
    return 'Invalid command!'
