FROM registry.baidubce.com/paddlepaddle/paddle:2.1.0-gpu-cuda10.2-cudnn7
LABEL maintainer='Mao Yongjiang; myj@whu.edu.cn'
RUN pip3.7 install -r requirements.txt -i https://mirror.baidu.com/pypi/simple

