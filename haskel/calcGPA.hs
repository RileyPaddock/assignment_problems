sumGPA x = sum([ number| grade <- x, let number = if grade == "A" then 4 else  if grade == "B" then 3 else if grade == "C" then 2 else if grade == "D" then 1 else 0])

calcGPA x = sumGPA(x)`div`length(x)

main = print(calcGPA(["A", "B", "B", "C", "C", "C", "D", "F"]))