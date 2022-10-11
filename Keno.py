import math
import tableOfPayouts


def kenoHitProb(spots, hits):
    # exceptions
    if spots < hits:
        raise Exception("Hits must be less than spots")
    if not isinstance(spots, int):
        raise Exception("Must input Integer")
    if not isinstance(hits, int):
        raise Exception("Must input Integer")

    # calculations
    permu = (math.perm(20, hits) * math.perm(20, 20 - hits)) / math.perm(20, 20)
    x = 1
    i = 0
    j = 0
    while i < spots:
        if i < hits:
            x *= ((spots - i) / (80 - i))
        else:
            x *= (61-(spots-hits) + j) / (80 - i)
            j += 1
        i += 1

    finalProb = permu * x

    return finalProb


def winPercentBySpots(spots):
    if spots == 1:
        return kenoHitProb(1, 1)
    elif spots == 2:
        return kenoHitProb(2, 1) + kenoHitProb(2, 2)
    elif spots == 3:
        return kenoHitProb(3, 3) + kenoHitProb(3, 2)
    elif spots == 4:
        return kenoHitProb(4, 4) + kenoHitProb(4, 3) + kenoHitProb(4, 2)
    elif spots == 5:
        return kenoHitProb(5, 5) + kenoHitProb(5, 4) + kenoHitProb(5, 3)
    elif spots == 6:
        return kenoHitProb(6, 6) + kenoHitProb(6, 5) + kenoHitProb(6, 4) + kenoHitProb(6, 3)
    elif spots == 7:
        return kenoHitProb(7, 7) + kenoHitProb(7, 6) + kenoHitProb(7, 5) + kenoHitProb(7, 4) + kenoHitProb(7, 3)
    elif spots == 8:
        return kenoHitProb(8, 8) + kenoHitProb(8, 7) + kenoHitProb(8, 6) + kenoHitProb(8, 5) + kenoHitProb(8, 4)
    elif spots == 9:
        return kenoHitProb(9, 9) + kenoHitProb(9, 8) + kenoHitProb(9, 7) + kenoHitProb(9, 6) + kenoHitProb(9, 5) + kenoHitProb(9, 4)
    elif spots == 10:
        return kenoHitProb(10, 10) + kenoHitProb(10, 9) + kenoHitProb(10, 8) + kenoHitProb(10, 7) + kenoHitProb(10, 6) + kenoHitProb(10, 5) + kenoHitProb(10, 0)
    elif spots == 11:
        return kenoHitProb(11, 11) + kenoHitProb(11, 10) + kenoHitProb(11, 9) + kenoHitProb(11, 8) + kenoHitProb(11, 7) + kenoHitProb(11, 6) + kenoHitProb(11, 5) + kenoHitProb(11, 0)
    elif spots == 12:
        return kenoHitProb(12, 12) + kenoHitProb(12, 11) + kenoHitProb(12, 10) + kenoHitProb(12, 9) + kenoHitProb(12, 8) + kenoHitProb(12, 7) + kenoHitProb(12, 6) + kenoHitProb(12, 0)


def ExpectedPayoutBySpots(spots, bet):
    x = 0
    i = 0
    while i <= spots:
        x += (kenoHitProb(spots, spots - i) * (tableOfPayouts.getPayout(spots, spots - i) * bet - bet))
        i += 1
    return "$" + str(x)