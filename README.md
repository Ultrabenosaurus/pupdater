pupdater
========

An importable python module for checking if a GitHub repo has a new release.

__Current Version: 1.1__ ([changelog](#changelog))

## Install

Honestly, I have no clue other than I know it works from the same directory as the script you want to use it in. I think it might work if you put it in your path, but then your script isn't distributable.

Python seems unecessarily awkward about using code in other files, especially classes. I read some SO threads about `__init__.py` files in nested directories but that shit makes no sense.

PHP is literally infinity times better at this than python.

## Use

This bit is pretty easy, if I say so myself.

```python
import Updater

upd = Updater.New("Ultrabenosaurus/EasyXdcc", "1.2")
print upd.Simple()
print upd.Main()
```

`Updater.Simple()` and `Updater.Main()` aren't both supposed to be called, usually you'd just pick one or the other. The former will return `True` if there's a newer version than you specified in `Updater.New()` and `False` if not, while the latter will give you strings to feed straight to your users.

You can also provide custom text output for `Updater.Main()` by the named arguments `new_full`, `new_short` and `no_new` (in any order) after the repo name and version number.

```python
import Updater

upd = Updater.New("Ultrabenosaurus/EasyXdcc", "1.2",
    new_short="A new version of $repo$ is available.",
    new_full="Please visit https://github.com/$repo$/releases/tag/$latest$ for the latest version.",
    no_new="Your version $current$ is the newest available."
)
```

To output the `new_short` text simply call `Updater.Main("short")`.

As for the placeholders, they should be pretty self-explanatory but just to make sure:

* `$repo$` is the repo name in the format `user/package`
* `$latest$` is the version number of the latest tag found via the [GitHub tags API](https://developer.github.com/v3/repos/#list-tags)
* `$current$` is the version number you passed when calling `Updater.New()`

Don't worry about tag names having a leading "v" like `v1.2` because Updater strips that off, same for the version you pass to `Updater.New()`, but that's all it knows to ignore. Version numbers with more parts, like 1.2.8, do work properly but something like an alpha release of 1.2.8a will not.

## TODO

* option to automatically download and extract new version
* figure out module importing and properly package

## Changelog

### 1.1

* the output of `Updater.Main()` is now customisable
  * `new_full` for a long message (direct to user)
  * `new_short` for a shortened version (subtle reminder?)
  * `no_new` for when the current version is the latest
* order of repo name and current version number have been swapped
* order or lack of following parameters doesn't matter

### 1.0

* initial release
* can check if there's a new release on a GitHub repo
  * `True`/`False`
  * string output
* that's basically it for now
