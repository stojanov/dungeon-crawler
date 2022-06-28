from Spell import spell, spell_type

FIRESPELL_DURATION = 0.5
FIRESPELL_DPS = 33
FIRESPELL_COST = 40

class firespell(spell):
    def __init__(self, fromplayer):
        from GameSprites import Sprites
        super().__init__(Sprites["firespell"], FIRESPELL_DURATION, spell_type.player if fromplayer else spell_type.enemy)
        self.dps = FIRESPELL_DPS
        self.cost = FIRESPELL_COST
