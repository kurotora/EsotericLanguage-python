# -*- coding: utf-8 -*-

class Counter:
    """
    >>> c = Counter(4); c.inc(); c.inc(); c.value
    6
    """

    def __init__(self, ini):
        self._value = ini

    def inc(self):
        self._value += 1

    @property
    def value(self):
        return self._value

if __name__ == "__main__":
    import doctest
    doctest.testmod()
