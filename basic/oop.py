class PlayerCharacter:
    # class object attribute
    membership = True

    def __init__(self, name):
        if self.membership:
            self.name = name
        else:
            self.name = 'Guest' # instance attribute
    
    def getName(self):
        return self.name    
    
player1 = PlayerCharacter('Peter')
print(player1.getName())
