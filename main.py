import os
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

FLAGS_eager_delete_tensor_gb = 0.0  # 垃圾占用大小达到0.0GB时释放内存垃圾，即一旦出现垃圾则马上释放。
FLAGS_fast_eager_deletion_mode = True  # 启用快速垃圾回收策略。
FLAGS_fraction_of_gpu_memory_to_use = 0.1  # 分配GPU总可用显存大小的10%作为初始GPU显存块。
FLAGS_conv_workspace_size_limit = 1024  # 将用于选择cuDNN卷积算法的工作区限制大小设置为1024MB
FLAGS_eager_delete_scope = True  # 同步局域删除 设置后，它将降低GPU内存使用量，但同时也会减慢销毁变量的速度（性能损害约1％）
FLAGS_memory_fraction_of_eager_deletion = 1

from paddleocr import PaddleOCR
import base64
import cv2
import numpy as np
import json

# 初始化OCR
runpath = os.path.abspath(".")

ocr = PaddleOCR(
    det_model_dir=runpath + "/inference/ch_PP-OCRv3_det_infer/",  # 检测模型目录
    det_max_side_len=960,  # 图片长边的最大尺寸,超出缩放,正常游戏截图都比较小使用默认基本都可以
    det_db_thresh=0.3,  # 检测模型输出预测图的二值化阈值                        影响识别关键0.1-1之间自己调整
    det_db_box_thresh=0.5,  # 检测模型输出框的阈值, 低于此值的预测框会被丢弃          影响识别关键0.1-1之间自己调整
    det_db_unclip_ratio=2,  # 检测模型输出框扩大的比例                              影响识别关键0.1-10之间自己调整 游戏正常在0.3-2之间
    rec_model_dir=runpath + "/inference/ch_PP-OCRv3_rec_infer/",  # 识别模型目录
    # rec_char_dict_path=runpath + '/rec/dict.txt',  # 识别字典文件
    use_space_char=True,  # 是否识别空格
    # max_text_length=25,  # 识别的最大文字长度
    cls_model_dir=runpath + "/inference/ch_ppocr_mobile_v2.0_cls_infer/",  # 分类模型目录 正常用不到
    use_gpu=True,  # 使用GPU
    gpu_mem=1000,  # 指定显存  ---------
    lang="ch",  # 模型语言类型,目前支持 中文(ch)、英文(en)及数字  ch=中文+数字+英文
    det=False,  # 使用启动检测
    rec=True,  # 是否启动识别
    cls=False,  # 是否启动分类
)


def ocrdao(img):
    result = ocr.ocr(img, det=True, cls=False)  # 从这里载入的  加载img
    # print('打印结果', result)
    lsxx = {"msg": [{"data": []}]}
    for k, v in result:
        lsxx["msg"][0]["data"].append({'text': v[0], 'text_box_position': k, 'confidence': '{:.3f}'.format(v[1])})
    return json.dumps(lsxx)


class Item(BaseModel):
    name: str
    description: Union[str, None] = None  # 可选参数
    price: float
    tax: Union[float, None] = None  # 可选参数


# 传入__name__实例化Flask
app = FastAPI(debug=False)


@app.post('/predict/')
def create_item(item: Item):
    imgs = base64.b64decode(item.name)  # 解码
    print("长度", len(imgs))
    img = cv2.imdecode(np.frombuffer(imgs, np.uint8), cv2.IMREAD_COLOR)  # 二进制数据流转np.ndarray [np.uint8: 8位像素]
    dict_new = ocrdao(img)  # 得到img和坐标结果
    print('打印结果', dict_new)
    return dict_new


if __name__ == '__main__':
    uvicorn.run(app)
    # uvicorn.run(app, host="0.0.0.0", port=8994)
    # uvicorn.run(app, host="0.0.0.0", port=7000)
    # gunicorn -c gunicorn_config.py main:app
    # gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
