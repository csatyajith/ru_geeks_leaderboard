import datetime
import json
import os

from config import Config
from github_retriever import GithubRetriever
from slack_messenger import SlackMessenger


def get_leader_board(gr: GithubRetriever):
    path = "leaderboard_{}.json".format(datetime.date.today().strftime("%d_%m_%Y"))
    if os.path.exists(path):
        with open(path) as fp:
            return json.load(fp)
    scores = gr.get_scores()
    with open(path, "w") as fp:
        json.dump(scores, fp)
    return scores


def main():
    config = Config("config/local-config.json").get_config()
    gr = GithubRetriever(config["participants"], config)
    sm = SlackMessenger(config)
    scores = get_leader_board(gr)
    sorted_scores = sorted([(p, scores[p]) for p in scores], key=lambda x: -x[1])
    leaderboard_message = "Leetcode solution count leaderboard: \n"
    for s in sorted_scores:
        leaderboard_message = leaderboard_message + "{}: {} \n".format(s[0], s[1])
    sm.send_message(leaderboard_message)


if __name__ == '__main__':
    main()
