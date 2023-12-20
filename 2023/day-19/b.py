from sys import stdin
from collections import namedtuple, deque
from operator import lt, gt, eq, mul
from functools import reduce


Rule = namedtuple('Rule', ['category', 'operator', 'value', 'next'])
Workflow = namedtuple('Workflow', ['name', 'rules', 'default'])
Interval = namedtuple('Interval', ['lo', 'hi'])
T = namedtuple('T', ['intervals', 'workflow', 'rule_index'])

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
start = T({'x': Interval(1, 4000), 'm': Interval(1, 4000), 'a': Interval(1, 4000), 's': Interval(1, 4000)}, 'in', 0)
q = deque([start])
while len(q) != 0:
    u: T = q.popleft()
    w: Workflow = workflows.get(u.workflow, None)
    if w is None:
        if u.workflow == 'A':
            answer += reduce(mul, (hi - lo + 1 for lo, hi in u.intervals.values()), 1)
        continue

    rule_index = u.rule_index
    if rule_index >= len(w.rules):
        q.append(T(u.intervals, w.default, 0))
        continue

    rule: Rule = w.rules[rule_index]
    category: str = rule.category
    op: str = rule.operator
    value: int = rule.value
    next_workflow: str = rule.next

    i: Interval = u.intervals[category]
    lo: int = i.lo
    hi: int = i.hi
    fn = operator_fns[op]
    if op == '=':
        if value < lo:
            # Whole interval fails, we move to next rule.
            q.append(T(u.intervals, u.workflow, rule_index + 1))
        elif value > hi:
            # Whole interval passes, we move to next workflow.
            q.append(T(u.intervals, next_workflow, 0))
        else:
            # We have to split the interval in three: [lo, value - 1], [value, value] [value + 1, hi].
            # The accepted interval go the next workflow and the two others pass to next rule.
            before = Interval(lo, value - 1)
            after = Interval(value + 1, hi)
            accepted = Interval(value, value)
            d = {k: (accepted if k == category else v) for k, v in u.intervals.items()}
            q.append(T(d, next_workflow, 0))
            if before.lo <= before.hi:
                e = {k: (before if k == category else v) for k, v in u.intervals.items()}
                q.append(T(d, u.workflow, rule_index + 1))
            if after.lo <= after.hi:
                f = {k: (after if k == category else v) for k, v in u.intervals.items()}
                q.append(T(d, u.workflow, rule_index + 1))

    if op == '<':
        if hi < value:
            # Whole interval passes, we move to next workflow.
            q.append(T(u.intervals, next_workflow, 0))
        elif lo > value:
            # Whole interval fails, we move to next rule.
            q.append(T(u.intervals, u.workflow, rule_index + 1))
        else:
            accepted = Interval(lo, value - 1)
            complement = Interval(value, hi)
            if accepted.lo <= accepted.hi:
                d = {k: (accepted if k == category else v) for k, v in u.intervals.items()}
                q.append(T(d, next_workflow, 0))
            e = {k: (complement if k == category else v) for k, v in u.intervals.items()}
            q.append(T(e, u.workflow, rule_index + 1))

    if op == '>':
        if lo > value:
            pass # Whole interval passes
        elif hi < value:
            pass # Whole interval fails
        else:
            accepted = Interval(value + 1, hi)
            complement = Interval(lo, value)
            if accepted.lo <= accepted.hi:
                d = {k: (accepted if k == category else v) for k, v in u.intervals.items()}
                q.append(T(d, next_workflow, 0))
            e = {k: (complement if k == category else v) for k, v in u.intervals.items()}
            q.append(T(e, u.workflow, rule_index + 1))
print(answer)
