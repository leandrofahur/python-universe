class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name, age):
        if self.membership and age > 18:
            self._name = name
            self._age = age
        else:
            self._name = 'Guest' # instance attribute
            self._age = None
        
    def getName(self):
        return self._name    
    
    def getAge(self):
        return self._age
    
    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)
    
    @staticmethod
    def adding_things2(num1, num2):
        return num1 + num2
    
player1 = PlayerCharacter('Peter', 10)
print(player1.getName())
print(player1.getAge())

print(PlayerCharacter.adding_things(12, 13))
print(PlayerCharacter.adding_things2(2, 3))
