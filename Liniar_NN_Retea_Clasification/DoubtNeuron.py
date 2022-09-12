# MODEL



class DoubtNeuron:
    def __init__(self):
        #               w0 W1
        self.weights = [0, 0, 0, 0]
        self.bias = 0
    def activation(self,x):
        e = 2.72
        return 1 / ( 1 + e ** -x)

    def forward(self,X):
        y = self.weights[0] * X[0] + self.weights[1] * X[1] +  self.weights[2] * X[2]+  self.weights[3] * X[3]+ self.bias
        y = self.activation(y)
        return y

    def __str__(self):
        return f"{self.weights[0]:12.6f} * x0 + {self.weights[1]:12.6f} * x1 +{self.weights[2]:12.6f} * x2 + {self.weights[3]:12.6f} * x3 + {self.bias: 12.6f}"

# HELPER FUNCTION

def loss(y,yp):
    return y - yp


# DATA SET

data_set_X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

data_set_X_one_hot = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]

data_set_Y = [
    0,
    1,
    1,
    0
]

# TRAINING

lr = 0.01
model = DoubtNeuron()
for epoch in range(2000):
    # pass trough all the data on each epoch
    for i in range(4):
        xt = data_set_X_one_hot[i]
        yt = data_set_Y[i]

        yp = model.forward(xt)

        e = loss(yt,yp)

        dBias = lr * e
        dWeight0 = lr * e * xt[0]
        dWeight1 = lr * e * xt[1]
        dWeight2 = lr * e * xt[2]
        dWeight3 = lr * e * xt[3]

        model.bias += dBias
        model.weights[0] += dWeight0
        model.weights[1] += dWeight1
        model.weights[2] += dWeight2
        model.weights[3] += dWeight3
    # if epoch % 10 == 0:
    #     print(f"epoch: {epoch:5} done!")
# print(model)


# TESTING

for i in range(4):
    xt = data_set_X_one_hot[i]
    yp = model.forward(xt)

    print(f"{i}: {xt} --> {yp:12.6f}")