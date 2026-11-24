import os
from pathlib import Path

poem = "Morning barges through the blinds; the room falls in line.\nAt six, even my inbox gets a pardon—with conditions."
out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "answer.txt").write_text(poem, encoding="utf-8")
