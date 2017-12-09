namespace AibgJebach
{
  public class BotServer
  {
    public readonly Bot Bot1;
    public readonly Bot Bot2;
    public readonly MapState MapState;
    private bool _isCurrentBotFirstBot = true;
    private int _movesLeft;

    public BotServer(IClient client)
    {
      this.Client = client;
      ServerStartingInformation ssi = client.GetServerStartingInformation();
      this.Bot1 = new Bot(ssi.Bot1StartingPosition, true);
      this.Bot2 = new Bot(ssi.Bot2StartingPosition, false);
      this.MapState = ssi.MapState;
      this._movesLeft = ssi.TotalMoves;
    }

    private IClient Client { get; }

    private Bot CurrentBot => this._isCurrentBotFirstBot ? this.Bot1 : this.Bot2;

    private Bot OtherBot => this._isCurrentBotFirstBot ? this.Bot2 : this.Bot1;

    public void NextStep(BotMove botMove)
    {
      this._movesLeft--;
      this._isCurrentBotFirstBot = !this._isCurrentBotFirstBot;
      //BotMove botMove = this.CurrentBot.IsBotNumberOne ? this.Client.GetBot1Move() : this.Client.GetBot2Move();

      CalculateNextState(this.CurrentBot, this.OtherBot, this.MapState, botMove);
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