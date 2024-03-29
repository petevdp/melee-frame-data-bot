"""
centralized config for things that you would want to quickly change. Should be
completely static.
"""
import re
import os

from . import creds
from ..definitions import ROOT_DIR, LOG_DIR, TREE_PATH

develop = True


class ServiceAccount:
    creds = creds.service_account_creds


class Client:
    token = creds.discord_token
    command_prefix = "$d"
    activity_msg = "{} help for Commands".format(command_prefix)


class Handler:
    command_prefix = Client.command_prefix


class HandleArgs:
    min_match_percent = 80


class Root:
    sheet_url = "https://docs.google.com/spreadsheets/d/12dwtMFdi95l03npBFuWI0fK62V0QZ6xET3qJ4oVdGc0&edit#gid=1165995726"
    sheet_id = re.search("id\=", sheet_url).end()
    char_names = {
        "Fox",
        "Falco",
        "Marth",
        "Samus",
        "Sheik",
        "Jigglypuff",
        "Peach",
        "Ice Climbers",
        "Captain Falcon",
        "Pikachu",
        "Samus",
        }
    contrib_list = ["sp99", "cfx"]
    # TODO dynamically determine correct client id
    invite_link = "https://discordapp.com/oauth2/authorize?client_id=492378733399900169&scope=bot&permissions=67584"


class CharacterNames:
    char_names = list(Root.char_names)


class Suggest:
    class Response:
        suggestion_que_loc = os.path.join(ROOT_DIR, 'suggestionQueue.json')


class HelpResponse:
    contrib_list = ["sp99", "cfx"]


class WrittenMSG:
    message_file = os.path.join(os.path.dirname(__file__),
                                "messages.yaml")
