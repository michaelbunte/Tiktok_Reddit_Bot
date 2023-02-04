from praw.models import MoreComments
import argparse
import re
from reddit_credentials import get_reddit_credentials

MAXCHARS = 300

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--red", help="subreddit to be chosen", required=True)
    parser.add_argument("-v", "--vids", help="number of videos to be created", required=True)
    args = vars(parser.parse_args())
    reddit = get_reddit_credentials()
    subreddit = reddit.subreddit(args['red'])

    for submission in subreddit.hot(limit = int(args['vids'])):
        print(submission.title)
        submission.comments.replace_more(limit=None)

        post_length = 0
        for top_level_comment in submission.comments:
            post_length += len(top_level_comment.body)
            print(top_level_comment.body)

            if(post_length >= MAXCHARS):
                break

        print('=' * 50)
