class VM (object):
    def __init__(self, memSize=102400, numRegs=5):
        self.memSize = memSize
        self.numRegs = numRegs
        self.mem = [0]*memSize
        self.regs = [0]*numRegs
        self.stack = []
        self.ip = 0
        self.ops = [
            self.nop,
            self.load,
            self.move,
            self.swap,
            self.push,
            self.pop,
            self.add,
            self.sub,
            self.mul,
            self.div,
            self.neg,
            self.and_,
            self.or_,
            self.xor,
            self.nand,
            self.nor,
            self.xnor,
            self.not_,
            self.lshift,
            self.rshift,
            self.jump,
            self.jumpe,
            self.jumpne,
            self.jumpt,
            self.jumpf,
        ]

    def nop(self):
        pass

    def load(self, x, a):
        self.regs[a] = x

    def move(self, a, b):
        self.regs[b] = self.regs[a]

    def swap(self, a, b):
        self.regs[a], self.regs[b] = self.regs[b], self.regs[a]

    def push(self, a):
        self.stack.append(self.regs[a])

    def pop(self, a):
        self.regs[a] = self.stack.pop()

    def add(self, a, b, c):
        self.regs[c] = self.regs[a] + self.regs[b]

    def sub(self, a, b, c):
        self.regs[c] = self.regs[a] - self.regs[b]

    def mul(self, a, b, c):
        self.regs[c] = self.regs[a]*self.regs[b]

    def div(self, a, b, c):
        self.regs[c] = self.regs[a]/self.regs[b]

    #def pow(self, a, b, c):
    #    self.regs[c] = self.regs[a]**self.regs[b]

    def neg(self, a, b):
        self.regs[b] = -self.regs[a]

    def and_(self, a, b, c):
        self.regs[c] = self.regs[a] & self.regs[b]

    def or_(self, a, b, c):
        self.regs[c] = self.regs[a] | self.regs[b]

    def xor(self, a, b, c):
        self.regs[c] = self.regs[a] ^ self.regs[b]

    def nand(self, a, b, c):
        self.regs[c] = ~self.regs[a] & ~self.regs[b]

    def nor(self, a, b, c):
        self.regs[c] = ~self.regs[a] | ~self.regs[b]

    def xnor(self, a, b, c):
        self.regs[c] = ~self.regs[a] ^ ~self.regs[b]

    def not_(self, a, b):
        self.regs[b] = ~self.regs[a]

    def lshift(self, a, b, c):
        self.regs[c] = self.regs[a] << self.regs[b]

    def rshift(self, a, b, c):
        self.regs[c] = self.regs[a] >> self.regs[b]

    def jump(self, a):
        self.ip = self.regs[a] - 1

    def jumpe(self, a, b, c):
        if self.regs[a] == self.regs[b]:
            self.ip = self.regs[c]


