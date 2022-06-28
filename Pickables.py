from Entities import entity, entity_type

FLASK_DUR = 0.75

HPFLASK_HP = 33
MANAFLASK_MANA = 40

class pickable(entity):
    def __init__(self, type, sprite, anim_dur):
        super().__init__(type, sprite, anim_dur)
        self.destroyed = False

    def destroy(self):
        self.destroyed = True
        
    def should_die(self):
        return self.destroyed

class hpflask(pickable):
    def __init__(self):
        from GameSprites import Sprites
        super().__init__(entity_type.hpflask, Sprites["hpflask"], FLASK_DUR)
        self.hp = HPFLASK_HP
        
class manaflask(pickable):
    def __init__(self):
        from GameSprites import Sprites
        super().__init__(entity_type.manaflask, Sprites["manaflask"], FLASK_DUR)
        self.mana = MANAFLASK_MANA

