# Yolo Custom Training 
#### https://keyog.tistory.com/6?category=879585
#### https://github.com/AlexeyAB/darknet.git
## Install Cuda
### RTX 3090 *8 cuda 11.0 cudnn8.0.4
## Install Darknet
```
git clone https://github.com/wlgnsthd/darknet_training.git
# OR git clone https://github.com/AlexeyAB/darknet.git
cp darknet_training darknet
cd darknet

gedit Makefile
# GPU=1 CUDNN=1(오류시 0) OPENCV=1(오류시 0) OPENMP=1 DEBUG=0
# Edit GPU gen 

make
```

## cfg수정
```
gedit custom_yolov4.cfg
```
```
# 수정 1 : width height 608 608 -> 416 416, batch size 조절 (gpu)
[net]
# Testing
# batch=1
# subdivisions=1
# Training
batch=64
subdivisions=16
width=416
height=416
channels=3
momentum=0.9
decay=0.0005
angle=0
saturation = 1.5
exposure = 1.5
hue=.1

learning_rate=0.001
burn_in=1000
max_batches = 500200
policy=steps
steps=400000,450000
scales=.1,.1
```
```
# 수정 2 : ctrl + f로 yolo 찾은 다음 위 아래 filter(=(classes+5)*3), classes 3개 수정
[convolutional]
size=1
stride=1
pad=1
filters=60
activation=linear


[yolo]
mask = 0,1,2
anchors = 10,13,  16,30,  33,23,  30,61,  62,45,  59,119,  116,90,  156,198,  373,326
classes=15
num=9
jitter=.3
ignore_thresh = .7
truth_thresh = 1
random=1
```
## Put xmls into xmls folder and make it yolov3 label
### path : conversion/xmls & conversion/output
```
python3 conversion/xmltotxt.py -xml conversion/xmls -out conversion/output
```
________________________
## Put images(jpg) and labels(txt) into "dataset" folder
### path : customs/dataset
__________________
## Move train.txt and validation.txt from customs/dataset,7:3
### path : customs/train.txt & customs/valdiation.txt 
```
python3 customs/train_val.py
```
## Make custom.names and custom.data
### path : customs/custom.name & custom/custom.data
```
truck
ladder
```
```
classes= 2
train  = customs/train.txt
valid  = customs/validation.txt
names = customs/custom.names
backup = backup/
```
## Pretrain model 다운로드 (tiny는 yolov4-tiny.conv.29)
```
wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137
```
## Train
```
./darknet detector train custom/custom.data custom/custom_yolov4.cfg yolov4.conv.137 -gpus 0,1,2,3,4,5,6,7 -dont_show
```
