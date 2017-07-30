
def execute(server, caller, arguments):
    result = caller.get_name() + ': '
    for a in arguments:
        result += str(a) + ' '

    server.send_to_all(result.encode())
    return ''
