# BotPy

このプロジェクトは、Python 製 Discord ボットです。  
`index.py` を実行することで、サーバーへの新規参加者の管理やロール付与、昇格、キックなどをボタン操作やコマンドで行えます。

## 主な機能
- **新規参加者の自動検知と一時ロール付与**
- **管理者向けボタンUIによるロール付与・キック**
- **スラッシュコマンド `/promote` によるゲスト昇格**
- **参加・退出時の通知メッセージ送信**

## 必要条件
- Python 3.x
- ライブラリ: `discord.py`（2.x系推奨）、`numpy`
- `config.json` または `config_t.json`（サーバーIDやロールID等を記載）

## ファイル構成
- `index.py`: メインスクリプト
- `config.json`/`config_t.json`: ボットの設定ファイル（ID類を記載）
- `.gitignore`: 機密ファイル除外設定

## 使い方
1. 必要なライブラリをインストール  
   ```
   pip install discord.py numpy
   ```
2. `config.json` または `config_t.json` を用意し、各種IDを記載
3. 環境変数 `DCTOKEN` または `DCTOKEN_TEST` にBotトークンを設定
4. `index.py` を実行し、起動方法（test/main）を選択

## 注意事項
- サーバーIDやロールIDは Discord 管理画面から取得してください
- 機密情報（トークン等）は `.gitignore` で管理し、公開しないでください

## ライセンス
MIT License