import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

X = torch.tensor([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=torch.float32)
y = torch.tensor([[0], [1], [1], [0]], dtype=torch.float32)

class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(2, 4)
        self.fc2 = nn.Linear(4, 1) 

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.sigmoid(self.fc2(x))
        return x

model = NeuralNetwork()

criterion = nn.BCELoss()  
optimizer = optim.SGD(model.parameters(), lr=0.1)

for epoch in range(1000):
    outputs = model(X)
    loss = criterion(outputs, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

predictions = (model(X) > 0.5).float()
print(predictions)
