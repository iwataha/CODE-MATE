# 概要

![CODEMATE Logo](app/static/img/logo.png)

## 保存対象

- **完成済み**：動作確認済み、またはレビュー済みのコード
- **準完成状態**：他ファイルとの連携状況は未確定だが、  
  単体でおおよそ完成しているコード

## 注意

- このフォルダ内のファイルを直接編集しないこと
  - 編集が必要な場合は開発用ディレクトリで作業を行い、  
  動作確認後に本フォルダへ移動してください

- 編集・新規作成したファイルをリモートで追加する場合は`new_file`へ追加してください

## 構成

src_v0.1/
├── app/
│   ├── models/           ← モデル
│   ├── routes/           ← Blueprint別ルート
│   └── static/           ← CSS・画像・アップロードフォルダ
│
├── template/             ← HTMLテンプレート群
│   ├── auth/
│   ├── chat/
│   ├── main/
│   └── profile/
│
├── instance/             ← users.db
├── config.py             ← 設定ファイル
├── run.py                ← アプリ起動
├── README.md

