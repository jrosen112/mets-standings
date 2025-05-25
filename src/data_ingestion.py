import requests
import pprint

NL_EAST_STANDINGS_URL = "http://statsapi.mlb.com/api/v1/standings/?leagueId=104"
METS_TEAM_URL = "http://statsapi.mlb.com/api/v1/teams/121"
CITI_FIELD_URL = "http://statsapi.mlb.com/api/v1/venues/3289"

def make_request(req_url: str) -> dict:
    response = requests.get(req_url)
    return response.json()

def main():
    response = make_request(CITI_FIELD_URL)
    pprint.pprint(response)

if __name__ == "__main__":
    main()