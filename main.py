#!/usr/bin/env python
import logging
from os import getenv

from github import Github
from github.GithubException import UnknownObjectException
from tabulate import tabulate

GITHUB_THREAD_URL_PREFIX = "https://github.com"


def get_drama_input(path):
    with open(path) as drama:
        return drama.readlines()


def get_parsed_drama_links(urls):
    return [
        parse_url(url) for url in urls
    ]


def add_repos(dramas):
    filtered_dramas = []
    for drama in filter(None, dramas):
        try:
            drama['repo'] = get_repo(
                drama['username'],
                drama['project_name']
            )
            filtered_dramas.append(drama)
            logging.debug(f"Added repo for {drama}")
        except UnknownObjectException:
            logging.warn(f"No GitHub repo found for {drama}")
        except Exception:
            logging.error(f"Could not retrieve info for {drama}")
    return filtered_dramas


def add_threads(dramas):
    for drama in dramas:
        if drama['thread_type'] in ["issues", "pull"]:
            drama['thread'] = drama['repo'].get_issue(drama['thread_id'])
            logging.debug(f"Added thread for {drama}")
    return dramas


def get_urls_from_text(text_lines, url_prefix):
    return [
        line.rstrip("\n").split(url_prefix)[1].split("/")[1:5]
        for line in text_lines
        if f"({url_prefix}" in line
    ]


def parse_url(url):
    try:
        return {
            "username": url[0],
            "project_name": url[1],
            "thread_type": url[2],
            "thread_id": int(url[3].rstrip(")")),
        }
    except IndexError:
        logging.warn(f"Could not parse {url}")
    except ValueError:
        logging.warn(f"Could not parse {url}")


def get_repo(owner, repo_name):
    github_token = getenv("GITHUB_TOKEN")
    gconn = Github(github_token)
    return gconn.get_repo(f"{owner}/{repo_name}")


def dramanalyze(dramas):
    commenters = {}
    for drama in dramas:
        logging.info(f"Processing {drama}")
        for comment in drama['thread'].get_comments():
            if comment.user.login not in commenters:
                logging.info(f"Found new user {comment.user.login}")
                commenters.update(
                    {
                        comment.user.login: {
                            "user": comment.user,
                            #  "reactions": [],
                            "count": 1,
                        }
                    }
                )
                #  commenters[comment.user.login]['reactions'].append([
                #      reaction for reaction in comment.get_reactions()
                #  ])
            else:
                logging.info(f"Found existing user {comment.user.login}")
                commenters[comment.user.login]['count'] += 1
                #  commenters[comment.user.login]['reactions'].append([
                #      reaction for reaction in comment.get_reactions()
                #  ])
    return commenters


def main():
    logging.basicConfig(
        filename="dramanalyzer.log",
        level=logging.INFO
    )
    text_source = "./github-drama/README.md"
    text_lines = get_drama_input(text_source)
    drama_links = get_urls_from_text(text_lines, GITHUB_THREAD_URL_PREFIX)
    dramas = get_parsed_drama_links(drama_links)
    logging.debug(dramas)
    dramas_with_repos = add_repos(dramas)
    dramas_with_threads = add_threads(dramas_with_repos)
    commenter_data = dramanalyze(dramas_with_threads)
    headers = ["Username", "Full name", "Comment count"]
    tabulated = [
        [commenter, data['user'].name, data['count']]
        for commenter, data in commenter_data.items()
    ]
    print(tabulate(tabulated, headers=headers))


if __name__ == "__main__":
    main()
