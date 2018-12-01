import copy


def spllit_into_files():
    import json
    with open("final.json", 'r') as f:
        input_json = json.loads(f.read())
    first_half = copy.deepcopy(input_json)
    second_half = copy.deepcopy(input_json)

    mid_split = len(input_json['corpus']) // 2
    # print(len(input_json['corpus']), mid_split, type(
    #     input_json['corpus']), input_json['corpus'][0])
    first_half['corpus'] = input_json['corpus'][:mid_split]
    second_half['corpus'] = input_json['corpus'][mid_split:]
    print(len(first_half['corpus']))
    with open('first.json', 'w') as f:
        f.write(json.dumps(first_half))
    with open('second.json', 'w') as f:
        f.write(json.dumps(second_half))


def combine():
    import json
    with open('first.json', 'r') as f:
        first_half = json.loads(f.read())
    with open('second.json', 'r') as f:
        second_half = json.loads(f.read())

    full_json = copy.deepcopy(first_half)
    full_json['corpus'].extend(second_half['corpus'])
    with open("final.json", 'w') as f:
        f.write(json.dumps(full_json))


spllit_into_files()
# combine()

