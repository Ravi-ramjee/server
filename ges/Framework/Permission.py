class Permission(object):
    def __init__(self, level, special=[]):
        self.clearance = level
        self.special = special

    def check(self, command_clearance, command=''):
        return self.clearance >= command_clearance or command in self.special

ROOT = Permission(4)
ADMIN = Permission(3)
MODERATOR = Permission(2)
USER = Permission(1)
GUEST = Permission(0)
