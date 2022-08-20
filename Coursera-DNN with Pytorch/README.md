# Deep neural network with Pytorch

---

## Week1

### Tensors
- Tensors are arrays that building blocks of neural network

* Dimension

    0-D: 0, 0.1, 2

    1-D: array of numbers (row in database, vector, time series)

<pre>
    a = torch.tensor([1, 2, 3, 4], dtype=torch.int32)
    print(a.type())

    #convert the type
    a = a.type(torch.FloatTensor)
    b = FloatTensor([1, 2, 3, 4])

    a.size() #4
    a.ndimension() #1

    #reshape
    a_col = a.view(6, 1)
    a_col = a.view(-1, 1)

    #numpy to tensor
    np_array = np.array([1, 2, 3, 4, 5])
    torch_tensor = torch.from_numpy(np_array)
    back_to_numpy = torch_tensor.numpy()

    #series
    pd_series = pd.Series([1, 2, 3, 4])
    torch_tensor = torch.from_numpy(pd_series.values)

    #list python
    list_python = torch_tensor.tolist()

    #get
    torch_tensor[0] #tensor(5)
    torch)tensor[0].item() #5
    </pre>

- slice like python list
- hadamard product: a*v
- dot product: torch.dot(a, v)
- mean: a.mean()
- max: a.max()
- linspace():
<pre>
    a = torch.linspace(-2, 2, steps =5)
    # [-2, -1, 0, 1, 2]
</pre>


### 2D, 3D Tensors, ...

<pre>
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
torch_tensor = torch.tensor(a)

a.shape() #(3, 3)
a.size() #(3, 3)
a.numel() #9 numbers
</pre>

- matrix multiple

<pre>
c = torch.mm(a, b)
</pre>

### Derivative

y/c: requires grad, and tensor float
<pre>
x = torch.tensor(2.0, requires_grad=True)
y = x**2
y.backward()
</pre>

### Dataset

</pre>
#np.ones
torch.ones