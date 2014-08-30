# -*- coding: utf-8 -*-

class HQ9Plus:
    """
    >>> HQ9Plus("HQ+H").run()
    Hello, world!
    HQ+H
    Hello, world!
    """

    def __init__(self, src):
        self.src = src
        self.count = 0

    def run(self):
        for c in self.src:
            if c == 'H':
                self.__hello()
            elif c == 'Q':
                self.__printSource()
            elif c == '9':
                self.__print99BottleOfBeer()
            elif c == '+':
                self.__increment()

    def __hello(self):
        print("Hello, world!")

    def __printSource(self):
        print(self.src)

    def __print99BottleOfBeer(self):
        for k in range(99, -1, -1):
            if k == 0:
                before = "no more bottles"
                after = "99 bottles"
            elif k == 1:
                before = "1 bottle"
                after = "no more bottles"
            elif k == 2:
                before = "2 bottles"
                after = "1 more bottles"
            else:
                before = "{0} bottles".format(k)
                after = "{0} more bottles".format(k)

            if k == 0:
                action = "Go to the store and buy some more"
            else:
                action = "Take one down and pass it around"

            print("{0} of beer on the wall, {1} of beer.".format(before.capitalize(), before))
            print("{0}, {1} of beer on the wall".format(action, after))
            if k == 0:
                print("")

    def __increment(self):
        self.count += 1

if __name__ == "__main__":
    # import doctest
    # doctest.testmod()

    import sys
    text = ""
    try:
        with open(sys.argv[1]) as f:
            for l in f:
                text += l
    except:
        for l in sys.stdin.readlines():
            text += l
    HQ9Plus(text).run()

