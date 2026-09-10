# python3.11のイメージをダウンロード
FROM python:3.11-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってuvをインストール
RUN pip install uv

# uvの定義ファイルをコピー (存在する場合)
COPY pyproject.toml* uv.lock* ./

# uvでライブラリをインストール (pyproject.tomlが既にある場合)
RUN if [ -f pyproject.toml ]; then uv sync; fi

# アプリケーションコードをコピー
COPY api ./api

# uvicornのサーバーを立ち上げる
# デプロイ先の環境によって$PORT環境変数が割り当てられる場合があるため、CMDで動的に設定
CMD uv run uvicorn api.main:app --host 0.0.0.0 --port ${PORT:-8000}