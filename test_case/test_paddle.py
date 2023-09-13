# https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/deploy/paddle2onnx/readme.md

# 下载超轻量中文检测模型：
# apt install git wget
# wget  https://paddleocr.bj.bcebos.com/PP-OCRv3/chinese/ch_PP-OCRv3_det_infer.tar
# tar xf ch_PP-OCRv3_det_infer.tar
# python3 tools/infer/predict_det.py --image_dir="./doc/imgs/00018069.jpg" --det_model_dir="./ch_PP-OCRv3_det_infer/"

# Pillow==10.0.0 要升版

paddle2onnx --model_dir ./inference/ch_ppocr_mobile_v2.0_cls_infer \
--model_filename inference.pdmodel \
--params_filename inference.pdiparams \
--save_file ./inference/cls_onnx/model.onnx \
--opset_version 10 \
--input_shape_dict="{'x':[-1,3,-1,-1]}" \
--enable_onnx_checker True

python3 tools/infer/predict_system.py --use_gpu=False --use_onnx=True \
--det_model_dir=./inference/det_onnx/model.onnx  \
--rec_model_dir=./inference/rec_onnx/model.onnx  \
--cls_model_dir=./inference/cls_onnx/model.onnx  \
--image_dir=doc/imgs_en/img_12.jpg \
--rec_char_dict_path=ppocr/utils/en_dict.txt
