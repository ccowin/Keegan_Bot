#!/usr/bin/env python3
import praw
# my credentials are saved to a file credentials.py as praw.Reddit object
import credentials


keegan = 'keegan murray'
reply = '''Keegan Murray!
***
^^this ^^is ^^a ^^[bot!](https://www.github.com/ccowin/Keegan_Bot) ^^by ^^/u/Narpity'''

opt_out = ['narpity']
comment_list = []


def main():
    reddit = credentials.get_credentials()

    subreddit = reddit.subreddit('kings')

    for comment in subreddit.stream.comments():
        process_comments(comment)


def process_comments(comment):
    # dont comment on the same comment:
    if comment in comment_list:
        return

    # Ignore users who have opted out
    if comment.author in opt_out:
        return

    # Ignore titles with more than 10 words as they probably are not simple questions.
    if len(comment.body.split()) > 2:
        return

    normalized_title = comment.body.lower()

    if keegan in normalized_title:
        print(f"Replied to: {comment.author}")
        comment.reply(reply)
        comment_list.append(comment)


if __name__ == "__main__":
    main()
