from torch import nn, optim
from torch.utils.data import Dataset, DataLoader


# example linear regression
model = nn.Linear(2, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.1)

train_loader = DataLoader(dataset=data_set, batch_size=2)
for epoch in range(epochs):
    for x, y in train_loader:
        yhat = model(x) # forward
        loss = criterion(yhat, y) # calculate loss
        optimizer.zero_grad() # set gradient to zero
        loss.backward() # transform (a function) into its derivative.
        optimizer.step() # update parameters