import shlex
import subprocess
from dataclasses import dataclass
from typing import Sequence


@dataclass
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


def run_command(argv: Sequence[str], timeout: float = 10.0) -> CommandResult:
    completed = subprocess.run(
        list(argv),
        capture_output=True,
        text=True,
        timeout=timeout,
        check=False,
    )
    return CommandResult(
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )


def ping(host: str, count: int = 1) -> CommandResult:
    safe_host = shlex.quote(host)
    return run_command(["ping", "-c", str(int(count)), safe_host])


def list_directory(path: str) -> CommandResult:
    return run_command(["ls", "-la", path])
