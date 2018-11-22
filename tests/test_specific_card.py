from pyartifact import Cards


def test_get_spell_parent(cards):
    c = cards.filter.type('Spell').named('Frostbite')[0]
    assert c.parent.name == 'Crystal Maiden'


def test_filter_creep(cards):
    minion = cards.filter.type('Creep')
    c = minion.named('Satyr Magician')[0]

    ability = c.active_abilities[0]

    assert ability.type == 'Ability'
    assert ability.name == 'Satyr Magician'


if __name__ == "__main__":
    pass
    # test_get_multiple()

    # test_filter_minion()
    # test_get_ability(Cards(limit_sets=["01"]).load_all_sets())
    test_filter_creep(Cards(limit_sets=["01"]).load_all_sets())
    # test_get_multiple_default(Cards().load_all_sets())
