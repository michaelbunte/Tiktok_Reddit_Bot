from praw.models import MoreComments
import argparse
import re
import json
from reddit_credentials import get_reddit_credentials

MAXCHARS = 300

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--red", help="subreddit to be chosen", required=True)
    parser.add_argument("-v", "--vids", help="number of videos to be created", required=True)
    args = vars(parser.parse_args())
    reddit = get_reddit_credentials()
    subreddit = reddit.subreddit(args['red'])

    top_posts = {
        "posts": []
    }
    for submission in subreddit.hot(limit = int(args['vids'])):
        print(submission.title)
        submission.comments.replace_more(limit=None)

        post_length = 0
        top_comments = []
        for top_level_comment in submission.comments:
            post_length += len(top_level_comment.body)
            print(top_level_comment.body)
            top_comments.append(top_level_comment.body)
            if(post_length >= MAXCHARS):
                break

        top_posts['posts'].append({
            "posts": submission.title,
            "top_comments": top_comments
        })

        print('=' * 50)

    
    json_object = json.dumps(top_posts, indent=4)
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
