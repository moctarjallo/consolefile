from .domain import *

class IO:
    def __init__(self, endpoint: str='console'):
        if endpoint == 'console':
            self.endpoint = Console()
        elif endpoint.endswith('.txt'):
            self.endpoint = File(endpoint)