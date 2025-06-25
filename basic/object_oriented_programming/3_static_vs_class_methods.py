"""
Demonstrating the differences between @staticmethod and @classmethod in Python
"""

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"
    
    @classmethod
    def from_string(cls, date_string):
        """
        Alternative constructor using @classmethod
        - Receives 'cls' parameter
        - Can access class methods and create instances
        - Supports inheritance polymorphism
        """
        try:
            year, month, day = map(int, date_string.split('-'))
            return cls(year, month, day)
        except ValueError:
            raise ValueError(f"Invalid date format: {date_string}")
    
    @classmethod
    def today(cls):
        """
        Another classmethod example - factory method
        - Can access class attributes and methods
        - Useful for creating instances with different logic
        """
        from datetime import datetime
        now = datetime.now()
        return cls(now.year, now.month, now.day)
    
    @staticmethod
    def is_valid_date(date_string):
        """
        Utility function using @staticmethod
        - No access to class or instance
        - Pure function, no side effects
        - Can be called without instantiation
        """
        try:
            year, month, day = map(int, date_string.split('-'))
            return (1900 <= year <= 2100 and 
                   1 <= month <= 12 and 
                   1 <= day <= 31)
        except (ValueError, TypeError):
            return False
    
    @staticmethod
    def days_in_month(year, month):
        """
        Another staticmethod example - pure calculation
        - No class state needed
        - Can be used independently
        """
        if month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            # Simple leap year check
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                return 29
            return 28
        else:
            return 31


class DateTime(Date):
    """
    Demonstrating inheritance with classmethod vs staticmethod
    """
    def __init__(self, year, month, day, hour=0, minute=0, second=0):
        super().__init__(year, month, day)
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def __str__(self):
        return f"{super().__str__()} {self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    @classmethod
    def from_string(cls, date_string):
        """
        Override classmethod - cls refers to DateTime, not Date
        - Polymorphic behavior
        """
        if ' ' in date_string:
            date_part, time_part = date_string.split(' ')
            date_obj = super().from_string(date_part)
            hour, minute, second = map(int, time_part.split(':'))
            return cls(date_obj.year, date_obj.month, date_obj.day, hour, minute, second)
        else:
            # Fall back to parent implementation
            return super().from_string(date_string)


def demonstrate_differences():
    """Showcase the key differences between @staticmethod and @classmethod"""
    
    print("=== @classmethod vs @staticmethod Demonstration ===\n")
    
    # 1. Basic usage
    print("1. Basic Usage:")
    print("-" * 40)
    
    # Using classmethod
    date1 = Date.from_string("2024-01-15")
    print(f"Date from string (classmethod): {date1}")
    
    # Using staticmethod
    is_valid = Date.is_valid_date("2024-01-15")
    print(f"Is valid date (staticmethod): {is_valid}")
    
    # 2. Inheritance demonstration
    print("\n2. Inheritance Behavior:")
    print("-" * 40)
    
    # classmethod respects inheritance
    datetime1 = DateTime.from_string("2024-01-15 14:30:00")
    print(f"DateTime from string (classmethod): {datetime1}")
    
    # staticmethod doesn't change behavior
    is_valid_dt = DateTime.is_valid_date("2024-01-15")
    print(f"DateTime.is_valid_date (staticmethod): {is_valid_dt}")
    
    # 3. Access to class vs no access
    print("\n3. Class Access Demonstration:")
    print("-" * 40)
    
    # classmethod can access class methods
    today_date = Date.today()
    print(f"Today's date (classmethod): {today_date}")
    
    # staticmethod is independent
    days = Date.days_in_month(2024, 2)
    print(f"Days in February 2024 (staticmethod): {days}")
    
    # 4. Error handling
    print("\n4. Error Handling:")
    print("-" * 40)
    
    try:
        invalid_date = Date.from_string("invalid-date")
    except ValueError as e:
        print(f"classmethod error: {e}")
    
    invalid_check = Date.is_valid_date("invalid-date")
    print(f"staticmethod validation: {invalid_check}")
    
    # 5. Performance comparison
    print("\n5. Performance Comparison:")
    print("-" * 40)
    
    import time
    
    # Test classmethod performance
    start = time.time()
    for _ in range(1000):
        Date.from_string("2024-01-15")
    classmethod_time = time.time() - start
    
    # Test staticmethod performance
    start = time.time()
    for _ in range(1000):
        Date.is_valid_date("2024-01-15")
    staticmethod_time = time.time() - start
    
    print(f"classmethod 1000 calls: {classmethod_time:.4f}s")
    print(f"staticmethod 1000 calls: {staticmethod_time:.4f}s")


if __name__ == "__main__":
    demonstrate_differences() 