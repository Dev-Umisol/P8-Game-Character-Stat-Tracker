class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1
    
    @property
    def name(self):
        return self._name # Read-only access getter
        
    @property
    def health(self):
        return self._health # Getter
    
    @health.setter
    def health(self, new_health):
        if new_health <= 0:
            new_health = 0 # <-- Sets Health to 0 if user tries and go lower than 0
        elif new_health >= 100:
            new_health = 100 #<-- Sets Health to 100 if user tries and go higher than 10-
        
        self._health = new_health # <-- Sets new_health to whatever number user enters
            
    @property
    def mana(self):
        return self._mana # Getter
    
    @mana.setter
    def mana(self, new_mana):
        if new_mana <= 0:
            new_mana = 0 # <-- Sets Mana to 0 if user tries and go lower than 0
        elif new_mana >= 50:
            new_mana = 50 # <-- Sets Mana to 50 if user tries and go higher than 50
        
        self._mana = new_mana # <-- Sets new_mana to whatever number user enters
            
    @property
    def level(self):
        return self._level # Getter
    
    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self._level}!")
    
    def __str__(self):
        return f"Name: {self._name}\nLevel: {self._level}\nHealth: {self._health}\nMana: {self._mana}\n"
    
hero = GameCharacter("Umisol")
print(hero)

hero.health -= 20
hero.mana -= 5
print(hero)

hero.level_up()
print(hero)