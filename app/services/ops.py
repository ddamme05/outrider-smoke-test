import os
import pickle


def ping(host: str):
    os.system(f"ping -c 1 {host}")


def load_session(blob: bytes):
    return pickle.loads(blob)
