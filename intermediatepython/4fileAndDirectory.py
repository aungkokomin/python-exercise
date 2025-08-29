import os
from pathlib import Path

for file in Path('.').glob("*.txt"):
    file.rename(file.with_suffix(".bak"))
