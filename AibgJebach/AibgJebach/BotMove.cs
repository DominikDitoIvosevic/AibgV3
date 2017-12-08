#region

using System.Collections.Generic;

#endregion

namespace AibgJebach
{
  public enum BotMove
  {
    North,
    South,
    East,
    West
  }

  public static class BotMoveExtensions
  {
    public static List<BotMove> PossibleMoves =>
      new List<BotMove> {BotMove.North, BotMove.South, BotMove.East, BotMove.West};
  }
}