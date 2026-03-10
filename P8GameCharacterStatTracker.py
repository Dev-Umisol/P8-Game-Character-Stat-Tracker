class GameCharacter:
    
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name
        
    @property
    def health(self):
        return self._health # Getter
    
    @health.setter
    def health(self, new_health):
        if min(new_health) <= 0 or max(new_health) >= 100:
            raise ValueError("Health can not be set to 0 or greater than 100")
            
        
    @property
    def mana(self):
        return self._mana # Getter
    
    @mana.setter
    def mana(self, new_mana):
           if self.mana < 0:
               raise ValueError("Mana can not be set to 0")
           
        