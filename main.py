#!/usr/bin/env python3
"""Write the weirdest job title entry to /output/entry.txt."""
import os

# 49 characters
TITLE = "Chief Apology Officer for Robots Who Feel Nothing"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(TITLE)
