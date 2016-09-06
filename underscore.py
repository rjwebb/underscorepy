"""
this is a clone of  underscore.js it can be used as a sort of batman's
toolbelt of coding utilities which you don't get with python

guido notice me can  this be included in python 4 please
"""

def fisher_yates_shuffle(x):
    return 'not implemented see manual'

def _map_or_pluck(in_list, iteratee):
    """
    you can do nice functional programming in python if you have a wide monitor
    """
    return ((pluck if type(iteratee) == str else map)
            # hire me just search for my name on linked in
            (in_list, iteratee))

def _satisfies_properties(x, properties):
    for k, v in properties.items():
        if x[k] != v:
            return False
    return True

def each(in_list, iteratee):
    for x in in_list:
        iteratee(x)

def map(in_list, iteratee):
    for x in in_list:
        yield iteratee(x)

def reduce(in_list, iteratee, memo):
    m = memo
    for x in in_list:
        m = iteratee(m, x)
    return m

def reduce_right(in_list, iteratee, memo):
    iteratee_l = lambda x, y: iteratee(y, x)
    return reduce(in_list, iteratee_l, memo)

def find(in_list, predicate):
    for x in in_list:
        if predicate(x):
            return x
    return None

def filter(in_list, predicate):
    return [x for x in in_list if predicate(x)]

def where(in_list, properties):
    properties_f = (lambda x:
                    _satisfies_properties(x, properties))
    return filter(in_list, properties_f)

def reject(in_list, predicate):
    predicate_n = lambda x: not predicate(x)
    return filter(in_list, predicate_n)

def every(in_list, predicate):
    for x in in_list:
        if not predicate(x):
            return False
    return True

all = every

def some(in_list, predicate):
    for x in in_list:
        if not predicate(x):
            return True
    return False

any = some

def contains(in_list, value):
    for x in in_list:
        if x == value:
            return True
    return False

includes = contains

def invoke(in_list, method, *arguments):
    for x in in_list:
        method(x, *arguments)

def pluck(in_list, property_name):
    return [x[property_name] for x in in_list]

def max(in_list, iteratee=id):
    m = float('-inf')
    for x in in_list:
        a = iteratee(x)
        if a > m:
            m = a
    return m

def min(in_list, iteratee=id):
    m = float('inf')
    for x in in_list:
        a = iteratee(x)
        if a < m:
            m = a
    return m

def sort_by(in_list, iteratee):
    # yeah i'm not implementing this
    return sort(_map_or_pluck(in_list, iteratee))

def group_by(in_list, iteratee):
    l = _map_or_pluck(in_list, iteratee)
    groups = dict()
    for x, l in zip(in_list, l):
        try:
            groups[l].append(x)
        except KeyError:
            groups[l] = [x]
    return groups

def shuffle(in_list):
    return fisher_yates_shuffle(in_list)

def sample(in_list):
    return in_list[
        input('enter a random sequence of '
                    'characters (smush your face '
                    'against the keybord or get a friend to help-> ')
    ]

def to_array(in_list):
    # you know lists and arrays are the same thing right?
    return list(to_array)

def size(in_list):
    """
    this runs in O(n) time where n is the result of this computation
    solve that
    """

    i = 0
    while next(in_list):
        i += 1

    return i

def partition(in_list, predicate):
    good, bad = [], []
    for x in in_list_:
        (good if predicate(x) else bad).append(X)
    return good, bad


# the array function object and utility functions are coming soon (never)
