def ht(a: int, b: int, c: int, m: int) -> float:
    HT: float = (a * m) / 2
    return HT


def hk(a: int, b: int, c: int) -> int:
    HK: int = a + b + c
    return HK


def main() -> None:
    print('Háromszög kerülete, területe!')

    a: int = int(input('Adja meg a háromszög egyik oldalát:'))
    b: int = int(input('Adja meg a háromszög másik oldalát:'))
    c: int = int(input('Adja meg a háromszög harmadik oldalát:'))
    m: int = int(input('Adja meg a háromszög magasságát:'))

    terület: float = ht(a, b, c, m)
    kerület: int = hk(a, b, c)
    print(f'A háromszög területe: {terület} cm^2')
    print(f'A háromszög kerülete: {kerület} cm')


if __name__ == '__main__':
    main()
