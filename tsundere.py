#!/usr/bin/env python3
"""把正经话翻译成傲娇体。

一个纯好玩的小工具：给输入的一句话加上傲娇口吻，便于做测试数据、文案草稿或聊天玩梗。
"""
import argparse
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


def tsundere(text: str, seed: int | None = None, use_filler: bool = True) -> str:
    """把一句正经话改写成傲娇体。

    Args:
        text: 输入的一句话。
        seed: 随机种子，传入后输出可复现。
        use_filler: 是否在句首插入语气词。

    Returns:
        改写后的一行文本。
    """
    if seed is not None:
        random.seed(seed)
    body = text.strip().rstrip("。！？!?")
    filler = random.choice(FILLER) if use_filler else ""
    return random.choice(PREFIX) + filler + body + random.choice(SUFFIX)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="把正经话翻译成傲娇体")
    parser.add_argument("text", nargs="+", help="要说的话")
    parser.add_argument("--seed", type=int, default=None, help="随机种子，用于复现输出")
    parser.add_argument("--no-filler", action="store_true", help="不插入语气词")
    args = parser.parse_args(argv)

    print(tsundere(" ".join(args.text), seed=args.seed, use_filler=not args.no_filler))
    return 0


if __name__ == "__main__":
    sys.exit(main())
