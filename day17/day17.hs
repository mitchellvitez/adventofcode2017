f :: Int -> Int -> Int -> Int -> Int
f idx buflen num buf1
  | num > 50000000 = buf1
  | otherwise = 
      let newidx = (idx + 337) `rem` buflen in
      f (newidx+1) (buflen+1) (num+1) (if newidx == 0 then num else buf1)

main = print $ f 0 1 1 0
