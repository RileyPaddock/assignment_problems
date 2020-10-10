from euler_estimator import EulerEstimator
# euler = EulerEstimator(derivative = (lambda x: x+1), point = (1,4))

# print("\n Testing starting point")
# assert euler.point == (1,4), 'Incorrect Starting point'
# print("     passed")
 
# print("\n Testing starting derivative")
# assert euler.calc_derivative_at_point() == 2, "Incorrect derivative at starting point"
# print("     passed")
 
# print("\n Testing point after first step")
# euler.step_forward(0.1)
# assert euler.point == (1.1, 4.2), 'Incorrect point after first step'
# print("     passed")
 
# print("\n Testing derivative after first step")
# assert euler.calc_derivative_at_point() == 2.1,'Incorrect derivative after first step'
# print("     passed")
 
# print("\n Testing point after 2nd step")
# euler.step_forward(-0.5)
# assert euler.point == (0.6, 3.15), 'Incorrect point after 2nd step'
# print("     passed")
 
# print("\n Testing go_to_input")
# euler.go_to_input(3, step_size = 0.5)
# assert euler.point == (3, 9.29), 'Incorrect final result'
# print("     passed")
 
# euler = EulerEstimator(derivative = (lambda x: x+1), point = (1,4))

# euler.plot([-5,5], step_size = 0.1, filename = 'plot.png')

# euler = EulerEstimator(
#                 derivatives = [
#                     (lambda x: x[0] + 1),
#                     (lambda x: x[0] + x[1]), 
#                     (lambda x: 2*x[1]) 
#                     ],
#                 point = (0,(0,0,0))
#             )

# print(euler.point)
#(0, (0, 0, 0))
# print(euler.calc_derivative_at_point())
#[1, 0, 0]

# euler.step_forward(0.1)
# print(euler.point)
#(0.1, (0.1, 0, 0))

# euler.calc_derivative_at_point()
# [1.1, 0.1, 0]
# euler.step_forward(-0.5)
# print(euler.point)
# (-0.4, (-0.45, 0.05, 0))

# euler.go_to_input(5, step_size = 2)

# notes to help you debug:

# point: (-0.4, (-0.45, 0.05, 0))
# derivative: (0.55, -0.4, -0.9)
# deltas: (2, (1.1, -0.8, -1.8))

# point: (1.6, (0.65, -0.75, -1.8))
# derivative: (1.65, -0.1, 1.3)
# deltas: (2, (3.3, -0.2, 2.6))

# point: (3.6, (3.95, -0.95, 0.8))
# derivative: (4.95, 3, 7.9)
# deltas: (1.4, (6.93, 4.2, 11.06))

# print(euler.point)
#(10.88, 3.25, 11.86)
# euler.plot([-5,5], step_size = 0.1, filename = 'plot.png')

# euler = EulerEstimator(
#                 derivatives = [
#                     (lambda x: 0.6*x[0] - 0.05*x[0]*x[1]),
#                     (lambda x: -0.9*x[1] + 0.02*x[0]*x[1])
#                     ],
#                 point = (0,(100,10))
#             )
euler = EulerEstimator(
                derivatives = [
                    (lambda x: -0.0003*x[1]*x[0]),
                    (lambda x: 0.0003*x[1]*x[0] - 0.02*x[1]),
                    (lambda x: 0.02*x[1])
                    ],
                point = (0,(1000,1,0))
            )
euler.plot([0,365], step_size = 0.001, filename = 'plot.png')