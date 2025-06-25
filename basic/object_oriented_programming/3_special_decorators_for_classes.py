# @classmethod when:
# - Creating alternative constructors
# - Need access to class attributes
# - Want inheritance polymorphism

# @staticmethod when:
# - Pure utility functions
# - No need for class/instance access
# - Performance is critical

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        # Can access cls and create instances        
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    
    @staticmethod
    def is_valid_date(date_string):
        # Pure utility function, no class access needed
        try:
            year, month, day = map(int, date_string.split('-'))
            return 1 <= month <= 12 and 1 <= day <= 31
        except:
            return False
        

