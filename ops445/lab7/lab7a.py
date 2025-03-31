#!/usr/bin/env python3

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
    """
    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string"""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def sum_times(t1, t2):
    """Add two time objects and return the sum."""
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second

    # Carry over seconds to minutes
    if sum.second >= 60:
        sum.minute += sum.second // 60  # Add the carryover to minutes
        sum.second = sum.second % 60  # Keep only the remainder of seconds

    # Carry over minutes to hours
    if sum.minute >= 60:
        sum.hour += sum.minute // 60  # Add the carryover to hours
        sum.minute = sum.minute % 60  # Keep only the remainder of minutes

    # Optional: Ensure hours do not exceed 24 (if that's part of the requirement)
    if sum.hour >= 24:
        sum.hour = sum.hour % 24  # Wrap around if the hour exceeds 24

    return sum

def valid_time(t):
    """Check for the validity of the time object attributes:
       24 > hour >= 0, 60 > minute >= 0, 60 > second >= 0 """
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.minute >= 60 or t.second >= 60 or t.hour >= 24:
        return False
    return True
