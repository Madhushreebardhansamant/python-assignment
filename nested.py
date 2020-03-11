# 3)Find the key whether it exits or not in a nested dict
def present_key(dic, key):
    dic_keys = list(dic.keys())

    if key in dic_keys:
        return 'yes exist'
    elif isinstance(dic[dic_keys[0]], dict):
        return present_key(dic[dic_keys[0]], key)
    else:
        return "not exist"
dic = {"a": {"b": {"c": 1}}}
key = 'a'
print(present_key(dic, key))