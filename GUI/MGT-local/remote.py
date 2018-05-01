import zmq
import json

def get_conf(sconf):
    server_env = True
    try:
        with open(sconf) as server_config:
            data = json.load(server_config)
    except IOError:
        print('no server configuration found')
    print(list(data.keys()))
    for i in ['IP', 'PORT']:
        if i not in list(data.keys()):
            print('incomplete configuration file, missing %s ' % i)
            server_env = None
    if server_env is not None:
        ip = data['IP']
        port = data['PORT']
        server_env={'IP': ip, 'PORT': port}
    return server_env


def get_message(command_name, ip, port, send_socket_type='pyobj', socket=None):
    #context = zmq.Context()
    #socket = context.socket(zmq.REQ)
    socket.connect("tcp://%s:%s" % (ip, port))
    socket.send_string(command_name)
    if send_socket_type=='pyobj':
        msg = socket.recv_pyobj()
    if send_socket_type=='string':
        msg = socket.recv_string()
    if send_socket_type=='json':
        msg = socket.recv_json()
    socket.close()
    return msg
