for epoch in range(epochs):
    for x, y in trainloader:
        yhat = model(x) # forward
        loss = criterion(yhat, y) # calculate loss
        optimizer.zero_grad() # set gradient to zero
        loss.backward() # transform (a function) into its derivative.
        optimizer.step() # update parameters