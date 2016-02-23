pupdater
========

An importable python module for checking if a GitHub repo has a new release.

__Current Version: 1.0__ ([changelog](#changelog))

## Install

Honestly, I have no clue other than I know it works from the same directory as the script you want to use it in. I think it might work if you put it in your path, but then your script isn't distributable.

Python seems unecessarily awkward about using code in other files, especially classes. I read some SO threads about `__init__.py` files in nested directories but that shit makes no sense.

PHP is literally infinity times better at this than python.

## Use

This bit is pretty easy, if I say so myself.

```python
import Updater

upd = Updater.New("1.2", "Ultrabenosaurus/EasyXdcc")
print upd.Simple()
print upd.Main()
```

`Updater.Simple()` and `Updater.Main()` aren't both supposed to be called, usually you'd just pick one or the other.

The former will return `True` if there's a newer version than you specified in `Updater.New()` and `False` if not, while the latter will give you strings to feed straight to your users.

## TODO

* actual customisation of `Main()`'s output
* option to automatically download and extract new version
* figure out module importing and properly package

## Changelog

### 1.0

* initial release
* can check if there's a new release on a GitHub repo
  * `True`/`False`
  * string output
* that's basically it for now
