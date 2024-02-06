# 京都銭湯巡り

## フォルダ構成

```
.
├── ai_reviewer.py // AIによる校正を行うスクリプト
├── assets
│   |── output.md  // 組本の出力先
|   |── cover.jpg  // 表紙画像
|   └── ddconv.yml // 組本の設定ファイル
├── concat.oy      // 組本を作成するスクリプト
├── posts          // 組本の個別の内容を保存するディレクトリ
└── README.md
```

## 組本

[でんでんコンバータ](https://conv.denshochan.com/)を使って、組本を作成します。

設定は `ddconv.yml` に記述します。

個別の内容は `posts/` 以下にMarkdownファイルとして保存します。

でんでんコンバータに渡す用のファイルは

```
python concat.py
```

で生成します。

## AIによる校正

環境変数 `OPENAI_API_KEY` にOpenAIのAPIキーを設定することでAIによる校正を行うことができます。

```
python ai_reviewer.py "3-1.md"
```

以下のようにワイルドカードを指定して複数のファイルを一括で校正することができます。

```
python ai_reviewer.py "3*.md"
```

校正したファイルは `git diff` で確認し、問題がなければコミットします。