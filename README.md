# 模型文件在./output/rec_chinese_mv3_v2.0
# train 指令
 python3.7 tools/train.py -c configs/rec/ch_ppocr_v2.0/rec_chinese_mv3_train_v2.0.yml

# test 指令
python3 tools/infer/predict_rec.py --image_dir='/home/aistudio/data/data97405/B榜测试数据集/TestBImages' --rec_model_dir='output/rec_chinese_mv3_v2.0'
#生成‘识别结果.txt’文件在当前目录下

# 调优策略
1、统计将训练集和测试集所有出现过的字符做一个统计，得到字符集，减少输出结点个数，同时精确给出所有出现的字符的可能；
2、修改了MobileNet-v3的网络结构并调优；
3、尝试了ShuffleNet-v2效果没有mobile-v3好，参数量相差不大；
4、修改了LSTM网络结构并调优。

# 结果
该模型被压缩到10Mb以内，符合比赛要求，在B榜测试数据集上识别精度78%

# 识别结果可视化
![image](https://github.com/a-maomao/Ultra_light_OCR_No.14/blob/main/imgs_for_show/image1.jpg)
![image1](https://github.com/a-maomao/Ultra_light_OCR_No.14/blob/main/imgs_for_show/result1.jpg)
