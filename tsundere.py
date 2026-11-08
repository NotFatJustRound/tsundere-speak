#!/usr/bin/env python3
"""把正经话翻译成傲娇体。

哼，才、才不是特意给你写的呢。
"""
import random
import sys

PREFIX = ["哼，", "哼！", "……", ""]

SUFFIX = [
    "…才、才不是特意说给你听的。",
    "…你、你别想太多啊。",
    "…这不代表什么哦。",
    "…反正我也不在乎。",
]

FILLER = ["那个，", "就是，", "唔……"]


def tsundere(text: str, seed: int | None = None) -> str:
    """正经话 → 傲娇话。"""
    if seed is not None:
        random.seed(seed)
    body = text.strip().rstrip("。！？!?")
    out = random.choice(PREFIX) + random.choice(FILLER) + body + random.choice(SUFFIX)
    return out


def main() -> None:
    if len(sys.argv) < 2:
        print("用法: python3 tsundere.py \"要说的话\"", file=sys.stderr)
        sys.exit(1)
    print(tsundere(" ".join(sys.argv[1:])))


if __name__ == "__main__":
    main()
