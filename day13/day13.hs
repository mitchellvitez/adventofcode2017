import Data.Map.Strict (fromList, (!?), (!))

checkSingleScanner :: Int -> Int -> Bool
checkSingleScanner delay x =
  case input !? x of
    Nothing -> True
    Just v -> ((x + delay - 1) `mod` (v * 2 - 2)) /= 0

checkDelay :: Int -> Bool
checkDelay delay =
  any (checkSingleScanner delay) [1..90]

main =
  print $ head $ filter (not . checkDelay) [1..]

input = fromList [(0, 4), (1, 2), (2, 3), (4, 5), (6, 6), (8, 4), (10, 8), (12, 6), (14, 6), (16, 8), (18, 8), (20, 6), (22, 8), (24, 9), (26, 8), (28, 8), (30, 12), (32, 12), (34, 10), (36, 12), (38, 12), (40, 10), (42, 12), (44, 12), (46, 12), (48, 12), (50, 12), (52, 14), (54, 14), (56, 12), (58, 14), (60, 14), (62, 14), (64, 17), (66, 14), (70, 14), (72, 14), (74, 14), (76, 14), (78, 18), (82, 14), (88, 18), (90, 14)]