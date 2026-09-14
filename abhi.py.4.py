# Ganpat bappa moriya
# the conditional exercises

duration_seconds = 210
file_format = "mp4"
audio_synced = True
copyright_flag = False

if copyright_flag or not audio_synced:
    print("Blocked:", "Fix audio sync or copyright issues before rendering")
elif duration_seconds < 30 or duration_seconds > 600 or (file_format !="mp4" and file_format != "mpv"):
    print("Blocked:", "invalid video length and unsupported file format")
    
# The fcb battle arena  .

import random
WIN_STREAK = 0
TOTAL_MONSTERS_DEFEATED = 0
def calculate_attack(base_damage,accuracy_chance,crit_chance):
    """
     Calculates the outcome of a single attack.

    MUST RETURN A TUPLE:
    (final_damage: int, is_crit: bool, is_miss: bool)
    """
    roll = random.randint(1,100)
    if roll > accuracy_chance:
        return 0,False ,True
    elif roll >= crit_chance:
        return base_damage*2,True ,False
    else:
        return base_damage,False,False

def play_turn(player_hp, monster_hp, player_potions, action):
    """
        Executes one turn of combat based on the player's chosen action.
        Returns the updated: (player_hp, monster_hp, player_potions, battle_over)
        """
    battle_over = False

    if action == "attack":
        damage, crit, miss = calculate_attack(20, 80, 20)

        if miss == True:
            print("miss message")
        elif crit == True:
            print("crit message ")
            monster_hp -= damage
        else:
            print("normal hit message")
            monster_hp -= damage

    # checking that the monster defeated

    if monster_hp <=0:
        print("monster defeated")
        battle_over = True
        record_victory()
    return  player_hp, monster_hp, player_potions, battle_over
def record_victory():
    """
    Updates the system-wide win counters when a monster dies.
    """
    global WIN_STREAK , TOTAL_MONSTERS_DEFEATED
    WIN_STREAK += 1
    TOTAL_MONSTERS_DEFEATED += 1
    print(WIN_STREAK)




            
#







