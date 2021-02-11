getFactors n = [i | i <- [1..n], n `mod` i == 0]
sumFactors n = sum(getFactors(n))
main = print(sumFactors 10)