from unittest.mock import patch, MagicMock
from src.main import main


@patch("src.main.api.get_random_joke", return_value="A joke")
def test_cmd_random_success(mock_random):
    exit_code = main(["random"])
    assert exit_code == 0


@patch("src.main.api.get_categories", return_value=["animal", "dev"])
def test_cmd_categories_success(mock_cats):
    exit_code = main(["categories"])
    assert exit_code == 0


@patch("src.main.api.search_jokes", return_value=["J1", "J2"])
def test_cmd_search_success(mock_search):
    exit_code = main(["search", "roundhouse", "-n", "2"])
    assert exit_code == 0
