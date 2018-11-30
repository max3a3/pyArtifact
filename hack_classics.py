from pyartifact import Cards


def list_classic():
    cards = Cards(limit_sets=["00"]).load_all_sets()

    minion = cards.filter.type('Creep')
    for m in minion:
        print(f'{m.type} {m.name} id({m.id}) atk({m.attack}) arm({m.armor}) health({m.health})')

    print('hero')
    minion = cards.filter.type('Hero')
    for m in minion:
        print(f'{m.type} {m.name}  {m.color} id({m.id}) atk({m.attack}) arm({m.armor}) health({m.hit_points})')
        includes_ = m.includes[0]
        print(f'signature id({includes_.id}){includes_}\n')
    print('spell')
    minion = cards.filter.type('Spell')
    for m in minion:
        print(f'{m.name} id({m.id}) mana({m.mana})\n {m.plain_text} \n')


def list_spell_conditions():
    cards = Cards().load_all_sets()

    spell = cards.get('Fighting Instinct')
    print(f'{spell.id} {spell.text}')

    spell = cards.get('Fight Through The Pain')
    print(f'{spell.id} {spell.text}')

    spell = cards.get('Double Edge') #10292
    print(f'{spell.id} {spell.text}')


    spell = cards.get('Gank')
    print(f'{spell.id} {spell.text}')

    spell = cards.get("Allseeing One's Favor")
    print(f'{spell.id} {spell.text}')

def active_ability():
    cards = Cards(limit_sets=["01"]).load_all_sets()
    hero = cards.filter.type('Improvement').named("Aghanim's Sanctum")[0]
    print(hero.type, hero.active_abilities)  #this is retrieved as a property get from card._references

    text = "<span style='font-weight:bold;color:#ffffff;'>Active 1:</span> Fully restore your tower's Mana."
    cool_down = 1

    ability = cards.get_by_id(10464) #"Fully restore your tower's Mana"
    print(ability.text)


    print(hero.abilities_data)

    for ab in hero.abilities_data:
        if ab.type=='active':
            ab_card = cards.get_by_id(ab.card_id)
            print(ab_card,ab_card.text)


def passive_ability():
    cards = Cards(limit_sets=["01"]).load_all_sets()
    hero = cards.get('Venomancer')
    abilities = hero.abilities_data
    print(hero,abilities)
    print(hero.abilities_data)

    hero = cards.get('Treant Protector')
    abilities = hero.abilities_data
    print(hero.id, hero,abilities)
    print(hero.text)
    print(hero.abilities_data)

    ability_card = cards.get_by_id(hero.abilities_data[0].card_id)
    print("treant ability_card.parent",ability_card.parent)

def creep_ability():
    cards = Cards(limit_sets=["01"]).load_all_sets()
    creep = cards.filter.type('Creep').named("Satyr Magician")[0]
    abilities = creep.abilities_data
    print(creep.id,creep,abilities)
    print(creep.abilities_data)

    ability_card = cards.get_by_id(creep.abilities_data[0].card_id)
    print("ability_card.parent",ability_card.parent)

if __name__ == "__main__":
    # list_classic()
    # list_spell_conditions()
    # active_ability()
    # passive_ability()
    creep_ability()
    # test_get_multiple()
'''
Melee Creep id(1006) atk(2) arm(0) health(4)
Zombie id(1009) atk(2) arm(0) health(2)
Prowler Vanguard id(4002) atk(0) arm(0) health(6)
hero
Farvhan the Dreamer id(4000) atk(4) arm(0) health(10)
signature id(4002)Prowler Vanguard

Keefe the Bold id(4003) atk(6) arm(1) health(11)
signature id(4004)Fighting Instinct

Debbi the Cunning id(4005) atk(7) arm(0) health(5)
signature id(4007)No Accident

J'Muy the Wise id(4008) atk(3) arm(0) health(8)
signature id(4010)Battlefield Control

spell
Fighting Instinct id(4004) mana(5)   #modify effect happen only on battle
 Modify a red hero with +1 Attack and +1 Armor.  #IS MODIFY A BUFF? or one action

No Accident id(4007) mana(3)  #spell action that deal damage happen right away
 Deal 3 damage to a unit. 

Battlefield Control id(4010) mana(1)
 Choose a unit. Choose a combat target for it. 



'''