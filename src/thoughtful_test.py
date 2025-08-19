import math



def is_bulky(volume: int, dimensions: list) -> bool:
    return volume >= 1000000 or any(dimension >= 150 for dimension in dimensions)

def is_heavy(mass: int) -> bool:
    return mass >= 20

def get_stack_type(volume: int, dimensions: list[int], mass: int) -> str:
    if is_bulky(volume, dimensions) and is_heavy(mass):
        return "REJECTED"
    elif is_bulky(volume, dimensions) or is_heavy(mass):
        return "SPECIAL"
    else:
        return "STANDARD"

def sort(width: int, height: int, lenght: int, mass: int) -> str:
    if width <= 0:
        raise ValueError("width should be a positive number")
    if height <= 0:
        raise ValueError("height should be a positive number")
    if lenght <= 0:
        raise ValueError("lenght should be a positive number")
    if mass <= 0:
        raise ValueError("mass should be a positive number")

    dimensions = [width, height, lenght]
    volume = math.prod(dimensions)
    stack_type = ""

    try:
        stack_type = get_stack_type(volume, dimensions, mass)
    except Exception as err:
        print(f"Could not get stack type, reason: {err}")

    return stack_type
