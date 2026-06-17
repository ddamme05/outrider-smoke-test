import os
import sys


def slugify(s: str) -> str:
    return s.strip().lower().replace(" ", "-")
