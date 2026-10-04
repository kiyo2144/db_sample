import os
from dotenv import load_dotenv

load_dotenv(override=True)

print(os.environ.get("PWD"))
# OSの中のPWD環境変数を読み込み
print(os.environ.get("SECRET"))
