import glob
import re
import shutil
import os

REG_PATTERN = "[^\x01-\x7E]|[(]"

# 全角と(が含まれているファイルを移動させる
target_dir = input("Input image Folder path.\n") + "/*"
zenkaku_dir = input("Input Zenkaku Folder path.\n") + "/"
files = glob.glob(target_dir)
for file in files:
    res = re.search(REG_PATTERN, file)
    if res is not None:
        print(f"Move {os.path.basename(file)}")
        shutil.move(file, zenkaku_dir)
