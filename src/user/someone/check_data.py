"""userフォルダ以下はlint対象外に設定されています。詳しくはpyproject.tomlを参照してください。"""


def check_data():
    with open("some_file.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    check_data()
