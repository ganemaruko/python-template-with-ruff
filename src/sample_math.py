"""適当なモジュールです."""


def add(x: int, y: int) -> int:
    """この関数は引数で与えられた2つの数値を加算します.

    Notes:
        各セクション(Notes, Args, Returnsなど)の間には空行を入れてください。

    Args:
        x: 1つ目の数値
        y: 2つ目の数値

    Returns:
        int:
    """
    return x + y


if __name__ == "__main__":
    print(add(1, 2))
