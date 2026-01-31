# YOLO 输出的结果

## 输出结果整体结构

```bash
<class 'list'>
```

我们可以看到这个是属于一个列表的，当我们提取出来其中的元素（只有一个对于单张图片，对于视频就是每一帧）

## 单个结果对象类型

```python
print(type(result[0]))
```

```bash
<class 'ultralytics.engine.results.Results'>
```

可以发现是 YOLO 自己的类型

## Results 的主要属性

#### names:类别映射表

```python
print(result[0].names)
```

```json
{
  0: 'person',
  1: 'bicycle',
  2: 'car',
  3: 'motorcycle',
  ...
}
```

我们可以发现这个是一个字典，告诉了不同物品的对应关系

#### boxes:检测框集合（核心）

```python
print(result[0].boxes)
```

```bash
cls: tensor([2., 2.,...], device='cuda:0')
conf: tensor([0.8739, 0.7434,...], device='cuda:0')
data: tensor([[6.1620e+01,...]], device='cuda:0')
id: None
is_track: False
orig_shape: (365, 519)
shape: torch.Size([15, 6])
xywh: tensor([[115.6755, ...]], device='cuda:0')
xywhn: tensor([[0.2229,...1]], device='cuda:0')
xyxy: tensor([[6.1620e+01,...]], device='cuda:0')
xyxyn: tensor([[1.1873e-01, ...]], device='cuda:0')
```

`boxes` 就是 `results` 中识别物体圈出来的方框
其中我们不同的字段的含义为

- cls:类别，和前面 `names` 对应的物体名称
- conf:置信度，即识别出来物体为真的概率
- data: 最低层的原始数据，一般用后面的内容
    - 顺序为 `[x1, y1, x2, y2, conf, cls]`
- id:跟踪 ID，只有在 `model.track()` 才存在
- is_track:是否为 tracking 模式结果
    - False:普通检测
    - True: 多目标跟踪
- orig_shape:原始图像尺寸
    - `(height, width)`
- shape:检测框数量和字段数与 `data.shape` 相同
- xywh:中心点 + 宽高
    - `xywh: tensor([[x_center, y_center, width, height], ...])`
    - 单位是像素
    - 常用于：
        - 与 YOLO 标签格式一致
        - 目标跟踪 / Kalman Filter
- xywhn：归一化 xywh
    - 坐标范围：`[0, 1]`
    - 与图像尺寸无关，便于：
        - 跨分辨率训练
        - 导出到 ONNX / TensorRT
- xyxy:左上 + 右下坐标
    - `xyxy: tensor([[x1, y1, x2, y2], ...])`
        - 即 `(x_min, y_min, x_max, y_max)`
    - 单位是像素
    - 常用于：
        - 画框
        - 裁剪 ROI
- xyxyn：归一化 xyxy
    - 坐标范围：`[0, 1]`
    - 与图像尺寸无关，便于：
        - 跨分辨率训练
        - 导出到 ONNX / TensorRT

总结来说即

| 字段           | 含义                                   |
|--------------|--------------------------------------|
| `cls`        | 类别 ID（与 `names` 对应）                  |
| `conf`       | 置信度（最终 detection score）              |
| `data`       | 原始底层数据 `[x1, y1, x2, y2, conf, cls]` |
| `id`         | 跟踪 ID（仅 `model.track()` 时存在）         |
| `is_track`   | 是否为多目标**跟踪**结果                       |
| `orig_shape` | 原始图像尺寸 `(height, width)`             |
| `shape`      | 检测框数量 × 字段数                          |
| `xywh`       | `(x_center, y_center, w, h)`（像素）     |
| `xywhn`      | 归一化 `(x, y, w, h)` ∈ `[0,1]`         |
| `xyxy`       | `(x1, y1, x2, y2)`（像素）               |
| `xyxyn`      | 归一化 `(x1, y1, x2, y2)`               |

###### 常用字段选型建议

| 场景              | 推荐字段             |
|-----------------|------------------|
| 画框 / 裁剪 ROI     | `xyxy`           |
| 保存 YOLO 标签      | `xywhn`          |
| 跟踪 / 卡尔曼滤波      | `xywh`           |
| TensorRT / ONNX | `xyxyn` 或 `data` |
| 业务逻辑判断          | `cls + conf`     |

