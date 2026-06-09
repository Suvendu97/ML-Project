# model.py
# import torch
# import torch.nn as nn

# class SimpleModel(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.linear = nn.Linear(3, 1)

#     def forward(self, x):
#         return self.linear(x)

# model = SimpleModel()

# # fake training (just random weights are fine for demo)
# torch.save(model.state_dict(), "model.pth")

def predict(x):
    return sum(x) * 0.5