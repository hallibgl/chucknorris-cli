# Chuck Norris Jokes CLI

![Tests](https://github.com/hallibgl/chucknorris-cli/workflows/Tests/badge.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)


A simple, portfolio-ready command-line tool that fetches data from the public [Chuck Norris API](https://api.chucknorris.io/).  
Built with argparse, tested with pytest (including mocked API calls), and wired up to GitHub Actions CI.

## Features
- `random` — fetch a random Chuck Norris joke
- `categories` — list all available joke categories
- `search <query>` — search for jokes by keyword (with `-n/--limit`)
- `save <filename>` — append a random joke to a local file

## Quick Start

```bash
git clone https://github.com/USERNAME/REPO.git
cd REPO
python -m venv .venv && source .venv/bin/activate  # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Usage

Run the CLI via module execution:

```bash
python -m src.main --help
python -m src.main random
python -m src.main categories
python -m src.main search "roundhouse" -n 3
python -m src.main save jokes.txt
```

## Testing

```bash
pytest -v
```

All tests mock HTTP requests so they run without internet access.

## Tech Stack
- Python 3.10+
- argparse
- requests
- pytest
- GitHub Actions (CI)

## API Credit
This project uses the free and public **Chuck Norris Jokes API**: https://api.chucknorris.io/

## Badges
- Update the `USERNAME/REPO` parts of the badge URL above to point to your GitHub repository.

## License
MIT — see [LICENSE](LICENSE).
