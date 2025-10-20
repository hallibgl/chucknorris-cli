"""
API module for interacting with the Chuck Norris Jokes API.

Endpoints used
--------------
- GET https://api.chucknorris.io/jokes/random
- GET https://api.chucknorris.io/jokes/categories
- GET https://api.chucknorris.io/jokes/search?query={query}

All functions raise `RuntimeError` with a helpful message on recoverable errors.
"""
from __future__ import annotations

from typing import Any, Dict, List
import requests

BASE_URL = "https://api.chucknorris.io"


def _handle_response(resp: requests.Response) -> Any:
    """
    Validate an HTTP response and return parsed JSON.

    Parameters
    ----------
    resp : requests.Response
        The response object returned by `requests.get`.

    Returns
    -------
    Any
        Parsed JSON content.

    Raises
    ------
    RuntimeError
        If the request failed (HTTP error), the content is not JSON, or the
        API returned an unexpected structure.
    """
    try:
        resp.raise_for_status()
    except requests.HTTPError as exc:
        raise RuntimeError(f"HTTP error from API: {exc}") from exc

    try:
        data = resp.json()
    except ValueError as exc:
        raise RuntimeError("API returned non-JSON response.") from exc

    return data


def get_random_joke() -> str:
    """
    Fetch a single random Chuck Norris joke.

    Returns
    -------
    str
        The joke text.

    Raises
    ------
    RuntimeError
        On network/HTTP errors or invalid response structure.
    """
    try:
        resp = requests.get(f"{BASE_URL}/jokes/random", timeout=10)
        data = _handle_response(resp)
        value = data.get("value")
        if not isinstance(value, str):
            raise RuntimeError("Unexpected API response: missing 'value' string.")
        return value
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error while fetching random joke: {exc}") from exc


def get_categories() -> List[str]:
    """
    Retrieve the list of joke categories.

    Returns
    -------
    List[str]
        Categories provided by the API.

    Raises
    ------
    RuntimeError
        On network/HTTP errors or invalid response structure.
    """
    try:
        resp = requests.get(f"{BASE_URL}/jokes/categories", timeout=10)
        data = _handle_response(resp)
        if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
            raise RuntimeError("Unexpected API response: expected a list of strings.")
        return data
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error while fetching categories: {exc}") from exc


def search_jokes(query: str, limit: int | None = None) -> List[str]:
    """
    Search for jokes containing the provided query string.

    Parameters
    ----------
    query : str
        Search term; must be non-empty.
    limit : int | None
        Optional cap on number of jokes returned (applied client-side).

    Returns
    -------
    List[str]
        A list of joke texts matching the query.

    Raises
    ------
    ValueError
        If `query` is empty or whitespace.
    RuntimeError
        On network/HTTP errors or invalid response structure.
    """
    q = (query or "").strip()
    if not q:
        raise ValueError("Query cannot be empty.")

    try:
        resp = requests.get(f"{BASE_URL}/jokes/search", params={"query": q}, timeout=10)
        data = _handle_response(resp)
        result_list = data.get("result", [])
        if not isinstance(result_list, list):
            raise RuntimeError("Unexpected API response: 'result' is not a list.")
        jokes = []
        for item in result_list:
            if isinstance(item, dict) and isinstance(item.get("value"), str):
                jokes.append(item["value"])
        if limit is not None:
            jokes = jokes[: max(0, int(limit))]
        return jokes
    except requests.RequestException as exc:
        raise RuntimeError(f"Network error while searching jokes: {exc}") from exc
