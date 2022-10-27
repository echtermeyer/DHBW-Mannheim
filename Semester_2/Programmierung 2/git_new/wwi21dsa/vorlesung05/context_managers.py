from contextlib import contextmanager


class ContextManager:
    def __init__(self, name):
        self.demo = "demo"
        self.name = name
        print(f"Hello, {name}")
        print("init method called")

    def __enter__(self):
        print("enter method called")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("exit method called")
        return True


with ContextManager("Max") as manager:
    print("with statement block")
    raise ValueError("I'm a value error for demo!")


@contextmanager
def print_this():
    print("Entering the context...")
    yield True
    print("Leaving the context...")


with print_this() as pt:
    print("with statement block")

print("halt")
