import itertools
import collections

def eat(seq, n=None):
    if n is None:
        collections.deque(seq, maxlen=0)
    else:
        next(itertools.islice(seq, n, n), None)
        
def group_k_forward(seq, lookahead=1, end_padding=None):
    safe_seq = seq
    if not (end_padding is None):
        safe_seq = itertools.chain(
            seq, 
            itertools.repeat(end_padding, lookahead)
        )
        
    context = itertools.tee(safe_seq, lookahead + 1)
    for i in range(lookahead + 1):
        eat(context[i], i)
    return zip(*context)

