import Keno
import tableOfPayouts


def winPercentBySpots(spots):
    if spots == 1:
        return Keno.kenoHitProb(1, 1)
    elif spots == 2:
        return Keno.kenoHitProb(2, 2)
    elif spots == 3:
        return Keno.kenoHitProb(3, 3) + Keno.kenoHitProb(3, 2)
    elif spots == 4:
        return Keno.kenoHitProb(4, 4) + Keno.kenoHitProb(4, 3) + Keno.kenoHitProb(4, 2)
    elif spots == 5:
        return Keno.kenoHitProb(5, 5) + Keno.kenoHitProb(5, 4) + Keno.kenoHitProb(5, 3)
    elif spots == 6:
        return Keno.kenoHitProb(6, 6) + Keno.kenoHitProb(6, 5) + Keno.kenoHitProb(6, 4) + Keno.kenoHitProb(6, 3)
    elif spots == 7:
        return Keno.kenoHitProb(7, 7) + Keno.kenoHitProb(7, 6) + Keno.kenoHitProb(7, 5) + Keno.kenoHitProb(7,
                                                                                                           4) + Keno.kenoHitProb(
            7, 0)
    elif spots == 8:
        return Keno.kenoHitProb(8, 8) + Keno.kenoHitProb(8, 7) + Keno.kenoHitProb(8, 6) + Keno.kenoHitProb(8,
                                                                                                           5) + Keno.kenoHitProb(
            8, 0)
    elif spots == 9:
        return Keno.kenoHitProb(9, 9) + Keno.kenoHitProb(9, 8) + Keno.kenoHitProb(9, 7) + Keno.kenoHitProb(9,
                                                                                                           6) + Keno.kenoHitProb(
            9, 5) + Keno.kenoHitProb(9, 0)
    elif spots == 10:
        return Keno.kenoHitProb(10, 10) + Keno.kenoHitProb(10, 9) + Keno.kenoHitProb(10, 8) + Keno.kenoHitProb(10,
                                                                                                               7) + Keno.kenoHitProb(
            10, 6) + Keno.kenoHitProb(10, 5) + Keno.kenoHitProb(10, 0)

def ExpectedPayoutBySpots(spots, bet):
    x = 0
    i = 0
    while i <= spots:
        x += (Keno.kenoHitProb(spots, spots - i) * (tableOfPayouts.getPayoutNY(spots, spots - i) * bet - bet))
        i += 1
    return "$" + str(x)
