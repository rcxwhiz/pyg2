def input_range(low: int, high: int, message: str = 'Option: ') -> int:
    answer = -100
    retry = ''
    while answer < low or answer > high:
        try:
            answer = int(input(message + retry))
        except ValueError:
            pass
        retry = f'({low}-{high}) '
    return answer
