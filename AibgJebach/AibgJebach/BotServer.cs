using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AibgJebach
{
  public class BotServer
  {
    private bool isCurrentBotFirstBot = true;
    private Bot bot1, bot2;
    private Bot currentBot => this.isCurrentBotFirstBot ? this.bot1 : this.bot2;
    private MapState mapState;

    public BotServer(Bot bot1, Bot bot2)
    {
      this.bot1 = bot1;
      this.bot2 = bot2;
      this.mapState = new MapState(bot1, bot2);
    }

    public void NextStep()
    {
      this.isCurrentBotFirstBot = !this.isCurrentBotFirstBot;
      var botMove = this.currentBot.GetNextMove(this.mapState);

      var nextMapState = this.mapState.GetNextState(this.currentBot, botMove);

      if (nextMapState.IsOver == false)
      {
        this.mapState = nextMapState;
        this.NextStep();
      }
    }
  }
}
