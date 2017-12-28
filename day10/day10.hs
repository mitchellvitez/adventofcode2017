
rounds remaining pos skip l [] =
  rounds (remaining-1) pos skip l i
rounds remaining pos skip l i =
    
i = map ord s ++ [17, 31, 73, 47, 23]

hash s = hex $ dense $ rounds 64 0 0 [0..255]

main = print $ hash input

input = "70,66,255,2,48,0,54,48,80,141,244,254,160,108,1,41"
