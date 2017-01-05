from random import randint

class Fortress():
    def __init__(self):
        f_size, self.f_type = determineFortressSizeAndType()
        self.population = determineFortressPopulation(f_size)
        
    def __str__(self):
        return '{} populated by {}'.format(self.f_type, self.population)
        
def determineFortressSizeAndType():
    r = randint(1,100)
    
    if r < 36:
        f_size = 'Small'
        if r < 11:
            f_type = 'Small Shell Keep'
        elif r < 26:
            f_type = 'Tower'
        else:
            r = randint(1,2)
            if r == 1:
                f_type = 'Moat House'
            else:
                f_type = 'Friary'
    elif r < 81:
        f_size = 'Medium'
        if r < 46:
            f_type = 'Large Shell Keep'
        elif r < 66:
            f_type = 'Small Walled Castle with Keep'
        else:
            f_type = 'Medium Walled Castle with Keep'
    else:
        f_size = 'Large'
        if r < 89:
            f_type = 'Concentric Castle'
        elif r < 96:
            f_type = 'Large Walled Castle with Keep'
        else:
            f_type = 'Fortress Complex'
    
    return [f_size, f_type]
    
def determineFortressPopulation(f_size):
    r = randint(1,100)
    if f_size == 'Small':
        if r < 46: population = 'Deserted'
        elif r < 61: population = 'Monsters'
        elif r < 71: population = 'Humans'
        else: population = 'Characters'
    elif f_size == 'Medium':
        if r < 31: population = 'Deserted'
        elif r < 51: population = 'Monsters'
        elif r < 66: population = 'Humans'
        else: population = 'Characters'    
    else:
        if r < 16: population = 'Deserted'
        elif r < 41: population = 'Monsters'
        elif r < 61: population = 'Humans'
        else: population = 'Characters'
        
    if population == 'Humans':
        r = randint(1,100)
        if r < 26: population = 'Bandits'
        elif r < 86: population = 'Brigands'
        elif r < 98: population = 'Berserkers'
        else: population = 'Dervishes'

    return population