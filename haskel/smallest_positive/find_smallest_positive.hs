findSmallestPositive :: (Num a, Ord a) => [a] -> a  
findSmallestPositive [] = error "smallest positive of empty list"  
findSmallestPositive [x] = x  
findSmallestPositive (x:xs)
    | x>0 && x < maxTail = x
    | otherwise = maxTail  
    where maxTail = findSmallestPositive xs

main = print(findSmallestPositive[1,2,3])