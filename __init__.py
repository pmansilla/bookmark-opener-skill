from mycroft import MycroftSkill, intent_file_handler


class BookmarkOpener(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('opener.bookmark.intent')
    def handle_opener_bookmark(self, message):
        self.speak_dialog('opener.bookmark')


def create_skill():
    return BookmarkOpener()

