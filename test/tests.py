# Run with pytest
from src.wiper import *
from math import ceil


def test_inflate_simple():
    min_size = 32768
    sizes = [2, 375, 1056, min_size, 40000]
    source_text = [x * 'x' for x in sizes]
    dest_text = [x * ceil(min_size / x) * 'x' for x in sizes]

    for source, dest in zip(source_text, dest_text):
        assert len(dest) == len(inflate(source))

