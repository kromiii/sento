import os
import sys
from openai import OpenAI

def main(input_text):
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {
            "role": "system",
            "content": "あなたはプロの編集者である。与えられた文章を文法・構文の誤りを修正した上で校正せよ。文末は「だ」または「である」を使うように。"
            },
            {
            "role": "user",
            "content": input_text
            },
        ],
        temperature=1,
        max_tokens=4095,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    # 引数でファイルパスを指定する
    fp = sys.argv[1]
    with open(fp, 'r') as file:
        input_text = file.read()
    result = main(input_text)
    # 結果をファイルに書き込む
    with open(fp, 'w') as file:
        file.write(result)
    print('AIレビューが完了しました。')