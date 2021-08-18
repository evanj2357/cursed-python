import itertools

class FizzBuzz:
    def __init__(self):
        self.filter_actions = []

    def add_filter_action(self, fun):
        self.filter_actions.append(fun)

    def __call__(self, start=0, end=100):
        for n in range(start, end):
            filtered = False
            for f in self.filter_actions:
                filtered = f(n) or filtered

            if not filtered:
                print(n)
            else:
                print()

def fizz(n: int) -> bool:
    if n % 3 == 0:
        print("Fizz", end='')
        return True
    else:
        return False

def buzz(n: int) -> bool:
    if n % 5 == 0:
        print("Buzz", end='')
        return True
    else:
        return False

_fizzbuzz = FizzBuzz()
def fizzbuzz(start: _fizzbuzz.add_filter_action(fizz) = 0, end: _fizzbuzz.add_filter_action(buzz) = 100) -> _fizzbuzz:
    fizzbuzz.__annotations__["return"](start, end)

if __name__ == "__main__":
    fizzbuzz()
    # fizzbuzz(0, 100)