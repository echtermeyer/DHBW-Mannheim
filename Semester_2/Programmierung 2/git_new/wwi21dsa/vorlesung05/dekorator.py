from datetime import datetime
from functools import wraps


def pseudo_logger(func):
    print("decorating")

    def myfuc(*args, **kwargs):
        start = datetime.now()
        print("it's ", str(start))
        res = func(*args, **kwargs)
        print("it took ", datetime.now() - start)
        return res

    print("decorated")

    return myfuc


def timestamp(func):
    print("it's ", str(datetime.now()))
    return func


@pseudo_logger
def hello(name, town="whereever"):
    print(locals())
    print(f"hello {name} from {town}")


@pseudo_logger
def demo(**kwargs):
    print(locals())
    print(kwargs)
    print(
        f"{kwargs.get('name', 'unknown')} from {kwargs.get('town', 'unknown')} in {kwargs.get('country', 'unknown')}"
    )
    big_pict(kwargs.get("continent"))


def big_pict(continent, **kwargs):
    print(continent)


my_funcs = {"ts": timestamp, "greet": hello}

if __name__ == "__main__":
    hello("class")
    hello("class", "DHBW")
    my_funcs["greet"]("Peter")
    #
    demo(name="Peter", town="Monnem")
    # demo(name="Anna", town="Paris", country="FR", continent="Europe")
