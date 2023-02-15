
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '0'

# os.system("hub serving start -m chinese_ocr_db_crnn_server==1.1.3 --port 8866 --use_gpu --workers 20")

os.system("hub serving start -c ./deploy/hubserving/ocr_system/config.json")
# os.system("python D:/YOLO/PaddleOCR-release-2.5hub/tools/test_hubserving.py --server_url=http://127.0.0.1:8866/predict/ocr_system --image_dir=D:/YOLO/PaddleOCR-release-2.5hub/1660316683581.bmp --visualize=false")

