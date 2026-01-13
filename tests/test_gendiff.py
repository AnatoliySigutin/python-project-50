from gendiff.compare import generate_diff

# Пути к тестовым файлам
file1 = "tests/test_data/file1.json"
file2 = "tests/test_data/file2.json"
file3 = "tests/test_data/file3.json"
file4 = "tests/test_data/file1.yaml"
file5 = "tests/test_data/file2.yaml"
file6 = "tests/test_data/file3.yaml"
file7 = "tests/test_data/file_1.yaml"
file8 = "tests/test_data/file_2.yaml"
file9 = "tests/test_data/file_1.json"
file10 = "tests/test_data/file_2.json"


def test_generate_diff_json():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file1, file2)
    assert result == expected


def test_generate_diff_with_file3():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
    timeout: 50
}"""
    result = generate_diff(file1, file3)
    assert result == expected


def test_generate_diff_identical_files():
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = generate_diff(file1, file1)
    assert result == expected


def test_generate_diff_yaml():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    result = generate_diff(file4, file5)
    assert result == expected


def test_generate_diff_with_file3_yaml():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
    timeout: 50
}"""
    result = generate_diff(file4, file6)
    assert result == expected


def test_generate_diff_identical_files_yaml():
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    result = generate_diff(file4, file4)
    assert result == expected


def test_generate_diff_different_file_1_and_file_3_yaml():
    expected = """{
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
}"""
    result = generate_diff(file7, file8)
    assert result == expected


def test_plain_format():
    excepted = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""
    result = generate_diff(file9, file10, format_name="plain")
    assert result == excepted


def test_json_format():
    excepted = """{
    "common": {
        "type": "nested",
        "children": {
            "follow": {
                "type": "added",
                "value": false
            },
            "setting1": {
                "type": "unchanged",
                "value": "Value 1"
            },
            "setting2": {
                "type": "removed",
                "value": 200
            },
            "setting3": {
                "type": "updated",
                "old_value": true,
                "new_value": null
            },
            "setting4": {
                "type": "added",
                "value": "blah blah"
            },
            "setting5": {
                "type": "added",
                "value": {
                    "key5": "value5"
                }
            },
            "setting6": {
                "type": "nested",
                "children": {
                    "doge": {
                        "type": "nested",
                        "children": {
                            "wow": {
                                "type": "updated",
                                "old_value": "",
                                "new_value": "so much"
                            }
                        }
                    },
                    "key": {
                        "type": "unchanged",
                        "value": "value"
                    },
                    "ops": {
                        "type": "added",
                        "value": "vops"
                    }
                }
            }
        }
    },
    "group1": {
        "type": "nested",
        "children": {
            "baz": {
                "type": "updated",
                "old_value": "bas",
                "new_value": "bars"
            },
            "foo": {
                "type": "unchanged",
                "value": "bar"
            },
            "nest": {
                "type": "updated",
                "old_value": {
                    "key": "value"
                },
                "new_value": "str"
            }
        }
    },
    "group2": {
        "type": "removed",
        "value": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    },
    "group3": {
        "type": "added",
        "value": {
            "deep": {
                "id": {
                    "number": 45
                }
            },
            "fee": 100500
        }
    }
}"""
    result = generate_diff(file9, file10, format_name="json")
    assert result == excepted
