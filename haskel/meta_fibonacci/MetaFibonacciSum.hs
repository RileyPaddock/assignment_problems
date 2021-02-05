fib :: (Integral a) => a -> a  
fib 0 = 0
fib 1 = 1 
fib n = fib (n - 2) + fib (n - 1) 


partialSumEntries k = [fibonacci | i <- [0..k], let fibonacci = fib i]

sumList :: [Integer] -> Integer
sumList [] = 0
sumList (x:xs) = x + sumList xs

partialSum k = sumList(partialSumEntries(k))

metaSumEntries n = [metaSum_ | j <- partialSumEntries n, let metaSum_ = partialSum j]

metaSum n = sumList(metaSumEntries(n))

main = print (metaSum 6)