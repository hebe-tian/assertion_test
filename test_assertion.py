import assertion


def test_return_list1():
    data = {"list": [1, 2, 3, 4]}
    res = assertion.auto_assert(data)
    assert res == {'list': {'type': 'list', 'data': 4}}


def test_return_list2():
    data = {"list1": {"list2": [1, 2, 3, 4]}}
    res = assertion.auto_assert(data)
    assert res == {'list1.list2': {'type': 'list', 'data': 4}}


def test_return_str():
    data = {"code": 200}
    res = assertion.auto_assert(data)
    assert res == {'code': {'type': 'str', 'data': 200}}


def test_return_str2():
    data = {"content": {"code": 200}}
    res = assertion.auto_assert(data)
    assert res == {'content.code': {'type': 'str', 'data': 200}}


def test_return_dict2():
    data = {"content": {"dict": {"key1": "value1", "key2": "value2"}}}
    res = assertion.auto_assert(data)
    assert res == {'content.dict': {'type': 'dict', 'data': ['key1', 'key2']}}


def test_return_complex():
    data = {
        "content": {
            "dict": {
                "key1": "value1",
                "key2": "value2"
            },
            "list": [1, 2, 3, 4],
            "str": "string"
        }
    }
    res = assertion.auto_assert(data)
    assert res == {
        'content.dict': {
            'type': 'dict',
            'data': ['key1', 'key2']
        },
        'content.list': {
            'type': 'list',
            'data': 4
        },
        'content.str': {
            'type': 'str',
            'data': 'string'
        }
    }
