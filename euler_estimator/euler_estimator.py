class EulerEstimator:
    def __init__(self,derivative,point):
        self.derivative = derivative
        self.point = point

    def calc_derivative_at_point(self):
        return self.derivative(self.point[0])

    def step_forward(self, step_size):
        derivative = self.calc_derivative_at_point()
        self.point = (round(self.point[0]+step_size,3), round(self.point[1]+(step_size * derivative),3))

    def go_to_input(self, stop_x, step_size):
        while self.point[0] < stop_x:
            if self.point[0] + step_size <= stop_x:
                self.step_forward(step_size)
            else:
                step_size = (stop_x - self.point[0])
                self.step_forward(step_size)
        return self.point


