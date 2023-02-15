# {"PaddleOCR":[{"ttxt":"喵了个大咪","rect":"3,4,124,31","score":"0.969148"},{"ttxt":"乌倩倩","rect":"5,86,74,34","score":"0.968494"}]}
# arr = [{'save_path': '', 'data': [
#     {'text': '喵了个大咪', 'confidence': 0.9852021336555481, 'text_box_position': [[9, 11], [131, 11], [131, 40], [9, 40]]},
#     {'text': '乌倩倩', 'confidence': 0.81844562292099, 'text_box_position': [[9, 93], [83, 95], [82, 128], [8, 125]]}]}]
import json


# arr = [{'save_path': '', 'data': []}]

# arr = [{"save_path": "", "data": [{"text": "倚楼听风_合1", "confidence": 0.8204723000526428, "text_box_position": [[5, 16], [152, 16], [152, 49], [5, 49]]}]}]

# lssst = {'text': '倚楼听风_合1', 'confidence': 0.8204723000526428, 'text_box_position': [[5, 16], [152, 16], [152, 49], [5, 49]]}

arr =[[[[9.0, 13.0], [135.0, 13.0], [135.0, 50.0], [9.0, 50.0]], ('宋金战场', 0.9947867393493652)]]
# {"PaddleOCR":[{"ttxt":"喵了个大咪","rect":"3,4,124,31","score":"0.969148"},{"ttxt":"乌倩倩","rect":"5,86,74,34","score":"0.968494"}]}
def ocrdao(arr):
    # retrec = {}
    lsxx = {"PaddleOCR": []}
    for k, v in arr:
        ttxt = v[0]  # 识别到的文字
        rect = [int(k[0][0]), int(k[0][1]), int(k[2][0]) - int(k[0][0]), int(k[2][1]) - int(k[0][1])]
        # rect= str(int(k[0][0])) + "," + str(int(k[0][1])) + "," + str(int(k[2][0])-int(k[0][0])) + "," + str(int(k[2][1])-int(k[0][1]))
        score = '{:.3f}'.format(v[1])  # 识别准确率 保留小数点后三位



        # top = str(int(k[0][0])) + "," + str(int(k[0][1]))  # 识别文本相对图片顶点坐标
        # bot = str(int(k[2][0])) + "," + str(int(k[2][1]))  # 识别文本相对图片下边坐标
        # retrec = {'ttxt': ttxt, 'rect': rect, 'score': score}
        lsxx["PaddleOCR"].append({'ttxt': ttxt, 'rect': rect, 'score': score})
        print(lsxx)

        # text = v[0]  # 识别到的文字
        # score = '{:.3f}'.format(v[1])  # 识别准确率 保留小数点后三位
        # top = str(int(k[0][0])) + "," + str(int(k[0][1]))  # 识别文本相对图片顶点坐标
        # bot = str(int(k[2][0])) + "," + str(int(k[2][1]))  # 识别文本相对图片下边坐标
        # retrec[text] = {'top': top, 'bot': bot, 'score': score}
        # print(str(retrec))

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


print('调用', ocrdao(arr))

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
