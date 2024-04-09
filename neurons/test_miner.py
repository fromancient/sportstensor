import datetime as dt
from common.data import Sport, MatchPrediction
from common.predictions import make_match_prediction

def test():
  match_datetime = "2024-04-01 17:00"
  match_prediction = MatchPrediction(
    matchId = 1234,
    matchDatetime = dt.datetime.strptime(match_datetime, "%Y-%m-%d %H:%M"),
    sport = Sport.SOCCER,
    homeTeamName = "Arsenal",
    awayTeamName = "Chelsea",
  )
  match_prediction = make_match_prediction(match_prediction)

  print(f"Match Prediction for {match_prediction.awayTeamName} at {match_prediction.homeTeamName} on {match_datetime}: \
  {match_prediction.awayTeamName} {match_prediction.awayTeamScore}, {match_prediction.homeTeamName} {match_prediction.homeTeamScore}"
  )

if __name__ == "__main__":
  test()