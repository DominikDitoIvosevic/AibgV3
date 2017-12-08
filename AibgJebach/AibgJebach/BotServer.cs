namespace AibgJebach
{
  public class BotServer
  {
    private readonly Bot _bot1;
    private readonly Bot _bot2;
    private readonly MapState _mapState;
    private bool _isCurrentBotFirstBot = true;
    private int _movesLeft;

    public BotServer(IClient client)
    {
      this.Client = client;
      ServerStartingInformation ssi = client.GetServerStartingInformation();
      this._bot1 = new Bot(ssi.Bot1StartingPosition, true);
      this._bot2 = new Bot(ssi.Bot2StartingPosition, false);
      this._mapState = ssi.MapState;
      this._movesLeft = ssi.TotalMoves;
    }

    private IClient Client { get; }

    private Bot CurrentBot => this._isCurrentBotFirstBot ? this._bot1 : this._bot2;

    private Bot OtherBot => this._isCurrentBotFirstBot ? this._bot2 : this._bot1;

    public void NextStep()
    {
      this._movesLeft--;
      this._isCurrentBotFirstBot = !this._isCurrentBotFirstBot;
      BotMove botMove = this.CurrentBot.IsBotNumberOne ? this.Client.GetBot1Move() : this.Client.GetBot2Move();

      CalculateNextState(this.CurrentBot, this.OtherBot, this._mapState, botMove);

      if (!this.IsOver())
      {
        this.NextStep();
      }
    }

    private bool IsOver() => this._movesLeft <= 0;

    private static void CalculateNextState(Bot currentBot, Bot otherBot, MapState mapState, BotMove botMove)
    {
      MapAction mapAction = MapActionExtension.GetMapAction(currentBot.Position, otherBot.Position, botMove, mapState,
        currentBot.IsBotNumberOne);

      currentBot.Perspire();

      if ((mapAction & MapAction.BotAttack) != 0)
      {
        otherBot.BeAttacked(currentBot);
      }
      if ((mapAction & MapAction.BotMove) != 0)
      {
        currentBot.Move(botMove, mapAction);
      }
      if ((mapAction & MapAction.BotHeal) != 0)
      {
        currentBot.Heal();
      }
      if ((mapAction & MapAction.BotAcquireMine) != 0)
      {
        currentBot.Mine(otherBot, mapState);
      }
    }
  }
}