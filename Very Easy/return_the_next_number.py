from typing import Callable

addition: Callable[[int], int] = lambda x: x+1

print(addition(-3))
