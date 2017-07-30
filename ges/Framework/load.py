from Framework.Execution import load_commands


def execute(server, caller, names):
    return load_commands(server, caller, names)
