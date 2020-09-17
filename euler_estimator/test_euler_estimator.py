from euler_estimator import EulerEstimator
euler = EulerEstimator(derivative = (lambda x: x+1), point = (1,4))

print("\n Testing starting point")
assert euler.point == (1,4), 'Incorrect Starting point'
print("     passed")
 
print("\n Testing starting derivative")
assert euler.calc_derivative_at_point() == 2, "Incorrect derivative at starting point"
print("     passed")
 
print("\n Testing point after first step")
euler.step_forward(0.1)
assert euler.point == (1.1, 4.2), 'Incorrect point after first step'
print("     passed")
 
print("\n Testing derivative after first step")
assert euler.calc_derivative_at_point() == 2.1,'Incorrect derivative after first step'
print("     passed")
 
print("\n Testing point after 2nd step")
euler.step_forward(-0.5)
assert euler.point == (0.6, 3.15), 'Incorrect point after 2nd step'
print("     passed")
 
print("\n Testing go_to_input")
euler.go_to_input(3, step_size = 0.5)
assert euler.point == (3, 9.29), 'Incorrect final result'
print("     passed")
 