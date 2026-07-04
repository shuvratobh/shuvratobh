#!/usr/bin/env python3
"""
update_readme.py
────────────────
Dynamically refreshes sections of the GitHub profile README.
Runs inside GitHub Actions via .github/workflows/update-readme.yml

Currently updates:
  • "Last updated" timestamp in the footer
"""

import os
import re
from datetime import datetime, timezone

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME", "shuvratobh")
README_PATH = "README.md"


def update_last_updated(content: str) -> str:
    """Replace the <!-- LAST_UPDATED --> marker with a fresh timestamp."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    pattern = r"<!-- LAST_UPDATED -->.*?<!-- /LAST_UPDATED -->"
    replacement = f"<!-- LAST_UPDATED -->{now}<!-- /LAST_UPDATED -->"
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def main():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    content = update_last_updated(content)

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅  README updated successfully at {datetime.now(timezone.utc)}")


if __name__ == "__main__":
    main()
