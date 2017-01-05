from random import randint

def roll(die, quantity=1, result_mod=0, drop_low=False):
    result = 0
    if not drop_low:
        for i in range(quantity):
            result += randint(1,die)
    else:
        assert(quantity>1)
        low = die
        for i in range(quantity):
            this_roll = randint(1,6)
            if this_roll < low:
                low = this_roll
            result += this_roll
        result -= low

    return (result + result_mod)