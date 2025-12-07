import json
from journal.storage import write, read, overwrite

def test_storage(tmp_path):
    test_file = tmp_path / "test.json"
    overwrite(test_file)

    data = [{"entry": "hi"}]
    write(test_file, data)

    assert read(test_file) == data