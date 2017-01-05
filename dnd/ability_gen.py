from random import randint

def main():
    
    #Player roll: 3 sets of 4d6 drop one roll
    print("\nPlayer Character")
    for i in range(3):
        ability_set = [0] * 6
        for j in range(6):
            stat = 0
            low = 6
            for die in range(4):
                roll = randint(1,6)
                if roll < low:
                    low = roll
                stat += roll
            stat -= low
            ability_set[j] = stat
        ability_set = sorted(ability_set, reverse=True)
        print(ability_set)
        
        #Then allow player to choose desired set, and assign to stats
        
    #General NPC Roll: 3d6, count 1s as 3, 6s as 4
    print("\nGeneral NPC")
    ability_set = [0] * 6
    for i in range(6):
        stat = 0
        for die in range(3):
            roll = randint(1,6)
            if roll == 1:
                roll = 3
            elif roll == 6:
                roll = 4
            stat += roll
            ability_set[i] = stat
    print(ability_set)
    
    #Special NPC / Henchman: 3d6, add +1 to any rolls below 6 in preferred stat
    # considering first stat as the preferred
    print("\nSpecial NPC")
    ability_set = [0] * 6
    
    stat = 0
    for die in range(3):
        roll = randint(1,6)
        if (roll < 6):
            roll += 1
        stat += roll
    ability_set[0] = stat
        
    for i in range(1,6):
        stat = 0
        for die in range(3):
            roll = randint(1,6)
            stat += roll
        ability_set[i] = stat
    
    print(ability_set)
            
    

if __name__ == '__main__':
    main()