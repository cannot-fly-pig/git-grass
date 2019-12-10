from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="git-grass",

    version='1.0.0', # バージョン

    license='MIT', # ライセンス

    install_requires=["beautifulsoup4","requests"], # pip installする際に同時にインストールされるパッケージ名をリスト形式で指定

    entry_points={
            "console_scripts": [
                "git-glass = app:main"
            ]
    },

    author='cannot-fly-pig', # パッケージ作者の名前
    author_email='document.sabakan@gmail.com', # パッケージ作者の連絡先メールアドレス

    url='https://github.com/cannot-fly-pig/git-grass', # パッケージに関連するサイトのURL(GitHubなど)

    description='You can see git contribution on comannd line', # パッケージの簡単な説明
    long_description=long_description, # PyPIに'Project description'として表示されるパッケージの説明文
    long_description_content_type='text/markdown', # long_descriptionの形式を'text/plain', 'text/x-rst', 'text/markdown'のいずれかから指定
    keywords='git-grass', # PyPIでの検索用キーワードをスペース区切りで指定

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ], # パッケージ(プロジェクト)の分類。https://pypi.org/classifiers/に掲載されているものを指定可能。
)
