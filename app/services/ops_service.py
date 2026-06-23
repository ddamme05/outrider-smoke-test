import os


def ping(host: str):
    os.system(f"ping -c 1 {host}")
