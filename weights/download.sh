#!/bin/bash

# Downloading darknet53 weights
wget -nc https://pjreddie.com/media/files/darknet53.weights

# Downloading darknet53.74 weights
wget -nc https://pjreddie.com/media/files/darknet53.conv.74 -O darknet53.conv.74.weights

# Downloading yolo weights
wget -nc https://pjreddie.com/media/files/yolov3.weights

# Downloading tiny-yolo weights
wget -nc https://pjreddie.com/media/files/yolov3-tiny.weights