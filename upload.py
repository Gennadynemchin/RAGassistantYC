from glob import glob

from config import DATA_DIR, sdk


def upload_files() -> list:
    filenames = glob(f"{DATA_DIR}/*.md")
    if not filenames:
        raise FileNotFoundError(f"No .md files found in '{DATA_DIR}/'")

    files = []
    for fn in sorted(filenames):
        file = sdk.files.upload(fn, ttl_days=7, expiration_policy="static")
        files.append(file)
    return files
