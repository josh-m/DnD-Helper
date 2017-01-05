
coin_types = ['c','s','e','g','p']

#Represents a quantity of a specific coin type
class Coin():
    def __init__(self, quantity=0, coin='c'):
        self.quantity = quantity
        self.coin = coin
    
    def __str__(self):
        return str(self.quantity)+' '+self.coin+'.p.'
        
    def __bool__(self):
        if self.quantity:
            return True
        else:
            return False
    
    def __lt__(self, other):
        self_base = convertLower(self, 'c')
        other_base = convertLower(other, 'c')
        return self_base.quantity < other_base.quantity
    
    def __le__(self, other):
        return (self.__lt__(other) or self.__eq__(other))
    
    def __eq__(self, other):
        self_base = convertLower(self, 'c')
        other_base = convertLower(other, 'c')
        return self_base.quantity == other_base.quantity
    
    def __ne__(self, other):
        return not(self.__eq__(other))
        
#Wealth is a collection of coins
class Wealth():
    def __init__(self,cp=0,sp=0,ep=0,gp=0,pp=0):
        self.copper = Coin(cp,'c')
        self.silver = Coin(sp,'s')
        self.electrum = Coin(ep,'e')
        self.gold = Coin(gp,'g')
        self.platinum = Coin(pp,'p')
    
    def __bool__(self):
        if (self.copper or self.silver or self.electrum
               or self.gold or self.platinum):
            return True
        else:
            return False

    
    def __str__(self):        
        ret = ''
        if self.copper.quantity: ret += str(self.copper) + ' '
        if self.silver.quantity: ret += str(self.silver) + ' '
        if self.electrum.quantity: ret += str(self.electrum) + ' '
        if self.gold.quantity: ret += str(self.gold) + ' '
        if self.platinum.quantity: ret += str(self.platinum) + ' '
        
        return ret
        
    def __add__(self,other):
        ret = None
        w = Wealth(0,0,0,0,0)
        if isinstance(other,Coin):
            w.addCoins(other)
        elif isinstance(other,Wealth):
            w.addWealth(other)
            w.addWealth(self)
    
        return w
    
    def addWealth(self, other):
        self.addCoins(other.copper)
        self.addCoins(other.silver)
        self.addCoins(other.electrum)
        self.addCoins(other.gold)
        self.addCoins(other.platinum)
    
    def addCoins(self, coins):
        currency = coins.coin
        quantity = coins.quantity
        
        if currency == 'c':
            self.copper.quantity += quantity
        elif currency == 's':
            self.silver.quantity += quantity
        elif currency == 'e':
            self.electrum.quantity += quantity
        elif currency == 'g':
            self.gold.quantity += quantity
        elif currency == 'p':
            self.platinum.quantity += quantity
        else:
            raise TypeError
    
    #returns the base (copper) value of all wealth
    def base_value(self):
        total = self.copper.quantity
        total += (self.silver.quantity * 10)
        total += (self.electrum.quantity * 100)
        total += (self.gold.quantity * 200)
        total += (self.platinum.quantity * 1000)
        
        return total
    
#returns wealth converted to highest value coins
def optimize(wealth):
    copper = wealth.copper.quantity
    silver = wealth.silver.quantity
    electrum = wealth.electrum.quantity
    gold = wealth.gold.quantity
    platinum = wealth.platinum.quantity

    #convert copper
    converted = copper // 1000
    copper = copper % 1000
    platinum += converted
    
    converted = copper // 200
    copper = copper % 200
    gold += converted
    
    converted = copper // 100
    copper = copper % 100
    electrum += converted
    
    converted = copper // 10
    copper = copper % 10
    silver += converted
    
    #convert silver
    converted = silver // 100
    silver = silver % 100
    platinum += converted
    
    converted = silver // 20
    silver = silver % 20
    gold += converted
    
    converted = silver // 10
    silver = silver % 10
    electrum += converted

    #convert electrum
    converted = electrum // 10
    electrum = electrum % 10
    platinum += converted
    
    converted = electrum // 2
    electrum = electrum % 2
    gold += converted
    
    #convert gold
    converted = gold // 5
    gold = gold % 5
    platinum += converted
    
    w = Wealth(copper,silver,electrum,gold,platinum)
    
    return w
        
#Converts a coin currency to a lower currency
def convertLower(coins, out_type='c'):
    if (not coins.coin in coin_types) or (not out_type in coin_types):
        raise ValueError
        
    if coins.coin == out_type:
        return coins
        
    if coin_types.index(coins.coin) < coin_types.index(out_type):
        raise ValueError
    
    #convert to copper
    quantity = coins.quantity
    if (not coins.coin == 'c'):
        if coins.coin == 's':
            quantity *= 10
        elif coins.coin == 'e':
            quantity *= 100
        elif coins.coin == 'g':
            quantity *= 200
        else:
            quantity *= 1000

    #convert to final   
    if out_type == 's':
        quantity /= 10
    elif out_type == 'e':
        quantity /= 100
    elif out_type == 'g':
        quantity /= 200
    elif out_type == 'p':
        quantity /= 1000
    
    return Coin(quantity,out_type)