namespace AibgJebach
{
  public class ServerStartingInformation
  {
    public ServerStartingInformation(
      Position bot1StartingPosition,
      Position bot2StartingPosition,
      MapState mapState,
      int totalMoves)
    {
      this.Bot1StartingPosition = bot1StartingPosition;
      this.Bot2StartingPosition = bot2StartingPosition;
      this.MapState = mapState;
      this.TotalMoves = totalMoves;
    }

    public Position Bot1StartingPosition { get; }
    public Position Bot2StartingPosition { get; }
    public MapState MapState { get; }
    public int TotalMoves { get; }
  }
}