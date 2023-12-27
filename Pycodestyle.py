#!/usr/bin/python3

import math
import datetime

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        raise ValueError("Radius cannot be negative")

    return math.pi * radius ** 2

class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def calculate_age(self):
        """
        Calculate the age of the person.

        Returns:
            int: The age of the person.
        """
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today.month < self.birthdate.month or (today.month == self.birthdate.month and today.day < self.birthdate.day):
            age -= 1

        return age

if __name__ == "__main__":
    print("Enter the radius of the circle:")
    radius = float(input())

    area = calculate_circle_area(radius)

    print(f"The area of the circle is: {area:.2f}")

