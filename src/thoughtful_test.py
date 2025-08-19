import math



def is_bulky(volume: int, dimensions: list) -> bool:
    return volume >= 1000000 or any(dimension >= 150 for dimension in dimensions)

def is_heavy(mass: int):
    return mass >= 20

def get_stack_type(volume: int, dimensions: list[int], mass: int) -> str:
    if is_bulky(volume, dimensions) and is_heavy(mass):
        return "REJECTED"
    elif is_bulky(volume, dimensions) or is_heavy(mass):
        return "SPECIAL"
    else:
        return "STANDARD"

def sort(width: int, height: int, lenght: int, mass: int):
    dimensions = [width, height, lenght]
    volume = math.prod(dimensions)

    stack_type = ""

    try:
        stack_type = get_stack_type(volume, dimensions, mass)
    except Exception as err:
        print(f"Could not get stack type, reason: {err}")
    
    return stack_type

"""
TEST CASES
"""
print(sort(100, 100, 100, 19))  # SPECIAL
print(sort(10, 10, 10, 21))     # SPECIAL
print(sort(200, 1, 1, 10))      # SPECIAL
print(sort(200, 200, 200, 25))  # REJECTED
print(sort(10, 10, 10, 10))  # STANDARD