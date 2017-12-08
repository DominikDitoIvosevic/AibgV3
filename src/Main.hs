module Main where

import Common
import Graphics.Gloss

main :: IO ()
main = display
    (InWindow "Hello" (800, 500) (10, 10))
    black
    (color white $ Circle 300)
