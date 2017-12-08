#region

using System.Collections.Generic;

#endregion

namespace AibgJebach
{
  public class Bot
  {
    public readonly List<Position> OwnedMines;
    public int Health, Mines, Coins;
    public Position Position;

    public Bot(Position startingPosition, bool isBotNumberOne)
    {
      this.IsBotNumberOne = isBotNumberOne;
      this.StartingPosition = startingPosition;
      this.OwnedMines = new List<Position>();
    }

    public bool IsBotNumberOne { get; }
    private Position StartingPosition { get; }

    public void Move(BotMove botMove, MapAction mapAction)
    {
      if ((mapAction | MapAction.BotMove) != 0)
      {
        this.Position = this.Position.Move(botMove);
      }
    }

    public void BeAttacked(Bot attackingBot)
    {
      this.Health -= 20;
      if (this.Health <= 0)
      {
        this.Health = 100;
        this.OwnedMines.Clear();
        attackingBot.AcquireMines(this.OwnedMines);
      }
    }

    public void Heal()
    {
      if (this.Coins >= 2)
      {
        this.Coins -= 2;
        this.Health += 50;
        if (this.Health > 100)
        {
          this.Health = 100;
        }
      }
    }

    public void AcquireMines(List<Position> newMines)
    {
      this.OwnedMines.AddRange(newMines);
    }

    public void AcquireMine(Position newMine)
    {
      this.OwnedMines.Add(newMine);
    }

    public void Mine(Bot otherBot, MapState mapState)
    {
      this.BeAttacked(otherBot);
      if (this.Health != 100)
      {
        //Hasn't died
        this.AcquireMine(this.Position);
        mapState.AcquireMine(this);
      }
    }

    public void Perspire()
    {
      if (this.Health > 1)
      {
        this.Health--;
      }
    }
  }
}