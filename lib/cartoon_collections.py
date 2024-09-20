def roll_call_dwarves(dwarves):
    i = 1
    for dwarf in dwarves:
        print (f"{i}. {dwarf}")
        i+=1

def summon_captain_planet(calls):
    calls_appended = []
    for call in calls:
        
        calls_appended.append(call.title()+"!")
        print(calls_appended)
    return calls_appended
    

def long_planeteer_calls(call_lengths):
    for call in call_lengths:
        if(len(call) < 4):
            return True
        else:
           return False

def find_the_cheese(ingredients):
    desired_ingredients = ['cheddar', 'gouda', 'thyme']
    for ingredient in ingredients:
        print(ingredient)
        if ingredient in desired_ingredients:
            return ingredient
    return None
    
    

ingredients = ['test', 'gouda']
find_the_cheese(ingredients)