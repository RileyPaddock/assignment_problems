sumPerfectCubes x = sum([ n*n*n| n <- [1..x]])

main = print(sumPerfectCubes(10))