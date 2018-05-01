import os
import json
import tempfile

def getgenv(gconf):
    try:
        with open(gconf) as grass_config:
            grassenv = True
            writegisrc = None
            data = json.load(grass_config)
            for i in ['GISBASE', 'MAPSET', 'LOCATION_NAME', 'GISDBASE']:
                if i not in list(data.keys()):
                    print('incomplete configuration file, missing %s ' % i)
                    grassenv = None
            if grassenv is not None:
                GISBASE = data['GISBASE']
                GISDBASE = data['GISDBASE']
                MAPSET = data['MAPSET']
                LOCATION_NAME = data['LOCATION_NAME']

                gisrc = 'MAPSET: %s\n' % MAPSET
                gisrc += 'GISDBASE: %s\n' % GISDBASE
                gisrc += 'LOCATION_NAME: %s\n' % LOCATION_NAME
                gisrc += 'GUI: text'

                temp_dir = tempfile.mkdtemp(prefix='.grassrc_')
                temp_name = next(tempfile._get_candidate_names())
                GISRC = os.path.join(temp_dir, temp_name)
                grass_gisrc = open(GISRC, 'w')
                grass_gisrc.write(gisrc)
                grass_gisrc.close()

                if 'GISRC' not in list(data.keys()) or not os.path.isfile(GISRC):
                    with open(gconf) as grass_config:
                        json_decoded = json.load(grass_config)
                    json_decoded['GISRC'] =  GISRC
                    with open(gconf, 'w') as grass_config:
                        json.dump(json_decoded, grass_config)


    except IOError as err:
        errno, strerror = err.args
        print('grassconfig.json not found in current directory %s' % os.path.basename(os.path.dirname(os.path.realpath(__file__))))
    return {'GISBASE': GISBASE, 'GISDBASE': GISDBASE, 'MAPSET': MAPSET, 'LOCATION_NAME': LOCATION_NAME, 'GISRC': GISRC}