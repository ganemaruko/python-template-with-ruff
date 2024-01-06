"""LintについてのUtil関数."""
import os.path
import subprocess


def check_lint(target_path: str) -> int:
    """Lintが通ることを確認します.

    もしこのテストがフェイルした場合は、以下を試してください.
    >>> fix_lint()
    """
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pyproject.toml")
    ruff_command = f"ruff check {target_path} --config {config_path}"
    result = subprocess.run(ruff_command, shell=True, capture_output=True, text=True)

    # 結果を表示
    print(f"Standard Output:\n{result.stdout}")
    print(f"Standard Error:\n{result.stderr}")
    return result.returncode


def fix_lint(target_path: str = ".") -> int:
    """Lintを自動修正します."""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pyproject.toml")
    ruff_command = f"ruff check {target_path} --fix --config {config_path}"
    result = subprocess.run(ruff_command, shell=True, capture_output=True, text=True)

    # 結果を表示
    print(f"Standard Output:\n{result.stdout}")
    print(f"Standard Error:\n{result.stderr}")
    return result.returncode


if __name__ == "__main__":
    fix_lint("src/")
