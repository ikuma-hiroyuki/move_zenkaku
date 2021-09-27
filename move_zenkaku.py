import glob
import re
import shutil

# 全角と(が含まれているファイルを移動させる
pattern = "[^\x01-\x7E]|[(]"
files = glob.glob("./image/*")
for file in files:
    res = re.search(pattern, file)
    if res is not None:
        print(file)
        shutil.move(file, "./zenkaku/")
