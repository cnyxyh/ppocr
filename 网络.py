
# import paddlehub as hub

# ocr = hub.Module(name="chinese_ocr_db_crnn_server")
# ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")

import json
import os

# from paddle.onnx import export

# FLAGS_fraction_of_gpu_memory_to_use = 0
# FLAGS_memory_fraction_of_eager_deletion = 1
# FLAGS_eager_delete_tensor_gb = 0

# os.environ['CUDA_VISIBLE_DEVICES'] = '0'
# CUDA_VISIBLE_DEVICES_of_gpu_memory_to_use = 0
# CUDA_VISIBLE_DEVICES_fraction_of_gpu_memory_to_use = 0

import base64
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

import cv2
import numpy as np




# print('调用ocr')

# def ocrdao(imagss):
    # results = ocr.recognize_text(
    #     images=imagss,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式；
    #     use_gpu=True,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
    #     box_thresh=0.5,  # 检测文本框置信度的阈值；
    #     text_thresh=0.5)  # 识别中文文本置信度的阈值；
    # return results


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
                            # zjttx["rect"] = str(item[1][0][0]) + "," + str(item[1][0][1]) + "," + str(
                            #     item[1][2][0] - item[1][0][0]) + "," + str(item[1][2][1] - item[1][0][1])
                        elif item[0] == "confidence":
                            zjttx["score"] = item[1]
                    # print("AA增加", zjttx)
                    lsxx["PaddleOCR"].append(zjttx)
    # json_dict = json.dumps(lsxx)
    # print("lsxx", type(json_dict), json_dict)
    return json.dumps(lsxx)  # 将表里所有单引号转为双引号


# post网络
class S(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()  # 输出IP

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        res = run_inference(post_data.decode('utf-8'))
        self.do_HEAD()
        self.wfile.write("{}".format(res).encode('utf-8'))  # 这里发送了 res


# post网络
def run(server_class=HTTPServer, handler_class=S, port=8088):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


# post网络调用
def run_inference(jpeg):
    # imgs = jpeg  # 这里调用了 be64的图片数据
    imgs = base64.b64decode(jpeg)  # 解码
    img = cv2.imdecode(np.frombuffer(imgs, np.uint8), cv2.IMREAD_COLOR)  # 二进制数据流转np.ndarray [np.uint8: 8位像素]
    print(img)
    print(type(img))
    # dict_new = ocrdao([img])  # 得到img和坐标结果
    # return retchuli(dict_new)


if __name__ == '__main__':
    run()
    input('结束')
