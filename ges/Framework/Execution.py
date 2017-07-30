import imp

command_cache = {}


def run_command(server, caller, name, arguments):
    try:
        return command_cache[name].execute(server, caller, arguments)
    except KeyError:
        return 'Invalid Command.'


def correct_path(server, path):
    return server.path + path.replace('..', '') + '.py'


def load_commands(server, caller, names):
    if not caller.get_permissions().check(3):
        return 'Invalid Permissions.'
    result = ''
    for name in names:
        path = correct_path(server, name)
        try:
            command_cache[name] = imp.load_source(name, path)
            result += 'Loaded ' + name + '\n'
        except Exception as err:
            result += 'Unable to load ' + name + ' because ' + str(err) + '\n'
    return result + 'Complete!'

command_cache['load'] = imp.load_source('load', 'Framework/load.py')