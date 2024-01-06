from lint import fix_lint


def test_lint():
    """Lintが通ることを確認するテスト.

    もしこのテストがフェイルした場合は、以下を試してください。
        1. 自動修正の適用

            from lint import fix_lint
            fix_lint()

        2. 1.で修正されない場合、ルールの詳細を確認
            - https://docs.astral.sh/ruff/rules/
    """
    result = fix_lint("src/")
    assert result == 0
