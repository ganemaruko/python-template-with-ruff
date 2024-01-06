# python-template-with-ruff

高速なlinter [Ruff](https://docs.astral.sh/ruff/) の設定が入ったPythonのテンプレートになります。

- 推奨されるlintの設定
- Ruffを実行するutil関数
- lint検査対象となるサンプルコード
- ignoreフォルダの例

などが入っています

このドキュメントやdocstringなどに日本語を使っていますが、文字コードに振り回されることになるので英語推奨です。(
例えばruffの`--show-files`
オプションを使うときに日本語が入っているとエンコードエラーが起きます。)

動作検証はWindowsで行っているため、他のOSでは動作しない可能性があります。

## Getting started

### 1. リポジトリのクローン

```shell
git clone git@github.com:ganemaruko/python-template-with-ruff.git
```

### 2. 外部モジュールのインストール

```shell
pip install -r requirements.txt
```

### 3. ruffのチェック

src以下の適当なファイルを編集して、`check_lint`が動作するかを確認してください。