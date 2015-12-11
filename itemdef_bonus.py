#!/usr/bin/python

from itemdef_itemtype import ItemType

bonus1 = []
# (stat, value_per_level, initial_level)
bonus1.insert(ItemType.MELEE_HEAD,      ("poise",            1, 6))
bonus1.insert(ItemType.RANGED_HEAD,     ("accuracy",         2, 6))
bonus1.insert(ItemType.MENT_HEAD,       ("mp",               3, 6))
bonus1.insert(ItemType.MELEE_CHEST,     ("hp",              25, 2))
bonus1.insert(ItemType.RANGED_CHEST,    ("accuracy",         3, 2))
bonus1.insert(ItemType.MENT_CHEST,      ("mp",               3, 2))
bonus1.insert(ItemType.MELEE_LEGS,      ("poise",            3, 2))
bonus1.insert(ItemType.RANGED_LEGS,     ("avoidance",        3, 2))
bonus1.insert(ItemType.MENT_LEGS,       ("mp",               2, 2))
bonus1.insert(ItemType.MELEE_FEET,      ("poise",            2, 2))
bonus1.insert(ItemType.RANGED_FEET,     ("avoidance",        4, 2))
bonus1.insert(ItemType.MENT_FEET,       ("mp_regen",         1, 2))
bonus1.insert(ItemType.MELEE_HANDS,     ("crit",             1, 2))
bonus1.insert(ItemType.RANGED_HANDS,    ("accuracy",         2, 2))
bonus1.insert(ItemType.MENT_HANDS,      ("mp_regen",         2, 2))
bonus1.insert(ItemType.MELEE_ARTIFACT,  ("hp_regen",        25, 2))
bonus1.insert(ItemType.RANGED_ARTIFACT, ("avoidance",        3, 2))
bonus1.insert(ItemType.MENT_ARTIFACT,   ("mp_regen",         2, 2))
bonus1.insert(ItemType.MELEE_WEAPON,    ("dmg_melee_min",    5, 2))
bonus1.insert(ItemType.RANGED_WEAPON,   ("dmg_ranged_min",   5, 2))
bonus1.insert(ItemType.MENT_WEAPON,     ("dmg_ment_min",     5, 2))
bonus1.insert(ItemType.SHIELD,          ("absorb_max",       1, 2))
bonus1.insert(ItemType.FIRE_RING,       ("fire_resist",      2, 2))
bonus1.insert(ItemType.ICE_RING,        ("ice_resist",       2, 2))
bonus1.insert(ItemType.SHOCK_RING,      ("lightning_resist", 2, 2))
bonus1.insert(ItemType.DARK_RING,       ("dark_resist",      2, 2))
bonus1.insert(ItemType.XP_RING,         ("xp_gain",          1, 2))
bonus1.insert(ItemType.GOLD_RING,       ("currency_find",    2, 2))
bonus1.insert(ItemType.ITEM_RING,       ("item_find",        5, 2))

bonus2 = []
bonus2.insert(ItemType.MELEE_HEAD,      ("",                 0, 0))
bonus2.insert(ItemType.RANGED_HEAD,     ("",                 0, 0))
bonus2.insert(ItemType.MENT_HEAD,       ("",                 0, 0))
bonus2.insert(ItemType.MELEE_CHEST,     ("",                 0, 0))
bonus2.insert(ItemType.RANGED_CHEST,    ("",                 0, 0))
bonus2.insert(ItemType.MENT_CHEST,      ("",                 0, 0))
bonus2.insert(ItemType.MELEE_LEGS,      ("",                 0, 0))
bonus2.insert(ItemType.RANGED_LEGS,     ("",                 0, 0))
bonus2.insert(ItemType.MENT_LEGS,       ("",                 0, 0))
bonus2.insert(ItemType.MELEE_FEET,      ("",                 0, 0))
bonus2.insert(ItemType.RANGED_FEET,     ("",                 0, 0))
bonus2.insert(ItemType.MENT_FEET,       ("",                 0, 0))
bonus2.insert(ItemType.MELEE_HANDS,     ("",                 0, 0))
bonus2.insert(ItemType.RANGED_HANDS,    ("",                 0, 0))
bonus2.insert(ItemType.MENT_HANDS,      ("",                 0, 0))
bonus2.insert(ItemType.MELEE_ARTIFACT,  ("",                 0, 0))
bonus2.insert(ItemType.RANGED_ARTIFACT, ("",                 0, 0))
bonus2.insert(ItemType.MENT_ARTIFACT,   ("",                 0, 0))
bonus2.insert(ItemType.MELEE_WEAPON,    ("dmg_melee_max",    5, 2))
bonus2.insert(ItemType.RANGED_WEAPON,   ("dmg_ranged_max",   5, 2))
bonus2.insert(ItemType.MENT_WEAPON,     ("dmg_ment_max",     5, 2))
bonus2.insert(ItemType.SHIELD,          ("",                 0, 0))
bonus2.insert(ItemType.FIRE_RING,       ("",                 0, 0))
bonus2.insert(ItemType.ICE_RING,        ("",                 0, 0))
bonus2.insert(ItemType.SHOCK_RING,      ("",                 0, 0))
bonus2.insert(ItemType.DARK_RING,       ("",                 0, 0))
bonus2.insert(ItemType.XP_RING,         ("",                 0, 0))
bonus2.insert(ItemType.GOLD_RING,       ("",                 0, 0))
bonus2.insert(ItemType.ITEM_RING,       ("",                 0, 0))

