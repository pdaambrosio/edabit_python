def stutter(word: str):
    return f'{word[:2]}... {word[:2]}... {word}?'


def main() -> None:
    print(stutter('incredible'))
    print(stutter('enthusiastic'))
    print(stutter('outstanding'))
    

if __name__ == '__main__':
    main()
