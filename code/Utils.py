import math
from Main import coerce
import os
import random
import json, re, copy


def rnd(n, nPlaces=3):
    mult = pow(10, nPlaces)
    return math.floor(n * mult + 0.5) / mult


def rand(lo=0, hi=1, Seed=937162211):
    # Seed=937162211
    Seed = (16807 * Seed) % 2147483647
    return lo + (hi - lo) * Seed / 2147483647, Seed


def rint(lo, hi):
    return math.floor(0.5 + rand(lo, hi))


def csv(src, fun):
    if not os.path.isfile(src):
        print("\nfile " + src + " doesn't exists!")
        sys.exit(2)
    with open(src, 'r') as file1:
        for line in file1:
            temp = []
            for j in line.strip().split(','):
                temp.append(coerce(j))
            fun(temp)


def map(src, fun):
    for i in src:
        # print(i)
        fun(i)


def kap(t, fun, u={}):
    u = {}
    for k, v in enumerate(t):
        v, k = fun(k, v)
        if not k:
            u[len(u)] = v
        else:
            u[k] = v
    return u


def cosine(a, b, c):
    if c == 0:
        c = 0.5
    x1 = (a ** 2 + c ** 2 - b ** 2) / (2 * c)
    x2 = max(0, min(1, x1))
    y = math.sqrt(abs(a ** 2 - x2 ** 2))
    return x2, y


def many(t, n, seed=937162211):
    random.seed(seed)
    return random.choices(t, k=n)


def any(t, seed=937162211):
    random.seed(seed)
    return random.choices(t)[0]


def show(node, what=None, cols=None, nPlaces=None, lvl=0):
    if node:
        print("|.. " * lvl + " ", end='')
        # print(node)
        if "left" not in node:
            print(node["data"].rows[-1].cells[-1])
        else:
            print(int(rnd(100 * node['C'])))
        show(None if "left" not in node else node["left"], what, cols, nPlaces, lvl + 1)
        show(None if "right" not in node else node["right"], what, cols, nPlaces, lvl + 1)


def dofile(src):
    json_string = '{'
    if not os.path.isfile(src):
        print("\nfile " + src + " doesn't exists!")
        sys.exit(2)
    with open(src, 'r') as file1:
        next(file1)
        next(file1)
        for line in file1:
            x = line.replace('_', '"_"').replace('=', ':').replace('{', '[').replace('}', ']').replace('\'', '"')
            json_string = json_string + x
    json_string = json_string[:-2] + '}'
    json_string = re.sub('(\w+):', r'"\1":', json_string)
    return json.loads(json_string)


def oo(t):
    td = t.__dict__
    td['a'] = t.__class__.__name__
    td['id'] = id(t)
    print(dict(sorted(td.items())))


def helper(k):
    return "Num" + str(k)


def repcols(cols, Data, the):
    cols = copy.deepcopy(cols)
    for col in cols:
        col[len(col) - 1] = str(col[0]) + ':' + str(col[len(col) - 1])
        for j in range(1, len(col)):
            col[j - 1] = col[j]
    col.pop()
    cols.insert(0, [helper(i) for i in range(len(cols[0]) - 1)])
    cols[0][len(cols[0]) - 1] = "thingX"
    return Data(cols, the)


def transpose(t):
    u = [[None] * len(t) for _ in range(len(t[0]))]
    for r, row in enumerate(t):
        for c, val in enumerate(row):
            u[c][r] = val
    return u


def repRows(t, rows, Data, the):
    rows = copy.deepcopy(rows)
    for j, s in enumerate(rows[-1]):
        rows[0][j] = rows[0][j] + ':' + s
    rows.pop()
    for n, row in enumerate(rows):
        if n == 0:
            row.append("thingX")
        else:
            u = t['rows'][-n+1]
            row.append(u[-1])

    return Data(rows, the)
