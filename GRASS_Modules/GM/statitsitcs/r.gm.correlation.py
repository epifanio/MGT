#!/usr/bin/env python
#
############################################################################
#
# MODULE:
# AUTHOR(S):   Massimo Di Stefano
#
#
# PURPOSE:
# COPYRIGHT:   (C) 2018 by the GRASS Development Team
#
#              This program is free software under the GNU General Public
#              License (>=v2). Read the file COPYING that comes with GRASS
#              for details.
#
#############################################################################

#%Module
#% description:
#% keyword:
#% keyword:
#%End
#%option
#% key:
#% type: string
#% gisprompt: old,cell,raster
#% description:
#% required : yes
#%end
#%option
#% key:
#% type: string
#% gisprompt: old,cell,raster
#% description:
#% required : yes
#%end
#%option
#% key:
#% type: integer
#% description:
#% options:
#% answer:
#%end

import sys
from grass.script import core as grass

def main():
    key = options[key]
    ret = grass.run_command()
    sys.exit(ret)

if __name__ == "__main__":
    options, flags = grass.parser()
    main()