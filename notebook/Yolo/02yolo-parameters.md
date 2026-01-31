# YOLO 参数
其默认/可设置的参数放在 `default.yaml` 我下载下来放到了

```bash
src/02yolo-parameters/default.yaml
attachment/02yolo-parameters/default.yaml
```

我们可以从这个位置来查看默认的参数和有那些可以设置的
[default.yaml](attachment/02yolo-parameters/default.yaml)

下面给出一个常用的参数设置

## conf
```yaml
conf: # (float, optional) confidence threshold; defaults: predict=0.25, val=0.001
```
模型判断物体为真的概率，低于这个值在结果中是不会显示的
```python
result_conf = yolo.predict(source="traffic.png", save=True, conf=0.66)
```
就可以设置这个参数

