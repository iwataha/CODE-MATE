# 概要

## 保存対象

- **完成済み**：動作確認済み、またはレビュー済みのコード
- **準完成状態**：他ファイルとの連携状況は未確定だが、  
	単体でおおよそ完成しているコード

## 注意

- このフォルダ内のファイルを直接編集しないこと
	- 編集が必要な場合は開発用ディレクトリで作業を行い、  
		動作確認後に本フォルダへ移動してください
	

## 構成例

- appフォルダ
	アプリケーション本体

- instanceフォルダ
	実行環境依存のファイル保存先
	
	
- run.py
	アプリ起動用エントリポイント
	
- config.py
	設定ファイル / DB URL、Uploadフォルダ設定

## 仮構成

src/
├── app/                        # アプリケーション本体
│   ├── routes/                 # 各画面・機能のルーティング（view関数）
│   │   ├── auth.py             # ログイン・登録など認証関連
│   │   ├── profile.py          # プロフィール編集・登録処理
│   │   └── main.py             # メイン画面・おすすめ表示など
│   │  
│   ├── models/
│   │   └── user.py             # ユーザーモデルなど
│   ├── static/                 # 画像・CSS・JSなど（プロフ画像もここに）
│   │   ├── img/				# デザインに使用する画像は必ずこのフォルダに配置
│   │   └── uploads/            # プロフィール画像など
│   └── templates/              # HTMLテンプレート
│       ├── auth/
│       │   ├── login.html
│       │   ├── register.html
│       │   └── check.html
│       ├── profile/
│       │   ├── profile.html
│       │   └── newprofile.html
│       ├── main/
│       │   └── main.html
│       └── top.html            # トップ画面（ログイン・新規登録リンク）
├── instance/                   # 実行環境依存のファイル
│   └── users.db                # SQLite DB（Flask標準構成に準拠）
├── run.py                      # アプリ起動用エントリポイント
├── config.py                   # 設定ファイル（DB URIやUploadフォルダ設定）
└── requirements.txt            # 依存ライブラリ（Flaskなど）