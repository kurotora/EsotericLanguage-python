# -*- coding: utf-8 -*-

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

