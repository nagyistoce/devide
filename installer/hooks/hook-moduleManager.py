import os
import sys

if sys.platform.startswith('win'):
    sys.path.insert(0, 'c:/work/code/dscas3/')
else:
    sys.path.insert(0, '/home/cpbotha/work/code/dscas3/')

import modules

# * we need to give the module paths relative to the directory moduleManager
#   is in (I think, since this is the hook for moduleManager)
# * the installer will treat these imports as if they were explicitly
#   imported by the moduleManager, so THEIR dependecies will automatically
#   be analysed.
ml2 = ["modules." + i for i in modules.moduleList]
hiddenimports = ml2

print "[*] hook-moduleManager.py - HIDDENIMPORTS"
print hiddenimports
