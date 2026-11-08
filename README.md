# tsundere-speak

把一句正经话，翻译成傲娇体。

一个纯好玩的小工具，用来给聊天、文案、测试数据加点情绪色彩。

## 安装

只需要 Python 3.9+，无第三方依赖。

```bash
git clone https://github.com/NotFatJustRound/tsundere-speak.git
cd tsundere-speak
```

## 用法

```bash
python3 tsundere.py "今天辛苦了"
```

输出示例：

```
哼，今天辛苦了…才、才不是特意说给你听的。
```

固定输出（方便测试）：

```bash
python3 tsundere.py --seed 42 "报告写完了"
```

## 作为库调用

```python
from tsundere import tsundere

print(tsundere("会议改到下午三点"))
```

## 可配置项

| 参数 | 说明 |
| --- | --- |
| `--seed` | 固定随机种子，输出可复现 |
| `--no-filler` | 不插入语气词，语气更简洁 |

也可以在代码里直接改 `PREFIX` / `SUFFIX` / `FILLER` 三个列表，换成自己的词汇。

## 边界

- 只做语气改写，不做语义翻译
- 不处理多句长文本，一句输入对一句输出
- 不做敏感词过滤，正式场景请自行检查输出

## License

MIT
