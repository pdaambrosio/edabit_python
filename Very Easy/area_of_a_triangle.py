def tri_area(base: int, height: int) -> float:
    return base * height / 2


def main() -> None:
    print(tri_area(3, 2))
    print(tri_area(7, 4))
    print(tri_area(10, 10))
    

if __name__ == '__main__':
    main()
