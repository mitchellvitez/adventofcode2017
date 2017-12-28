{-# LANGUAGE OverloadedLists #-}
import qualified Data.Set as Set
import qualified Data.Vector as V
import Data.Ord

import Data.Maybe
import Data.List

maxBank :: V.Vector Int -> (Int, Int)
maxBank banks = V.maximumBy (comparing snd) $ V.zip [0..] banks

initialBanks :: V.Vector Int
initialBanks = [14,0,15,12,11,11,3,5,1,6,8,4,9,1,8,4]
-- initialBanks = [0,2,7,0]

minicycle :: Int -> Int -> V.Vector Int -> V.Vector Int
minicycle 0 _ banks = banks
minicycle blocks i banks =
  let j = (i + 1) `mod` length banks
  in minicycle (blocks-1) j $ banks V.// [(j, banks V.! j + 1)]

cycle :: V.Vector Int -> Int -> Set.Set (V.Vector Int) -> Int
cycle banks iters seen =
  if banks `Set.member` seen then iters
  else
    let (i, blocks) = maxBank banks
        newBanks = minicycle blocks i $ banks V.// [(i, 0)]
    in Main.cycle newBanks (iters + 1) (Set.insert banks seen)

-- cycle' :: V.Vector Int -> Int -> [V.Vector Int] -> ()
cycle' banks iters seen =
  if banks `elem` seen then (iters, seen, banks)
  else
    let (i, blocks) = maxBank banks
        newBanks = minicycle blocks i $ banks V.// [(i, 0)]
    in Main.cycle' newBanks (iters + 1) (banks:seen)

main = do
  print $ Main.cycle initialBanks 0 Set.empty
  let (iters, seen, banks) = Main.cycle' initialBanks 0 []
  print $ iters - fromJust (elemIndex banks (reverse seen))

