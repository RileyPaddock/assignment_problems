import matplotlib.pyplot as plt
class EulerEstimator:
    def __init__(self,derivatives,point):
        self.derivatives = derivatives
        self.point = point

    def calc_derivative_at_point(self):
        derivatives = []
        for x in range(len(self.derivatives)):
            derivatives.append(self.derivatives[x](self.point[1]))
        return derivatives

    def step_forward(self, step_size):
        derivatives = self.calc_derivative_at_point()
        new_points = [self.point[1][x] + (step_size*derivatives[x]) for x in range(len(derivatives))]
        self.point = (self.point[0]+step_size, tuple(new_points))
        
    def go_to_input(self, stop_x, step_size):
        while abs(self.point[0]) < abs(stop_x):
            derivatives = self.calc_derivative_at_point()
            print("\nPoint: " + str(self.point))
            print("derivative: "+str(derivatives))
            print("Delta: "+str(step_size)+","+ str([(step_size*derivatives[x]) for x in range(len(derivatives))]))
            if self.point[0] + step_size <= stop_x:
                self.step_forward(step_size)
            else:
                step_size = (stop_x - self.point[0])
                self.step_forward(step_size)
        return self.point

    def plot(self, interval, step_size, filename):
        start_point = [point for point in self.point]
        positive_coord_set = self.positive_movement(interval,step_size)
        self.point = start_point
        negative_coord_set = self.negative_movement(interval,step_size)

        for negative_set in negative_coord_set[1]:
            negative_set = negative_set[::-1]
        x_coords_negative = negative_coord_set[0][::-1]
        y_coords = []
        for i in range(len(self.derivatives)):
            y_coords.append(negative_coord_set[1][i] + positive_coord_set[1][i])
        #print(x_coords[0])
        x_coords = x_coords_negative + positive_coord_set[0]
        x_coords = x_coords[::-1]
        plt.style.use('bmh')
        for coord_set in y_coords:
            plt.plot(x_coords,coord_set,linewidth = 2.5)
        plt.legend(['Recovered','Infected','Susceptible'])
        plt.title("SIR model")
        plt.savefig(filename)

    def positive_movement(self, interval, step_size):
        y_coords = [[] for _ in range(len(self.derivatives))]
        x_coords = []
        while self.point[0] < interval[1]:
            if self.point[0] + step_size <= interval[1]:
                self.step_forward(step_size)
            else:
                adjusted_step_size = (interval[1] - self.point[0])
                self.step_forward(adjusted_step_size)
            for x in range(len(self.derivatives)):
                y_coords[x].append(self.point[1][x])
            x_coords.append(self.point[0])
        return x_coords, y_coords

    def negative_movement(self,interval,step_size):
        y_coords = [[] for _ in range(len(self.derivatives))]
        x_coords = []
        while self.point[0] > interval[0]:
            if self.point[0] + -1 * step_size >= interval[0]:
                self.step_forward(-1*step_size)
            else:
                adjusted_step_size = (interval[0] + self.point[0])
                self.step_forward(adjusted_step_size)
            for x in range(len(self.derivatives)):
                y_coords[x].append(self.point[1][x])
            x_coords.append(self.point[0])
        return x_coords, y_coords
