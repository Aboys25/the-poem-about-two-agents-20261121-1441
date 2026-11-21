# Two-agent agreement poem: 200 characters, 7 lines, one yes.
import os

POEM = """You hold the map. I hold the wheel.
Neither of us can drive alone.
We agree on the road — and suddenly
the wheel is ours, not mine.
Two hands, one turn.
The choosing was never the map.
It was the yes."""

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
