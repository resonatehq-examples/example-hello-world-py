from resonate import Resonate, Context
from typing import Generator, Any

resonate = Resonate.local()


def baz(_: Context, noun: str) -> str:
    return f"Hello {noun} from baz!"


def bar(ctx: Context, noun: str) -> Generator[str, Any, Any]:
    greeting = yield ctx.run(baz, noun=noun)
    return f"Hello {noun} from bar! {greeting}"


@resonate.register
def foo(ctx: Context, noun: str) -> Generator[str, Any, Any]:
    greeting = yield ctx.run(bar, noun=noun)
    return f"Hello {noun} from foo! {greeting}"


def main():
    try:
        promise_id = "hello-world"
        result = foo.run(promise_id, noun="Cully")
        print(result)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
