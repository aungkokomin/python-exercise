import itertools
from typing import Iterable,List

def clamp(value: int, low_val: int, high_val:int) -> int:
    """
    Clamp `value` into the inclusive range [low_val, high_val].

    Examples
    --------
    >>> clamp(7, 0, 5)
    5
    >>> clamp(-1, 0, 5)
    0
    >>> clamp(3, 0, 5)
    3
    """
    return max(low_val,min(value, high_val))

def chunks(sequence: Iterable, size: int) -> Iterable[List]:
    """
    Yield lists of length `size` (last may be shorter) from `sequence`.

    Examples
    --------
    >>> list(chunks([1, 2, 3, 4, 5], 2))
    [[1, 2], [3, 4], [5]]

    Works with any iterable (e.g., range):
    >>> list(chunks(range(5), 3))
    [[0, 1, 2], [3, 4]]

    Empty input:
    >>> list(chunks([], 3))
    []

    Size larger than input:
    >>> list(chunks([1, 2], 10))
    [[1, 2]]

    Strings iterate character-by-character:
    >>> list(chunks("abc", 2))
    [['a', 'b'], ['c']]
    """
    it = iter(sequence)
    while True:
        chunk = list(itertools.islice(it, size))
        if not chunk:
            break
        yield chunk
    return chunk