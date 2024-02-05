import glob
import os

if __name__ == '__main__':
    # マークダウンファイルがあるディレクトリ
    directory = 'posts'

    # アルファベット順にソートされたマークダウンファイルのリストを取得
    markdown_files = sorted(glob.glob(os.path.join(directory, '*.md')))

    # 各ファイルを読み込み、その内容を結合
    content = ''
    for md_file in markdown_files:
        with open(md_file, 'r') as file:
            content += file.read() + '\n\n'

    # 結果をoutput.mdに書き出す
    with open('output.md', 'w') as output_file:
        output_file.write(content)