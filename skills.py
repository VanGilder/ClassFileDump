def charge(player, enemy):
    damage = player['attack'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Charge! {enemy['name']} took {damage} damage!"

def defend(player):
    player['defense'] *= 1.5
    return f"{player['name']} used Defend! Defense increased!"

def fireball(player, enemies):
    damage = player['magic'] * 1.2
    for enemy in enemies:
        enemy['hp'] -= damage
    return f"{player['name']} used Fireball! All enemies took {damage} damage!"

def teleport(player, location):
    player['location'] = location
    return f"{player['name']} used Teleport! Moved to {location}!"

def stealth(player):
    player['stealthed'] = True
    return f"{player['name']} used Stealth! Became invisible!"

def backstab(player, enemy):
    if player.get('stealthed', False):
        damage = player['attack'] * 3
        enemy['hp'] -= damage
        return f"{player['name']} used Backstab! {enemy['name']} took {damage} damage!"
    else:
        return f"{player['name']} tried to use Backstab but wasn't stealthed!"

def heal(player):
    healing = player['magic']
    player['hp'] += healing
    return f"{player['name']} used Heal! Restored {healing} HP!"

def smite(player, enemy):
    damage = player['magic'] * 1.5
    enemy['hp'] -= damage
    return f"{player['name']} used Smite! {enemy['name']} took {damage} damage!"

def bow_shot(player, enemy):
    damage = player['ranged_attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Bow Shot! {enemy['name']} took {damage} damage!"

def find_path(player):
    player['shortcuts_found'] += 1
    return f"{player['name']} used Find Path! Discovered a shortcut!"

def bless(player, ally):
    ally['attack'] *= 1.2
    ally['defense'] *= 1.2
    return f"{player['name']} used Bless! {ally['name']}'s attack and defense increased!"

def meditate(player):
    player['hp'] += 10
    player['mana'] += 10
    return f"{player['name']} used Meditate! Restored 10 HP and 10 Mana!"

def punch(player, enemy):
    damage = player['attack']
    enemy['hp'] -= damage
    return f"{player['name']} used Punch! {enemy['name']} took {damage} damage!"

def sing(player, allies):
    for ally in allies:
        ally['attack'] *= 1.1
        ally['defense'] *= 1.1
    return f"{player['name']} used Sing! All allies' attack and defense increased!"

def inspire(player, allies):
    for ally in allies:
        ally['attack'] *= 1.2
        ally['defense'] *= 1.2
    return f"{player['name']} used Inspire! All allies' attack and defense significantly increased!"

def shield_bash(player, enemy):
    enemy['stunned'] = True
    return f"{player['name']} used Shield Bash! {enemy['name']} is stunned!"

