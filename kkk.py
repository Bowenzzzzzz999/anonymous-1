import torch
from torch import nn
m = nn.Softmax()
input = torch.randn(2, 3)
# output = m(input,1)
sum(input)
output = m(sum(input))
print(1)