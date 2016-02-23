import urllib2, json

#
# Ulltrabenosaurus/Updater
#
# check the GitHub API for the latest tag release of a given
# repo and compare with the given version number
#
# can return a simple True/False if there's a newer version
# or give a message to show your users
#
# example:
# import Updater
# upd = Updater.New("Ultrabenosaurus/EasyXdcc", "1.2")
# print upd.Simple()
# print upd.Main()
#

class Updater:

    # @required
    # repo          GitHub repo to query for update
    # ver           current version of script
    #
    # @optional
    # new_full      long string to return for alerting the user of an available update
    # new_short     short string to return for alerting the user of an available update
    #           use $latest$ as a placeholder for the LATEST VERSION in your custom message
    #           use $current$ as a placeholder for the CURRENT VERSION in your custom message
    #           use $repo$ as a placeholder for the REPO NAME in your custom message
    # no_new        string to return if no newer version found
    def __init__(self, repo, ver, **kwargs):
        self.ver = ver
        self.repo = repo

        if not kwargs.has_key("new_full"):
            self.new_full = "Version $latest$ of $repo$ is now available, you are running $current$. Please visit https://github.com/$repo$/releases/tag/$latest$ for more information."
        else:
            self.new_full = kwargs["new_full"]

        if not kwargs.has_key("new_short"):
            self.new_short = "New version available from https://github.com/$repo$/releases/tag/$latest$"
        else:
            self.new_short = kwargs["new_short"]

        if not kwargs.has_key("no_new"):
            self.no_new = "You are running the latest version available."
        else:
            self.no_new = kwargs["no_new"]

        self.new = None
        self.isOld()

    # return messages to tell users the latest version
    def Main(self, which="full"):
        if self.new is None:
            self.isOld()

        if self.new:
            if "full" == which:
                return self.prepString(self.new_full)
            else:
                return self.prepString(self.new_short)
        else:
            return self.prepString(self.no_new)

    # return True if there's a newer version, otherwise False
    def Simple(self):
        if self.new is None:
            self.isOld()

        if self.new:
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
        if str(latest).replace("v", "") > str(self.ver).replace("v", ""):
            self.new = latest
            return True
        else:
            return False

    # parse the output strings to replace the symbols
    def prepString(self, string):
        return string.replace("$latest$", str(self.new)).replace("$current$", str(self.ver)).replace("$repo$", self.repo)

# because apparently python doesn't like using classes for importable modules
def New(ver, repo, **kwargs):
    return Updater(ver, repo, **kwargs)
