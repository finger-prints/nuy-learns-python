import random


# can't apply if you're full hp or don't have any
def can_apply_potion(hp, num_potions):
    # write here...

    return True


# apply healing to hp and return hp
def apply_potion(hp, healing_amount):
    # write here...

    return hp


# apply dmg to hp and return hp
def apply_attack(hp, dmg):
    # write here...

    return hp


# the last one standing wins
def print_winner(character_hp, enemy_hp):
    # write here...

    return


def prompt_for_action():
    while True:

        # enumerate potential actions
        print("[1] attack")
        print("[2] take a potion")
        print("[3] inspect inventory")
        print("[4] inspect enemy health")

        # get choice
        try:
            choice = int(input("what action do you take? "))
            print()
            if choice > 0 and choice < 5:
                return choice
        except:
            pass

    return choice


def main():

    # initial hp
    character_hp = 100
    enemy_hp = 50

    # character potions
    num_character_potions = 2

    # intro
    print(
        "welcome to the dimmsdale dimmadimmadimmadome, where you will fight to your death"
    )
    print("an enemy approaches...")

    # main loop
    while character_hp > 0 and enemy_hp > 0:

        # character choice
        choice = prompt_for_action()

        # prompt for choices until player takes a "real" action
        while choice != 1 and choice != 2:
            if choice == 3:
                print(f"potions: {num_character_potions}")
            if choice == 4:
                print(f"enemy health: {enemy_hp}")
            choice = prompt_for_action()

        # apply action effects
        if choice == 1:
            enemy_hp = apply_attack(enemy_hp, random.randint(5, 14))
        if choice == 2:
            if can_apply_potion(character_hp, num_character_potions):
                character_hp = apply_potion(character_hp, random.randint(3, 8))
                num_character_potons -= 1
            else:
                print("you spent a turn rummaging around for a non-existent potion...")

        # character receives an attack
        print(f"enemy attacks player... character health: {character_hp}")
        character_hp = apply_attack(character_hp, random.randint(7, 19))

    print_winner(character_hp, enemy_hp)


if __name__ == "__main__":
    main()
