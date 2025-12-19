from program_command.gendiff.compare import generate_diff

# Пути к тестовым файлам
file1 = 'tests/test_data/file1.json'
file2 = 'tests/test_data/file2.json'
file3 = 'tests/test_data/file3.json'
file4 = 'tests/test_data/file1.yaml'
file5 = 'tests/test_data/file2.yaml'
file6 = 'tests/test_data/file3.yaml'
file7 = 'tests/test_data/file_1.yaml'
file8 = 'tests/test_data/file_2.yaml'


def test_generate_diff_json():
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_with_file3():
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
    timeout: 50
}'''
    result = generate_diff(file1, file3)
    assert result == expected


def test_generate_diff_identical_files():
    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    result = generate_diff(file1, file1)
    assert result == expected


def test_generate_diff_yaml():
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}'''
    result = generate_diff(file4, file5)
    assert result == expected


def test_generate_diff_with_file3_yaml():
    expected = '''{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
    timeout: 50
}'''
    result = generate_diff(file4, file6)
    assert result == expected


def test_generate_diff_identical_files_yaml():
    expected = '''{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}'''
    result = generate_diff(file4, file4)
    assert result == expected


def test_generate_diff_different_file_1_and_file_3_yaml():
    expected = '''{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}'''
    result = generate_diff(file7, file8)
    assert result == expected