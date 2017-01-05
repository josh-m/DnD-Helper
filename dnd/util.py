

def roundDownToNearest(num, interval):
    n = int(num)
    return ((n // interval) * interval)

#Attempts to find a name in a list, returning the full_name
def findNameInList(name, ls):
    name_tokens = name.lower().split()
    num_tokens = len(name_tokens)
    if num_tokens < 1:
        return None
    
    #Find initial candidates
    candidates = [c for c in ls
                    if name_tokens[0] in c.lower()] 
    
    #check if each word is within the creature's full name
    for token in name_tokens[1:]:
        candidates = [c for c in candidates
                        if token in c.lower()]
        
    if len(candidates) == 0:
        return None
    elif len(candidates) > 1:
        #if there is an exact match, drop others
        if name.lower() in [c.lower() for c in candidates]:
            found_idx = [c.lower() 
                              for c in candidates].index(name.lower())
            found_name = candidates[found_idx]
        else:
            return candidates
    else:
        found_name = candidates[0]

    return found_name