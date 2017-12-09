#region

using System;

#endregion

namespace AibgJebach
{
  public class Position
  {
    public Position(int posX, int posY)
    {
      if (posX < 0 || posY < 0)
      {
        throw new InvalidOperationException("Invalid position");
      }

      this.posX = posX;
      this.posY = posY;
    }

    public int posX { get; }
    public int posY { get; }

    public Position Move(BotMove botMove)
    {
      switch (botMove)
      {
        case BotMove.East:
          return new Position(this.posX + 1, this.posY);
        case BotMove.West:
          return new Position(this.posX - 1, this.posY);
        case BotMove.North:
          return new Position(this.posX, this.posY - 1);
        case BotMove.South:
          return new Position(this.posX, this.posY + 1);
      }

      throw new InvalidOperationException("Invalid move");
    }

    public bool IsNeighbouring(Position otherPosition)
    {
      if (otherPosition.posY == this.posY && otherPosition.posX - 1 == this.posX
          || otherPosition.posY == this.posY && otherPosition.posX + 1 == this.posX
          || otherPosition.posX == this.posX && otherPosition.posY - 1 == this.posY
          || otherPosition.posX == this.posX && otherPosition.posY + 1 == this.posY)
      {
        return true;
      }

      return false;
    }
  }
}