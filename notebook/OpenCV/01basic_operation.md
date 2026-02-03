# OpenCV 基本操作

## 图片的读取和保存

基本内容参照代码

```bash
src/OpenCV/01base_operation/main.ipynb
```

## 视频的读取和保存

```python
vc = cv2.VideoCapture("demo.mp4")
```

我们其是是按照每一帧进行图像处理

我们调用

```python
vc.read() 
```

其实是有两个返回值，一个是状态，为布尔类型，另一个是图像信息

我们每一次调用这个，就是会返回下一帧的内容

下面就是我们完整的内容

```python
vc = cv2.VideoCapture("demo.mp4")

if vc.isOpened():
    isOpen, frame = vc.read()
else:
    isOpen = False

while isOpen:
    ret, frame = vc.read()
    if frame is None:
        break
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('result', gray)
        if cv2.waitKey(10) & 0xFF == 27:
            break

vc.release()
cv2.destroyAllWindows()
```

## 颜色通道

## 填充/Padding

## 数值计算
