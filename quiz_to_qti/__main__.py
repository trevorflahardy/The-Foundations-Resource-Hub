from __future__ import annotations

# Import the Click CLI group as `main` so `python -m quiz_to_qti` works
from .cli import cli as main

if __name__ == "__main__":
    main()
