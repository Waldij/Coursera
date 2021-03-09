import socket
import time


class ClientError(Exception):
    """ Client error class to throw """
    pass


class Client():
    """ Client class for assignment by coursera """

    def __init__(self, addr, port, timeout=None):
        self._addr = addr
        self._port = int(port)
        self._timeout = int(timeout)

    def get(self, key):
        """
            Gets metrics from the server by key, using command:
            get <key>\n
            :return returns metrics dict
        """
        get_command = 'get ' + key + '\n'
        response = self.send_command(get_command)
        self._check_response(response)
        return self._get_response_processing(response)

    def put(self, key, value, timestamp=None):
        """
            Puts metric on the server, command form:
            put <key> <value> <timestamp or time>\n
        """
        put_command = 'put ' + key + ' ' + str(value) + ' ' + str(timestamp if timestamp else int(time.time())) + '\n'
        self._check_response(self.send_command(put_command))

    def send_command(self, command):
        """
            Sends any command to server
            :return response
        """
        try:
            with socket.create_connection((self._addr, self._port), self._timeout) as sock:
                sock.sendall(command.encode("utf8"))
                response = sock.recv(1024)
                return response.decode('utf-8')
        except:
            raise ClientError

    def _check_response(self, response):
        """
            Checks response from server to be
            'ok\n'
            or
            :raise ClientError
        """
        if response[0:3] != 'ok\n':
            raise ClientError(response)

    def _get_response_processing(self, response):
        """
            Processes the server response to get command, that returns dict
            :arg response [(timestamp1, metric_value1), (timestamp2, metric_value2), …]
            :return metrics dict
                    {
                        'key': [
                            (int(timestamp), float(metric_value)),
                            (timestamp, metric_value)
                        ]
                    }
        """
        ret_dict = dict()
        try:
            lines = response.split('\n')
            for line in lines[1:-2]:
                metric = line.split(' ')
                key = metric[0]
                value = float(metric[1])
                timestamp = int(metric[2])
                if not key in ret_dict:
                    ret_dict[key] = list()
                ret_dict[key].append((timestamp, value))
                ret_dict[key].sort(key=lambda tup: tup[0])
        except:
            raise ClientError
        return ret_dict
