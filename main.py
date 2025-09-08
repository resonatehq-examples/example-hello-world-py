from resonate import Resonate, Context
from typing import Generator, Any

resonate = Resonate.local()


def baz(_: Context, greetee: str) -> str:
    print("running baz")
    return f"Hello {greetee} from baz!"


def bar(_: Context, greetee: str) -> str:
    print("running bar")
    return f"Hello {greetee} from bar!"


@resonate.register
def foo(ctx: Context, greetee: str) -> Generator[Any, Any, str]:
    print("running foo")
    foo_greeting = f"Hello {greetee} from foo!"
    bar_greeting = yield ctx.run(bar, greetee=greetee)
    baz_greeting = yield ctx.run(baz, greetee=greetee)
    greeting = f"{foo_greeting} {bar_greeting} {baz_greeting}"
    return greeting


def main():
    try:
        promise_id = "hello-world-example"
        result = foo.run(promise_id, greetee="World")
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
