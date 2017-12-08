#region

using System;
using System.Collections.Generic;

#endregion

namespace AibgJebach
{
  public class MapState
  {
    public MapState(List<List<TileType>> tiles)
    {
      this.Tiles = tiles;
    }

    private List<List<TileType>> Tiles { get; }

    public TileType GetTile(Position currentPosition) => this.Tiles[currentPosition.posX][currentPosition.posY];

    public void AcquireMine(Bot bot)
    {
      TileType newTileType = bot.IsBotNumberOne ? TileType.MinePlayer1 : TileType.MinePlayer2;

      if (this.Tiles[bot.Position.posX][bot.Position.posY] == newTileType)
      {
        throw new InvalidOperationException("Already acquired");
      }

      this.Tiles[bot.Position.posX][bot.Position.posY] = newTileType;
    }
  }
}