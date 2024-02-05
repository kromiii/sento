# 京都銭湯巡り

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
``

以下のようにワイルドカードを指定して複数のファイルを一括で校正することができます。

```
python ai_reviewer.py "3*.md"
```

校正したファイルは `git diff` で確認し、問題がなければコミットします。