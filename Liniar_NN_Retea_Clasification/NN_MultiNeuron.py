from tkinter import X


class LiniarLayer:
    def __init__(self,x_size, y_size):
        # layer size
        self.x_size = x_size
        self.y_size = y_size

        # input layer
        self.x = [ 0 for i in range(x_size) ]
        self.b = [ 0 for j in range(y_size) ]
        self.w = [
            [ 0 for i in range(x_size) ] for j in range(y_size)
        ]

        # output layer
        self.y =[ 0 for j in range(y_size) ]

    def forward(self,x):
        # guarding input vector dimension
        if len(x) != self.x_size:
            print(f"ERROR: input size must be {self.x_size} but {len(x)} given")
            return
        # memorizing input values       
        self.x = x
        # computing forward pass

        for j in range(self.y_size):
            self.y[j] = sum([self.w[j][i] * self.x[i] for i in range(self.x_size)]) + self.b[j]
            # HW1: rewrite this part sum(compact for)
        return self.y

    def __str__(self):
        out = '-'*80 +'\n'

        for i in range(self.x_size):
            out += f'{self.x[i]:17.5f}'
        out +='\n'

        for i in range(self.x_size):
            out += f'{"||":>17}'
        out +='\n\n'

        for j in range(self.y_size):
            for i in range(self.x_size):
                out += f'     x{self.w[j][i]:11.5f}'

            out += f'     +{self.b[j]:11.5f}'
            out += f' > {self.y[j]:15.5f}'
        
            out +='\n'

        out += '-'*80+'\n'
        return out


hidden_layer = LiniarLayer(2,3)

hidden_layer.b[0]    = 1
hidden_layer.w[0][0] = 1
hidden_layer.w[0][1] = 1


hidden_layer.w[2][0] = 1


x=[1,1]

y = hidden_layer.forward(x)

print(hidden_layer)
print(y)
