## 概要
- 週報システムにおけるサンプルソース、必要最低限の機能しか揃っていない。
- python + flask + sqlarchemy + jinja 等を使用
- 基本的に仮想環境(今回はcent7.2)上で動かすことを想定している、なおホストOSはwindows想定（個人的にはMacが好きなのだが。。。）
- [flaskについてはこちらを参照](https://flask-docs-ja.readthedocs.io/en/latest/)

## vagrantによる環境構築
- vagrant仮想環境作成
	1. 本プロジェクトをクローン(ホストで)
	2. `cd weekly_report/vagrant`
	3. `vagrant up`

- 仮想環境内で行うこと
	1. `cd /home/vagrant/synced-weekly-report`
	2. `pip install -r requirements.txt -r requirements-dev.txt`

- アプリケーション起動（TODO:apache上で動かすようにしようかな。Nginxのほうが簡単かな。）
	1. `cd /home/vagrant/synced-weekly-report/src`
	2. `python main.py`
	3. ホストからブラウザで確認する場合は、5000番でポートフォワードしてるんで`127.0.0.1:5000`でつながるかな。
	
