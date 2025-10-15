import pytest
from program_command.gendiff.compare import generate_diff

# Пути к тестовым файлам
file1 = 'tests/test_data/file1.json'
file2 = 'tests/test_data/file2.json'
file3 = 'tests/test_data/file3.json'

def test_generate_diff_json():
    expected = '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}'''
    result = generate_diff(file1, file2)
    # Сравниваем построчно
    assert result.splitlines() == expected.splitlines()

def test_generate_diff_with_file3():
    # Тест сравнения file1 и file3
    expected = '''{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
  timeout: 50
}'''
    result = generate_diff(file1, file3)
    assert result.splitlines() == expected.splitlines()

def test_generate_diff_identical_files():
    # Тест сравнения одного и того же файла
    expected = '''{
  follow: False
  host: hexlet.io
  proxy: 123.234.53.22
  timeout: 50
}'''
    result = generate_diff(file1, file1)
    assert result.splitlines() == expected.splitlines()

