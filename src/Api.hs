{-# LANGUAGE DuplicateRecordFields, DeriveGeneric, DeriveAnyClass, DataKinds, TypeOperators #-}
module Api where

import Common
import Servant.API

data Response = Response
    { game :: Game
    , hero :: Hero
    , token :: Text
    , viewUrl :: Text
    , playUrl :: Text }
    deriving (Eq, Ord, Read, Show, Generic, FromJSON)

data Game = Game
    { id :: Text
    , turn :: Int
    , maxTurns :: Int
    , heroes :: [Hero]
    , board :: Board
    , finished :: Bool }
    deriving (Eq, Ord, Read, Show, Generic, FromJSON)

data Hero = Hero
    { id :: Int
    , name :: Text
    , userId :: Maybe Text
    , pos :: Coords
    , lastDir :: Maybe Direction
    , life :: Int
    , gold :: Int
    , mineCount :: Int
    , spawnPos :: Coords
    , crashed :: Bool }
    deriving (Eq, Ord, Read, Show, Generic, FromJSON)

data Direction = North | West | East | South | Stay
    deriving (Eq, Ord, Read, Show, Generic, FromJSON, ToJSON)

data Board = Board
    { size :: Int
    , tiles :: Text }
    deriving (Eq, Ord, Read, Show, Generic, FromJSON)

data Coords = Coords
    { x :: Int
    , y :: Int }
    deriving (Eq, Ord, Read, Show, Generic, FromJSON)

-- AnalDestroyer: 9wydbx82

data TrainingPayload = TrainingPayload
    { key :: Text }
    deriving (Eq, Ord, Read, Show, Generic, ToJSON)

data PlayPayload = PlayPayload
    { key :: Text
    , dir :: Direction }
    deriving (Eq, Ord, Read, Show, Generic, ToJSON)

type Api = "api" :>
    (    "training" :> ReqBody '[JSON] TrainingPayload :> Post '[JSON] Response
    :<|> Capture "gamekey" Text :> Capture "fragment" Text :> "play"
        :> ReqBody '[JSON] PlayPayload :> Post '[JSON] Response
    )
