from ..src.lib.stings import remove_vogal

def test_remove_vogal():
   assert remove_vogal('teste') == 'tst'

def test_remove_vogal_aeiou():
   assert remove_vogal('aeiou') == ''

def test_remove_vogal_123():
    assert remove_vogal(123) == ''

def test_remove_vogal_1b3c():
   assert remove_vogal('1b3c') == '1b3c'

def test_remove_vogal_123():
   assert remove_vogal('qwrtd') == 'qwrtd'