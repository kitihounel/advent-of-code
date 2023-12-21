from sys import stdin
from collections import deque, namedtuple
from itertools import chain


Pulse = namedtuple('Pulse', ['src', 'dst', 'type'])
queue = deque()


class Module:
    book = {}

    def __init__(self, name, t, output_module_names) -> None:
        self.name = name
        self.type = t
        self.output_module_names = output_module_names
        self.state = False
        self.memory = {}
        type(self).book[name] = self
        self.low_pulse_count = 0


    def add_input(self, name):
        self.memory[name] = 'low'


    @classmethod
    def connect_modules(cls):
        for m in cls.book.values():
            for name in m.output_module_names:
                other = cls.book.get(name)
                other.add_input(m.name)


    @classmethod
    def get(cls, name):
        return cls.book.get(name, None)


    def process(self, pulse):
        if self.type == 'c':
            self._process_as_conjunction(pulse)
        elif self.type == 'f':
            self._process_as_flip_flop(pulse)
        elif self.type == 'b':
            self._process_as_broadcaster(pulse)
        else:
            pass
        if pulse.type == 'low':
            self.low_pulse_count += 1


    def _process_as_broadcaster(self, pulse):
        for name in self.output_module_names:
            queue.append(Pulse(self.name, name, pulse.type))


    def _process_as_flip_flop(self, pulse):
        if pulse.type == 'high':
            return
        self.state = not self.state
        t = 'high' if self.state else 'low'
        for name in self.output_module_names:
            queue.append(Pulse(self.name, name, t))


    def _process_as_conjunction(self, pulse):
        self.memory[pulse.src] = pulse.type        
        t = 'low' if all(v == 'high' for v in self.memory.values()) else 'high'
        for name in self.output_module_names:
            queue.append(Pulse(self.name, name, t))


def get_module_type(s):
    if s == 'broadcaster':
        return 'b'
    ch = s[0]
    return 'f' if ch == '%' else 'c' if ch == '&' else 'o'


def read_input():
    modules = []
    names = set()
    for line in stdin:
        chunks = [s.strip() for s in line.strip().split('->')]
        t = get_module_type(chunks[0])
        name = chunks[0] if t in ('b', 'o') else chunks[0][1:]
        outputs = [s.strip() for s in chunks[1].split(',')]
        modules.append(Module(name, t, outputs))
        names.update(chain([name], outputs))
    return modules, names


modules, names = read_input()
for name in filter(lambda s: Module.get(s) is None, names):
    m = Module(name, 'o', [])
    modules.append(m)
Module.connect_modules()

answer = 0
while True:
    answer += 1
    queue.append(Pulse(None, 'broadcaster', 'low'))
    while len(queue) != 0:
        pulse = queue.popleft()
        m = Module.get(pulse.dst)
        if m is not None:
            m.process(pulse)
    m = Module.get('rx')
    if m.low_pulse_count == 1:
        break
    m.low_pulse_count = 0
print(answer)
