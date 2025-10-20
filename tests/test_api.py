import pytest
from unittest.mock import patch, MagicMock
from src import api


@patch("src.api.requests.get")
def test_get_random_joke_success(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {"value": "Chuck can divide by zero."}
    mock_resp.raise_for_status.return_value = None
    mock_get.return_value = mock_resp

    joke = api.get_random_joke()
    assert isinstance(joke, str)
    assert "Chuck" in joke


@patch("src.api.requests.get")
def test_get_categories_success(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = ["animal", "career"]
    mock_resp.raise_for_status.return_value = None
    mock_get.return_value = mock_resp

    cats = api.get_categories()
    assert cats == ["animal", "career"]


@patch("src.api.requests.get")
def test_search_jokes_success_with_limit(mock_get):
    mock_resp = MagicMock()
    mock_resp.json.return_value = {
        "result": [
            {"value": "Chuck fact 1"},
            {"value": "Chuck fact 2"},
            {"value": "Chuck fact 3"},
        ]
    }
    mock_resp.raise_for_status.return_value = None
    mock_get.return_value = mock_resp

    jokes = api.search_jokes("chuck", limit=2)
    assert jokes == ["Chuck fact 1", "Chuck fact 2"]


def test_search_jokes_empty_query_raises():
    with pytest.raises(ValueError):
        api.search_jokes("   ")
