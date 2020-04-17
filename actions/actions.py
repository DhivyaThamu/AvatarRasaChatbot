from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import os


#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionFindAvatar(Action):

    def name(self) -> Text:
        print("Action action_find_avatar")
        return "action_find_avatar"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        style = tracker.get_slot("style")
        gender = tracker.get_slot("gender")

        dispatcher.utter_message(template="utter_avatar_found")

        url = get_avatar_svc() + '/' + style + '/' + gender

        dispatcher.utter_message(image=url)

        return []


def get_avatar_svc():
    """
    Retrieves host serving the Avatar images
    :return:
    """
    return str(os.environ.get("AVATAR_SVC", 'http://localhost:5000'))
