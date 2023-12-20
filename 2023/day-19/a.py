from sys import stdin
from collections import namedtuple
from operator import lt, gt, eq


Rule = namedtuple('Rule', ['category', 'operator', 'value', 'next'])
Workflow = namedtuple('Workflow', ['name', 'rules', 'default'])

operator_fns = { '<': lt, '=': eq, '>': gt }


def read_workflows():
    workflows = {}
    for line in stdin:
        stripped = line.strip()
        if len(stripped) == 0:
            break

        chunks = stripped.split('{')
        name = chunks[0]
        remaining = chunks[1][:-1].split(',')
        rules = []
        for rule in remaining[:-1]:
            i = 0
            category = ''
            while rule[i].isalpha():
                category += rule[i]
                i += 1
            operator = rule[i]
            i += 1
            int_literal = ''
            while rule[i].isnumeric():
                int_literal += rule[i]
                i += 1
            nxt = rule[i+1:]
            rules.append(Rule(category, operator, int(int_literal), nxt))
        default = remaining[-1]
        workflows[name] = Workflow(name, rules, default)
    return workflows


def read_parts():
    parts = []
    for line in stdin:
        stripped = ''.join(ch for ch in line.strip() if ch != '{' and ch != '}')
        chunks = stripped.split(',')
        part = {}
        for chunk in chunks:
            a, b = chunk.split('=')
            part[a] = int(b)
        parts.append(part)
    return parts
            

workflows = read_workflows()
parts = read_parts()
answer = 0
for p in parts:
    w = workflows['in']
    while w != 'A' and w != 'R':
        for rule in w.rules:
            fn = operator_fns[rule.operator]
            if fn(p[rule.category], rule.value):
                nxt = rule.next
                w = workflows[nxt] if nxt in workflows else nxt
                break
        else:
            w = workflows[w.default] if w.default in workflows else w.default
    if w == 'A':
        answer += sum(p.values())
print(answer)
