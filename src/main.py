"""
CLI entry point for the Chuck Norris Jokes tool.
"""
from __future__ import annotations

import argparse
from typing import List, Optional
from . import api


def build_parser() -> argparse.ArgumentParser:
    """
    Build and return the argparse CLI parser.

    Returns
    -------
    argparse.ArgumentParser
        Configured parser with subcommands.
    """
    parser = argparse.ArgumentParser(
        prog="chuck",
        description="Chuck Norris Jokes CLI — fetch random jokes, categories, and search results.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # random
    p_random = subparsers.add_parser("random", help="Get a random joke.")
    p_random.set_defaults(func=cmd_random)

    # categories
    p_categories = subparsers.add_parser("categories", help="List all categories.")
    p_categories.set_defaults(func=cmd_categories)

    # search
    p_search = subparsers.add_parser("search", help="Search jokes by keyword.")
    p_search.add_argument("query", help="Search query string.")
    p_search.add_argument("-n", "--limit", type=int, default=5, help="Max jokes to return (default: 5).")
    p_search.set_defaults(func=cmd_search)

    # save
    p_save = subparsers.add_parser("save", help="Save a random joke to a file.")
    p_save.add_argument("filename", help="Path to output text file.")
    p_save.set_defaults(func=cmd_save)

    return parser


def cmd_random(_: argparse.Namespace) -> int:
    """Handle the `random` subcommand."""
    try:
        print(api.get_random_joke())
        return 0
    except Exception as exc:  # noqa: BLE001 - simple CLI tool
        print(f"Error: {exc}")
        return 1


def cmd_categories(_: argparse.Namespace) -> int:
    """Handle the `categories` subcommand."""
    try:
        cats = api.get_categories()
        if not cats:
            print("No categories found.")
        else:
            for c in cats:
                print(c)
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


def cmd_search(args: argparse.Namespace) -> int:
    """Handle the `search` subcommand."""
    try:
        jokes = api.search_jokes(args.query, limit=args.limit)
        if not jokes:
            print("No jokes found.")
        else:
            for j in jokes:
                print(f"- {j}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


def cmd_save(args: argparse.Namespace) -> int:
    """Handle the `save` subcommand."""
    try:
        joke = api.get_random_joke()
        with open(args.filename, "a", encoding="utf-8") as f:
            f.write(joke + "\n")
        print(f"Saved joke to {args.filename}")
        return 0
    except Exception as exc:
        print(f"Error: {exc}")
        return 1


def main(argv: Optional[List[str]] = None) -> int:
    """
    CLI entry point function. Exposed for testing.

    Parameters
    ----------
    argv : list[str] | None
        Arguments to parse. If `None`, defaults to `sys.argv[1:]`.

    Returns
    -------
    int
        Exit code (0 on success, non-zero on error).
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
