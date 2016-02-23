
import urllib2, json

#
# check the GitHub API for the latest tag release of a given
# repo and compare with the given version number
#
# can return a simple True/False if there's a newer version
# or give a message to show your users
#
# example:
# import Updater
# upd = Updater.New("1.2","Ultrabenosaurus/EasyXdcc")
# print upd.Simple()
# print upd.Main()
#

class Updater:

    # ver       current version of script
    # repo      GitHub repo to query for update
    # text      text prompt to return for alerting the user, set to false/blank to return nothing
    #           use $ as a placeholder for the latest version number in your custom message
    def __init__(self, ver, repo, text=None):
        self.ver = ver
        self.repo = repo
        if text is None:
            self.text = "Version $ of " + repo + " is now available, you are running " + ver + ". Please visit https://github.com/" + repo + "/releases/tag/$ for more information."
        else:
            self.text = text
        self.new = False

    # return messages to tell users the latest version
    def Main(self):
        if self.isOld():
            return self.text.replace("$", self.new)
        else:
            return "You are running the latest version available."

    # return True if there's a newer version, otherwise False
    def Simple(self):
        if self.isOld():
            return True
        else:
            return False

    # ping the GitHub API and compare the given version to the latest tag
    def isOld(self):
        url = "https://api.github.com/repos/" + self.repo + "/tags"

        data = urllib2.Request(url)
        opener = urllib2.build_opener()
        source = opener.open(data).read();
        latest = json.loads(source)[0]['name']
        if latest.replace("v", "") > self.ver.replace("v", ""):
            self.new = latest
            return True
        else:
            return False

# because apparently python doesn't like using classes for importable modules
def New(ver, repo, text=None):
    return Updater(ver, repo, text)
