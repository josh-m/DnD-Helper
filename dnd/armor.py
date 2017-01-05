from dnd.currency import Coin

class Armor():
    def __init__(self, name, ac, weight, bulk, base_move, value):

        self.name = name
        self.AC = ac
        self.weight = weight
        self.bulk = bulk
        self.base_move = base_move
        self.value = value
        
plate_field = Armor('Field Plate',2,450,1,9,Coin(2000,'g'))
plate = Armor('Plate Mail',3,450,2,6,Coin(400,'g'))
banded = Armor('Banded Mail',4,350,2,9,Coin(90,'g'))
splint = Armor('Splint Mail',4,400,2,6,Coin(80,'g'))
chain_elf = Armor('Elfin Chain',5,150,0,12,None)
chain = Armor('Chain Mail',5,300,1,9,Coin(75,'g'))
scale = Armor('Scale Mail',6,400,1,6,Coin(45,'g'))
ring = Armor('Ring Mail',7,250,1,9,Coin(30,'g'))
studded = Armor('Studded Leather',7,200,1,9,Coin(15,'g'))
leather = Armor('Leather Armor',8,150,0,12,Coin(5,'g'))
padded = Armor('Padded Armor',8,100,1,9,Coin(4,'g'))

#shield AC applies only to front and offhand side
class Shield():
    def __init__(self, name, block_ac, missile_ac, blocks_round, weight, bulk, value):
       self.name = name
       self.AC = block_ac
       self.AC_missile = missile_ac
       self.blocks_per_round = blocks_round
       self.weight = weight
       self.bulk = bulk
       self.value = value
       
small_shield = Shield('Small Shield',1,1,2,30,0,Coin(15,'g'))
wood_shield = Shield('Small Wooden Shield',1,1,2,50,0,Coin(10,'g'))
large_shield = Shield('Large Shield',1,2,3,100,2,Coin(1,'g'))