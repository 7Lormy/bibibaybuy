# первая
def chunk_split(items, sz):
    i = 0
    total = len(items)
    while i < total:
        yield items[i:i + sz]
        i += sz

# вторая
def flat_iter(nested):
    queue = [nested]
    while queue:
        cur = queue.pop()
        if isinstance(cur, (list, tuple)):
            if isinstance(cur, (str, bytes)):
                yield cur
            else:
                queue.extend(reversed(cur))
        else:
            yield cur

# третья (не правильно)
bad = [[None] * 3] * 3

# третья (правильно)

good = [[None for _ in range(3)] for _ in range(3)]

# четвертая

def uniq_ordered(seq):
    memo = {}
    res = []
    for val in seq:
        if val not in memo:
            memo[val] = True
            res.append(val)
    return res

