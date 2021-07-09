#模型文件在./output/rec_chinese_mv3_v2.0
# train 指令
 python3.7 tools/train.py -c configs/rec/ch_ppocr_v2.0/rec_chinese_mv3_train_v2.0.yml

# test 指令
python3 tools/infer/predict_rec.py --image_dir='/home/aistudio/data/data97405/B榜测试数据集/TestBImages' --rec_model_dir='output/rec_chinese_mv3_v2.0'
#生成‘识别结果.txt’文件在当前目录下