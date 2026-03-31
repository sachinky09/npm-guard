#!/usr/bin/env python3

import argparse
from scanner import run_scan

def main():
    parser = argparse.ArgumentParser(prog="npm-guard", description="NPM Security Scanner")

    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan")
    scan.add_argument("target")
    scan.add_argument("--json", action="store_true")
    scan.add_argument("--no-yara", action="store_true")

    args = parser.parse_args()

    if args.command == "scan":
        run_scan(args.target, json_out=args.json, use_yara=not args.no_yara)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
