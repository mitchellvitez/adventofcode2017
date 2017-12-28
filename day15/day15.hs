import Data.Bits
import Control.Parallel.Strategies

f1 :: Int -> Int -> Int -> Int -> Int
f1 a b i total
  | i < 40000000 =
    let newtotal = if (a .&. 0xFFFF) == (b .&. 0xFFFF) then total + 1 else total in
    f1 ((a * 16807) `rem` 2147483647) ((b * 48271) `rem` 2147483647) (i+1) newtotal
  | otherwise = total

newA a =
  let a' = (a * 16807) `rem` 2147483647
  in if a' `rem` 4 == 0 then a' else newA a'

newB b =
  let b' = (b * 48271) `rem` 2147483647
  in if b' `rem` 8 == 0 then b' else newB b'

p :: Int -> Int -> (Int, Int)
p a b =
  runEval $ do
    a' <- rpar (newA a)
    b' <- rpar (newB b)
    rseq a'
    rseq b'
    return (a',b')

f2 :: Int -> Int -> Int -> Int -> Int
f2 a b i total
  | i < 5000000 =
    let (a', b') = (newA a, newB b)
        newtotal = if (a' .&. 0xFFFF) == (b' .&. 0xFFFF) then total + 1 else total
    in f2 a' b' (i+1) newtotal
  | otherwise = total

main =
  print $ runEval $ do
    f1ans <- rpar (f1 703 516 0 0)
    f2ans <- rpar (f2 703 516 0 0)
    -- rseq f1ans
    -- rseq f2ans
    return (f1ans, f2ans)

  -- print $ f1 703 516 0 0
  -- print $ f2 703 516 0 0 

