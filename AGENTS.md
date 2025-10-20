# AGENTS.md — Context for AI Assistants

## Overview
A Python CLI that interacts with the public Chuck Norris Jokes API. Users can fetch a random joke, list categories, search for jokes, and save a random joke to a local file. The goal is a small but professional, testable, and CI-enabled portfolio project.

## API
- Base: https://api.chucknorris.io
- Endpoints used:
  - `/jokes/random` → single random joke
  - `/jokes/categories` → list of categories
  - `/jokes/search?query={q}` → results with `result: [{ value: str, ...}]`

## CLI Commands
- `random` → prints one random joke
- `categories` → prints categories (one per line)
- `search <query> [-n/--limit N]` → prints up to N matching jokes
- `save <filename>` → appends a random joke to the specified text file

## Architecture
- `src/api.py` — API calls via `requests` with a shared `_handle_response` helper; raises `RuntimeError` on recoverable failures.
- `src/main.py` — argparse setup with subparsers; command handlers return integer exit codes and print user-facing output.
- `tests/` — pytest tests; API calls are fully mocked using `unittest.mock.patch`.

## Coding Standards
- Docstrings on all public functions (NumPy-style).
- PEP 8 style; readable names; small functions.
- Error handling with clear messages; no bare network calls without timeouts.

## Testing Strategy
- No live HTTP during tests.
- Mock `requests.get` in `test_api.py` to simulate API responses and errors.
- Mock `src.main.api.*` functions in `test_main.py` to isolate CLI behavior.

## CI/CD
- GitHub Actions workflow runs `pip install -r requirements.txt` and `pytest` on push and PR.
- README includes a status badge pointing to the workflow named **Tests**.

## Notes for AI
- Keep the CLI surface area stable (commands above) for grading.
- Prefer explicit prints in the CLI, pure returns in API functions.
- Assume Python 3.10+.
