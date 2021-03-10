import asyncio

storage = dict()


class ClientServerProtocolError(Exception):
    """ Server error class to raise """
    pass


class ClientError(Exception):
    """ Client error class to raise """
    pass


class ClientServerProtocol(asyncio.Protocol):
    """ Class, that describes server logic"""
    def __init__(self):
        self.transport = None

    def connection_made(self, transport: asyncio.Transport):
        self.transport = transport

    def data_received(self, data: bytes):
        self.transport.write(self._process_command(data.decode('utf-8').strip('\r\n')).encode('utf-8'))

    def _process_command(self, command):
        """
            Procrsses commands from clients

            put <key> <value> <timestamp>

            get <key>
        """
        command_chunks = command.split(' ')
        print(command_chunks)

        if command_chunks[0] == 'put' and len(command_chunks) <= 4:
            try:
                return self._process_put(key=command_chunks[1],
                                         value=float(command_chunks[2]),
                                         timestamp=int(command_chunks[3]))
            except:
                return 'error\nwrong command\n\n'
        elif command_chunks[0] == 'get' and len(command_chunks) == 2:
            return self._process_get(key=command_chunks[1])
        else:
            return 'error\nwrong command\n\n'

    def _process_put(self, key, value: float, timestamp: int):
        """ Puts metric on server's storage """
        response = 'ok\n\n'
        if key == '*':
            return 'error\nkey cannot contain *\n\n'
        if not key in storage:
            storage[key] = list()
        for pair in storage[key]:
            if timestamp in pair:
                storage[key].remove(pair)
        storage[key].append((timestamp, value))
        storage[key].sort(key=lambda tup: tup[0])
        return response

    def _process_get(self, key):
        """ Returns metrics from server storage by key  """
        response = 'ok\n'
        if key == '*':
            for key, values in storage.items():
                for value in values:
                    response = response + key + ' ' + str(value[1]) + ' ' + str(value[0]) + '\n'
        else:
            if key in storage:
                for value in storage[key]:
                    response = response + key + ' ' + str(value[1]) + ' ' + str(value[0]) + '\n'
        return response + '\n'


def run_server(host='127.0.0.1', port=8888):
    """ Runs server, default: 127.0.0.1:8888    """
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server()
