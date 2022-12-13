from src.lib.stings import remove_vogal

def test_remove_vogal():
    assert remove_vogal('teste') == 'tst'