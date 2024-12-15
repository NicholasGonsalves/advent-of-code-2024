import Data.List (sort)
import Data.Map qualified as Map
import Data.Maybe (fromMaybe)
import System.IO (readFile)

parseInput :: String -> [[Int]]
parseInput = map (map read . words) . lines

solvePart1 :: [[Int]] -> Int
solvePart1 lines = sum (zipWith (\a b -> abs (a - b)) firsts lasts)
  where
    firsts = sort [head line | line <- lines]
    lasts = sort [last line | line <- lines]

countOccurrences :: (Ord k) => [k] -> Map.Map k Int
countOccurrences = foldr (\x acc -> Map.insertWith (+) x 1 acc) Map.empty

solvePart2 :: [[Int]] -> Int
solvePart2 lines = sum (map (\x -> x * fromMaybe 0 (Map.lookup x lastsCount)) firsts)
  where
    firsts = sort [head line | line <- lines]
    lastsCount = countOccurrences [last line | line <- lines]

-- Main function to run the program
main :: IO ()
main = do
  input <- readFile "day1.txt"
  let parsed = parseInput input
  print $ solvePart1 parsed
  print $ solvePart2 parsed
