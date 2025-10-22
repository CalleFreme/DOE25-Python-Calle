"""
args_kwargs_demo.py

func(*args, **kwargs)

Varför finns dessa?

Hantera funktioner med flexibelt antal argument

Bygg mer återanvändbar och skalbar kod

Vanligt i bibliotek, API:er, loggningsfunktioner

*args

Tar emot ett godtyckligt antal positionella argument

"""
def add_all(*numbers):
    return sum(numbers)
"""

**kwargs

Tar emot godtyckligt antal namngivna argument (dictionary)

"""
def print_user_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")
"""

När ska de användas?

När antalet parametrar inte är bestämt i förväg

Vid konfiguration, logging, plugin-arkitektur

För att skriva generella funktioner

Fallgrop

Överanvänd inte - kan göra koden svårare att förstå om det inte är nödvändigt

På ren svenska:
När används *args? När du inte vet hur många argument.
När används **kwargs? När parametrar är valfria/named/konfigurerbara.

"""

from typing import Any


def greet(greeting, *names):
    """Demonstrates *args: accept any number of positional arguments.

    greet('Hi', 'Alice', 'Bob') -> 'Hi Alice' and 'Hi Bob' printed
    """
    for name in names:
        print(f"{greeting} {name}")

greet("Hej", "Calle", "Anna", "Bob")

def make_config(**kwargs):
    """Demonstrates **kwargs: return a configuration dict with defaults.

    Use kwargs.get('key', default) or combine dicts to supply defaults.
    """
    defaults = {"host": "localhost", "port": 8080}
    # Merge defaults and kwargs; kwargs overrides defaults
    cfg = {**defaults, **kwargs}
    return cfg


def forward_example(a, b, *args, **kwargs):
    """Show pattern for forwarding args/kwargs to another function.

    This is useful when wrapping or decorating functions.
    """
    print("a, b:", a, b)
    print("extra args:", args)
    print("extra kwargs:", kwargs)
    # Forwarding to an imaginary function:
    # return some_other_function(a, b, *args, **kwargs)


class Demo:
    def __init__(self, **kwargs):
        # Store arbitrary settings
        self.settings = kwargs

    def show(self):
        print("Settings:", self.settings)


if __name__ == "__main__":
    print("*args example")
    greet("Hello", "Alice", "Bob", "Charlie")

    print("\n**kwargs example")
    cfg = make_config(port=9090, debug=True)
    print(cfg)

    print("\nForwarding example")
    forward_example(1, 2, 3, 4, key='value')

    print("\nClass with kwargs")
    d = Demo(mode='production', retries=3)
    d.show()
