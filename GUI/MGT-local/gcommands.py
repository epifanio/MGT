import os
import sys
import subprocess
import json
import pandas as pd
import time
from gutil import getgenv


grassenv = getgenv('grassconf.json')
os.environ["GISBASE"] = grassenv['GISBASE']
sys.path.append(os.path.join(grassenv['GISBASE'], 'etc/python'))
os.environ["GISDBASE"] = grassenv['GISDBASE']
os.environ["MAPSET"] = grassenv['MAPSET']
os.environ["LOCATION_NAME"] = grassenv['LOCATION_NAME']
os.environ['GISRC'] = grassenv['GISRC']



from grass.script import task as gtask
import grass.script as grass

def get_command_list():
    # this function should return a filtered list of commands
    # that can run client size (e.g.: exclude all the d.* commands)
    command_list = grass.read_command('g.search.modules', keyword='', flags='g').decode().strip().split('\n')
    return command_list

def get_model():
    """list of list to be converted to three model"""
    model={}
    model['mapsets'] = [i.decode() for i in grass.mapsets(search_path=True)]
    model['raster'] = grass.core.list_pairs('raster')
    model['vector'] = grass.core.list_pairs('vector')
    model['raster_3d'] = grass.core.list_pairs('raster_3d')
    model['region'] = grass.core.list_pairs('region')
    model['group'] = grass.core.list_pairs('group')
    return model

def get_command_description(command):
    pd.options.mode.chained_assignment = None
    b = command.encode('utf-8')
    commandspecs = gtask.command_info(b)
    flags = []
    for i, v in enumerate(commandspecs['flags']):
        flags.append(pd.DataFrame.from_dict({0: v}, orient='index'))
    flags = pd.concat(flags).reset_index()
    flags.drop('index', 1, inplace=True)
    flags['guisection'].loc[(flags['guisection'] == '')] = 'Optional'

    params = []
    for i, v in enumerate(commandspecs['params']):
        params.append(pd.DataFrame.from_dict({0: v}, orient='index'))
    params = pd.concat(params).reset_index()
    params.drop('index', 1, inplace=True)

    params['guisection'].loc[
        (params['guisection'] == '') & (params['required'] == False)
    ] = 'Optional'
    params['guisection'].loc[
        (params['guisection'] == '') | (params['required'] == True)
    ] = 'Required'

    guisection = list(params['guisection'].unique()) + \
        list(flags['guisection'].unique())
    guisection = set(guisection)
    command_description = {}
    pr = {}
    fl = {}
    for i in guisection:
        pr[i] = params.loc[(params['guisection'] == i)].reset_index()
        fl[i] = flags.loc[(flags['guisection'] == i)].reset_index()
        del pr[i]['index']
        del fl[i]['index']
    command_description['description'] = commandspecs['description']
    command_description['keywords'] = commandspecs['keywords']
    command_description['usage'] = commandspecs['usage']
    command_description['parameters'] = pr
    command_description['flags'] = fl
    command_description['model'] = get_model()
    return command_description
