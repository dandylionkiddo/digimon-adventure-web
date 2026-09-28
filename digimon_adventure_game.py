#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""디지몬 어드벤처 콘솔 게임 런처"""
import base64, gzip, urllib.request, runpy, tempfile, os, sys

url = "https://raw.githubusercontent.com/dandylionkiddo/digimon-adventure-web/main/digimon_adventure_game.py.gz.b64"
print("게임 데이터를 불러오는 중...")
with urllib.request.urlopen(url, timeout=30) as r:
    b64 = r.read().decode().strip()
while len(b64) % 4:
    b64 += "="
code = gzip.decompress(base64.b64decode(b64))
path = os.path.join(tempfile.gettempdir(), "_digimon_adventure_game.py")
with open(path, "wb") as f:
    f.write(code)
sys.argv = [path] + sys.argv[1:]
runpy.run_path(path, run_name="__main__")
