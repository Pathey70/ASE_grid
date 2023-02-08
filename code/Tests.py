import sys

import TestEngine
from Sym import Sym
from Num import Num
from Data import Data
from Utils import rnd, csv, rand, show, dofile, repcols, oo, repRows, transpose

tot = 0


def count(t):
    global tot
    tot = tot + len(t)


def eg_check_syms(the):
    """Tests Sym"""
    sym = Sym()
    for x in ["a", "a", "a", "a", "b", "b", "c"]:
        sym.add(x)
    assert 'a' == sym.mid() and 1.379 == rnd(sym.div())


def eg_check_nums(the):
    """Tests Num"""
    num = Num()
    for x in [1, 1, 1, 1, 2, 2, 3]:
        num.add(x)
    assert 11 / 7 == num.mid() and 0.787 == rnd(num.div())


def eg_the(the):
    print(the)
    pass


def eg_repcols(the):
    t = repcols(dofile(the["file"])['cols'], Data, the)
    a = list(map(oo, t.cols.all))
    b = list(map(oo, t.rows))
    pass


def eg_reprows(the):
    t = dofile(the["file"])
    rows = repRows(t, transpose(t['cols']), Data, the)
    a = list(map(oo, rows.cols.all))
    b = list(map(oo, rows.rows))
    pass


def eg_synonyms(the):
    show(repcols(dofile(the["file"])['cols'], Data, the).cluster())
