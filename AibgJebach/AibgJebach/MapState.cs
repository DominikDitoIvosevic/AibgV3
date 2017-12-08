using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AibgJebach
{
  public class MapState
  {
    private Bot bot1, bot2;
    private int stepsLeft;

    public MapState(int totalSteps, Bot bot1, Bot bot2)
    {
      this.stepsLeft = totalSteps;
      this.bot1 = bot1;
      this.bot2 = bot2;
    }

    public MapState GetNextState(Bot currentBot, BotMove botMove)
    {
      int posX = currentBot.PosX;
      int posY = currentBot.PosY;


    }

    public bool IsOver => this.stepsLeft <= 0;

    
  }
}
