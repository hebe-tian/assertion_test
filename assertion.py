import jsonpath
import json


# list assert length
# dict into , son dict assert keys exist
# str assert equal
def auto_assert(response):
    # response_dict = json.loads(response)
    assert_content = {}
    path1_list = response.keys()
    for path1 in path1_list:
        new_path1 = path1
        content1 = jsonpath.jsonpath(response, new_path1)[0]
        if type(content1) == list:
            data = len(content1)
            assert_content[new_path1] = {
                'type': 'list',
                'data': data
            }
        elif type(content1) == dict:
            data = content1
            path2_list = data.keys()
            for path2 in path2_list:
                new_path2 = path2
                content2 = jsonpath.jsonpath(data, new_path2)[0]
                print(content2)

                if type(content2) == list:
                    data2 = len(content2)
                    assert_content[new_path1+'.'+new_path2] = {
                        'type': 'list',
                        'data': data2
                    }
                elif type(content2) == dict:
                    data2 = content2
                    data2_key = list(data2.keys())
                    assert_content[new_path1+'.'+new_path2] = {
                        'type': 'dict',
                        'data': data2_key
                    }
                else:
                    data2 = content2
                    assert_content[new_path1+'.'+new_path2] = {
                        'type': 'str',
                        'data': data2
                    }
        else:
            data1 = content1
            assert_content[new_path1] = {
                'type': 'str',
                'data': data1
            }
    return assert_content
