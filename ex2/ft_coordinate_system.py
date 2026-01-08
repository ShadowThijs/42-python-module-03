import math


def calculate_distance(p1, p2):
    """Calculates Euclidean distance between two 3D points."""
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def parse_coordinates(coord_string):
    """Parses a string 'x,y,z' into a tuple (x, y, z)."""
    try:
        parts = coord_string.split(',')
        if len(parts) != 3:
            raise ValueError("Coordinates must have 3 parts")

        coords = tuple(int(part.strip()) for part in parts)
        return coords
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        return None


def main():
    print("=== Game Coordinate System ===")

    pos1 = (10, 20, 5)
    origin = (0, 0, 0)

    print(f"Position created: {pos1}")
    dist1 = calculate_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round(dist1, 2)}")

    demo_valid_str = "3,4,0"
    print(f'Parsing coordinates: "{demo_valid_str}"')
    parsed_pos = parse_coordinates(demo_valid_str)

    if parsed_pos:
        print(f"Parsed position: {parsed_pos}")
        dist2 = calculate_distance(origin, parsed_pos)
        print(f"Distance between {origin} and {parsed_pos}: {dist2}")

    demo_invalid_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{demo_invalid_str}"')
    parse_coordinates(demo_invalid_str)

    print("Unpacking demonstration:")
    unpack_source = parsed_pos if parsed_pos else (3, 4, 0)

    x, y, z = unpack_source
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
