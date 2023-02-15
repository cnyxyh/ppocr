# {"PaddleOCR":[{"ttxt":"喵了个大咪","rect":"3,4,124,31","score":"0.969148"},{"ttxt":"乌倩倩","rect":"5,86,74,34","score":"0.968494"}]}
arr = [{'save_path': '', 'data': [
    {'text': '喵了个大咪', 'confidence': 0.9852021336555481, 'text_box_position': [[9, 11], [131, 11], [131, 40], [9, 40]]},
    {'text': '乌倩倩', 'confidence': 0.81844562292099, 'text_box_position': [[9, 93], [83, 95], [82, 128], [8, 125]]}]}]
import json


# arr = [{'save_path': '', 'data': []}]
# arr = [{"save_path": "", "data": [{"text": "倚楼听风_合1", "confidence": 0.8204723000526428, "text_box_position": [[5, 16], [152, 16], [152, 49], [5, 49]]}]}]

# lssst = {'text': '倚楼听风_合1', 'confidence': 0.8204723000526428, 'text_box_position': [[5, 16], [152, 16], [152, 49], [5, 49]]}


def retchuli(arr):
    lsxx = {"PaddleOCR": []}
    for key in arr[0].keys():
        if key == 'data':
            if len(arr[0][key]) > 0:
                for i in arr[0][key]:
                    zjttx = {}
                    for item in i.items():
                        if item[0] == "text":
                            zjttx["ttxt"] = item[1]
                            # print('ttxt增加',item[1])
                        elif item[0] == "text_box_position":
                            zjttx["rect"] = [item[1][0][0], item[1][0][1], item[1][2][0] - item[1][0][0],
                                             item[1][2][1] - item[1][0][1]]
                        elif item[0] == "confidence":
                            zjttx["score"] = item[1]
                    # print("AA增加", zjttx)
                    lsxx["PaddleOCR"].append(zjttx)
    # json_dict = json.dumps(lsxx)
    # print("lsxx", type(json_dict), json_dict)
    return json.dumps(lsxx)


print('调用', retchuli(arr))

#
#
#
#


# rexx.append()
#
# print('rexx',  type(rexx))
# arr = [{'save_path': '', 'data': []}]
# print('arr',type(arr[0]))
#
# if len(arr[0]['data']) == 0:
#     print('AAAA')
#
# print('aaa', arr[0]['data'], type(arr[0]['data']), len(arr[0]['data']))
