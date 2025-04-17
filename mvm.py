#!/usr/bin/env python3

import argparse
import subprocess
import os
from pathlib import Path

MOON_HOME = Path.home() / ".moon"
if os.environ.get("MOON_HOME"):
    MOON_HOME = Path(os.environ["MOON_HOME"])

MVM_BASE = MOON_HOME / "mvm"


def run_install(channel: str):
    moon_install_location = MVM_BASE / channel
    env = os.environ.copy()
    env["MOON_HOME"] = str(moon_install_location)

    if channel == "stable":
        print(f"Installing {channel} version of MoonBit to {moon_install_location}")
        cmd = "curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash"
    elif channel == "pre-release":
        print(f"Installing {channel} version of MoonBit to {moon_install_location}")
        cmd = "curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash -s 'pre-release'"
    elif channel == "bleeding":
        print(f"Installing {channel} version of MoonBit to {moon_install_location}")
        cmd = (
            "curl -fsSL https://cli.moonbitlang.com/install/unix.sh | bash -s bleeding"
        )
    else:
        raise ValueError("Unknown channel")

    subprocess.run(cmd, shell=True, check=True, env=env)


def run_use(channel: str):
    target = MVM_BASE / channel
    if not target.exists():
        raise FileNotFoundError(f"{target} does not exist. Please run install first.")

    MVM_BASE.mkdir(exist_ok=True)

    for subdir in ["bin", "include", "lib"]:
        link_path = MOON_HOME / subdir
        target_path = target / subdir
        if link_path.exists() or link_path.is_symlink():
            link_path.unlink()
        link_path.symlink_to(target_path)

        link_str = str(link_path).replace(str(Path.home()), "~")
        target_str = str(target_path).replace(str(Path.home()), "~")
        print(f"Linked {link_str} -> {target_str}")


def main():
    parser = argparse.ArgumentParser(
        description="MoonBit installer and environment switcher"
    )
    subparsers = parser.add_subparsers(dest="command")

    install_parser = subparsers.add_parser("install")
    install_parser.add_argument(
        "channel", choices=["stable", "pre-release", "bleeding"]
    )

    use_parser = subparsers.add_parser("use")
    use_parser.add_argument("channel", choices=["stable", "pre-release", "bleeding"])

    args = parser.parse_args()

    if args.command == "install":
        run_install(args.channel)
    elif args.command == "use":
        run_use(args.channel)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
