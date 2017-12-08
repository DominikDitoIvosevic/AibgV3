#region

using System;

#endregion

namespace AibgJebach
{
  [Flags]
  public enum MapAction
  {
    BotAttack = 1 << 1,
    BotHeal = 1 << 2,
    BotAcquireMine = 1 << 3,
    BotStay = 1 << 4,
    BotMove = 1 << 5
  }

  public static class MapActionExtension
  {
    public static MapAction GetMapAction(
      Position currentPosition,
      Position otherHeroPosition,
      BotMove botMove,
      MapState mapState,
      bool isBotNumberOne)
    {
      TileType currentTile = mapState.GetTile(currentPosition);
      Position targetPosition = currentPosition.Move(botMove);
      TileType targetTile = mapState.GetTile(targetPosition);

      MapAction action = 0;

      switch (targetTile)
      {
        case TileType.Hero1:
        case TileType.Hero2:
        case TileType.Obstacle:
          action |= MapAction.BotStay;
          break;

        case TileType.CoffeeMachine:
        case TileType.MineNeutral:
        case TileType.MinePlayer1:
        case TileType.MinePlayer2:
          action |= MapAction.BotMove;
          currentTile = targetTile;
          break;
      }

      switch (currentTile)
      {
        case TileType.MineNeutral:
          action |= MapAction.BotAcquireMine;
          break;
        case TileType.MinePlayer1:
          if (isBotNumberOne == false)
          {
            action |= MapAction.BotAcquireMine;
          }
          break;
        case TileType.MinePlayer2:
          if (isBotNumberOne)
          {
            action |= MapAction.BotAcquireMine;
          }
          break;
        case TileType.CoffeeMachine:
          action |= MapAction.BotHeal;
          break;
      }

      if (targetPosition.IsNeighbouring(otherHeroPosition))
      {
        action |= MapAction.BotAttack;
      }

      return action;
    }
  }
}