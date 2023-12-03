import torch  # 假设你正在使用PyTorch

# 假设有一个四维张量 tensor，形状为 (a, b, c, d)
tensor = torch.randn(2, 2, 3, 3)

# 获取后两维的数据
# 使用负索引来表示从倒数第二维开始到最后一维
last_two_dims = tensor[:, :, :1, :]  # 获取后两维的数据
print(last_two_dims)

# 这里的 `[..., :]` 表示取所有维度的所有数据，但忽略前两维，保留后两维的数据

# 可以对 last_two_dims 进行进一步的操作或者使用
