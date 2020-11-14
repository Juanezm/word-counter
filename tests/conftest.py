import json
from pathlib import Path

import pytest


@pytest.fixture
def json_test_file():
    test_file = Path(__file__).parent / "test_words.json"
    with open(test_file, "w") as json_file:
        json.dump({}, json_file)
    yield str(test_file)
    test_file.unlink()
