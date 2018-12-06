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

    print('item')
    minion = cards.filter.type('Item')
    for m in minion:
        print(f'[{m.sub_type}] {m.name} id({m.id}) {m.plain_text} \n')


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

def list_card(name):
    cards = Cards().load_all_sets()
    card = cards.get(name)
    # if not getattr(card,'mana_cost',0):
    #     card.mana_cost = 0
    # if not getattr(card,'mana_cost','no_color'):

    print(f"id {card.id} ({getattr(card,'color','no_color')}) [{getattr(card,'mana_cost',0)}] {card.type} {card.name}: {card.plain_text}")
    if card.parent:
        print(f"  parent {card.parent}")

    for ab in card.abilities_data:
        if ab.type=='active':
            ab_card = cards.get_by_id(ab.card_id)
            print(f"active: id {ab.card_id} cd:{ab.cooldown} {ab_card} {ab_card.plain_text}")
    if len(card.abilities_data)==0:
        for r in card.references:
            print(
                f"  ref -> id {r.id} ({getattr(r,'color','no_color')}) [{getattr(r,'mana_cost',0)}] {r.type} {r.name}: {r.plain_text}")
    print("\n"*2)
def list_item(name):
    cards = Cards().load_all_sets()
    card = cards.get(name)
    print(f"id {card.id} {card.type} [{card.sub_type}] {card.name}: {card.plain_text}")
    for a in card.abilities_data:
        print(f"  active id {a.card_id} cd:{a.cooldown}")
if __name__ == "__main__":
    # list_classic()
    # list_spell_conditions()
    # active_ability()
    # passive_ability()
    # creep_ability()
    # test_get_multiple()

    # list_card('Crippling Blow')
    # list_card('Cleansing Rite')
    # list_card('Fighting Instinct')
    # list_card('corrosive mist')

    # list_card('heroic resolve')

    # list_item('Short Sword')
    # list_item('Stonehall Pike')
    # list_item('Revtel Signet Ring')

    # list_item('Demagicking Maul')
    # list_item('blade of the vigil')
    # list_item('broadsword')
    # list_item('red mist maul')
    # list_item('blink dagger')

    # list_card('beastmaster')
    # list_card('Call of the Wild')
    # list_card('loyal beast')


    list_card('Ancient Tower')
    #to read card
    # list_card('hip fire')

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

[Accessory] Traveler's Cloak id(3000) Equipped hero has +4 Health. 

[Armor] Leather Armor id(3001) Equipped hero has +1 Armor. 

[Weapon] Short Sword id(3002) Equipped hero has +2 Attack. 

[Consumable] Healing Salve id(3003) Heal a unit 6. 

[Consumable] Fountain Flask id(3004) Fully heal a unit. 

[Consumable] Potion of Knowledge id(3005) Draw a card. 

[Consumable] Town Portal Scroll id(3006) Return an allied hero to the Fountain. 

'''