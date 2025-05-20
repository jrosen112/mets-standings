import requests
import pprint
from Division import Division

MLB_BASE_URL = "https://statsapi.mlb.com/api/v1/"
BASEBALL_URL_PARAM = "divisions?sportId=1"

def make_request(req_url: str) -> dict:
    response = requests.get(req_url)
    return response.json()

def construct_url(division: Division = None) -> str:
    if not division:
        return MLB_BASE_URL + BASEBALL_URL_PARAM
    # TODO: return link for data for that div's leaderboard
    # return MLB_BASE_URL + "divisions?" + BASEBALL_URL_PARAM + "&" + division.value.get("link")

def main():
    # url = construct_url(Division.NLE)
    url = construct_url()
    response = make_request(url)
    pprint.pprint(response)

if __name__ == "__main__":
    main()