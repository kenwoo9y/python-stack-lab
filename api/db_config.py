import os
from urllib.parse import urlparse
from urllib.parse import urlunparse


def normalize_database_url(url: str) -> str:
    """
    データベース接続URLをSQLAlchemyの非同期ドライバー形式に正規化する。

    Args:
        url: データベース接続URL

    Returns:
        正規化されたデータベース接続URL

    Examples:
        - postgres://user:pass@host:5432/db -> postgresql+asyncpg://user:pass@host:5432/db
        - postgresql://user:pass@host:5432/db -> postgresql+asyncpg://user:pass@host:5432/db
    """
    parsed = urlparse(url)
    scheme = parsed.scheme.lower()

    # 既に正しい形式の場合はそのまま返す
    if "+asyncpg" in scheme:
        return url

    # PostgreSQLの正規化
    if scheme in ("postgres", "postgresql"):
        # postgres://またはpostgresql://をpostgresql+asyncpg://に変換
        new_scheme = "postgresql+asyncpg"
        normalized = urlunparse((new_scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, parsed.fragment))
        return normalized

    # その他のスキームはそのまま返す（既に正しい形式の可能性がある）
    return url


def _build_database_url_from_env() -> str:
    """
    環境変数からデータベース接続URLを構築する（内部関数）。

    Returns:
        データベース接続URL

    Raises:
        ValueError: 必要な環境変数が設定されていない場合
    """
    DB_HOST = os.getenv("DB_HOST")
    if DB_HOST is None:
        raise ValueError("DB_HOST environment variable is not set")

    DB_PORT = os.getenv("DB_PORT")
    if DB_PORT is None:
        raise ValueError("DB_PORT environment variable is not set")

    DB_NAME = os.getenv("DB_NAME")
    if DB_NAME is None:
        raise ValueError("DB_NAME environment variable is not set")

    DB_USER = os.getenv("DB_USER")
    if DB_USER is None:
        raise ValueError("DB_USER environment variable is not set")

    DB_PASSWORD = os.getenv("DB_PASSWORD")
    if DB_PASSWORD is None:
        raise ValueError("DB_PASSWORD environment variable is not set")

    return f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


def get_database_url() -> str:
    """
    環境変数（DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD）から
    データベース接続URLを取得する。

    Returns:
        正規化されたデータベース接続URL

    Raises:
        ValueError: 必要な環境変数が設定されていない場合
    """
    if not all(os.getenv(key) for key in ["DB_HOST", "DB_PORT", "DB_NAME", "DB_USER", "DB_PASSWORD"]):
        raise ValueError(
            "Database connection URL not found. "
            "Please set individual environment variables: DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD"
        )

    database_url = _build_database_url_from_env()
    return normalize_database_url(database_url)
