def dis(price: int, discount: int) -> float:
    result: float = price - (price * discount / 100)
    return round(result, 2)


def main() -> None:
    print(dis(1500, 50))
    print(dis(89, 20))
    print(dis(100, 75))
    

if __name__ == "__main__":
    main()
