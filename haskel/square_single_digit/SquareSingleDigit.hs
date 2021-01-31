squareSingleDigitNumbers x = map(^2) (filter(<10) x)

main = print(squareSingleDigitNumbers [2, 7, 15, 11, 5])