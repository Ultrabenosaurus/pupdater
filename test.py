import Updater

print "default output"
upd = Updater.New("Ultrabenosaurus/EasyXdcc", "1.2")
print "SIMPLE:\n\t%s" % upd.Simple()
print "NEW-FULL:\n\t" + upd.Main()
print "NEW-SHORT:\n\t" + upd.Main("short")

upd = Updater.New("Ultrabenosaurus/EasyXdcc", "9.9")
print "NO-NEW:\n\t" + upd.Main()

print "\ncustom output"
upd = Updater.New("Ultrabenosaurus/EasyXdcc", "1.2",
    new_short="A new version of $repo$ is available.",
    new_full="Please visit https://github.com/$repo$/releases/tag/$latest$ for the latest version."
)
print "SIMPLE:\n\t%s" % upd.Simple()
print "NEW-FULL:\n\t" + upd.Main()
print "NEW-SHORT:\n\t" + upd.Main("short")
upd = Updater.New("Ultrabenosaurus/EasyXdcc", "9.9",
    no_new="Your version $current$ is the newest available."
)
print "NO-NEW:\n\t" + upd.Main()
