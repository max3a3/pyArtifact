from pyartifact import Cards


def test_spell_mana(cards):
    assert cards.get("No Accident").mana == 3


def test_card_health(cards):
    assert cards.get("Melee Creep").health == 4


def test_plain_text(cards):
    assert cards.get("Fighting Instinct").plain_text == "Modify a red hero with +1 Attack and +1 Armor."

def test_plain_text_2(cards):
    assert cards.get("Loyal Beast").plain_text == "When Loyal Beast deals battle damage to a unit, modify that unit with -1 Attack."


def test_abilities_data(cards):
    c = cards.get("Aghanim's Sanctum")
    assert len(c.abilities_data) == 1
    assert c.abilities_data[0].cooldown == 1
    assert c.abilities_data[0].type == 'active'
    assert c.abilities_data[0].card_id == 10464

    c = cards.get("Venomancer")
    assert len(c.abilities_data) == 1
    assert c.abilities_data[0].cooldown == 0
    assert c.abilities_data[0].type == 'passive'
    assert c.abilities_data[0].card_id == 10491

    ability = cards.get_by_id(10491)
    assert ability.parent == c

def test_creep_abilities_data(cards):
    creep = cards.filter.type('Creep').named("Satyr Magician")[0]
    ability = cards.get_by_id(creep.abilities_data[0].card_id)
    assert ability.parent == creep

if __name__ == "__main__":
    pass
    test_spell_mana(Cards(limit_sets=["01"]).load_all_sets())
