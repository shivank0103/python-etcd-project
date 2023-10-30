import etcd
from caching import CashifyCache


DEFAULT_TIMEOUT = 300
GLOBAL_SERVICE_NAME = 'global'


class SingleTonCache(object):
    _instance = None
    cache = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls, app_name: str, cache_type: str):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
            cls.cache = CashifyCache(app_name=app_name, cache_type=cache_type)
        return cls._instance


class CashifyETCD(object):
    """ Base class for initializing """

    host = None
    protocol = None
    port = None
    etcd_client = None
    service_name = None
    service_version = None
    proxy = None
    headers = None

    def __init__(self, host: str, protocol: str, port: int, service_name: str, service_version: str):

        """ Get ETCD client """

        self.host = host
        self.protocol = host
        self.port = host
        self.etcd_client = etcd.Client(host=host, protocol=protocol, port=port)
        self.service_name = service_name
        self.service_version = service_version

    def get_config(self):
        return {
            'host': self.host,
            'protocol': self.host,
            'port': self.host,
            'service_name': self.service_name,
            'service_version': self.service_version
        }

    def get_property_value(self, key: str):
        """ Get property value from ETCD if not found return default """
        cache = SingleTonCache.instance(self.service_name, 'LOCAL').cache
        cache_key = 'etcd.' + key
        value = cache.cache(cache_key, DEFAULT_TIMEOUT, [])(self.get_value)(self.service_name, self.service_version, key)
        return value

    def get_value(self, service_name: str, service_version: str, key: str):
        try:
            return self.etcd_client.read(
                service_name + '/' + service_name + '.' + service_version + '.' + key
            ).value
        except etcd.EtcdKeyNotFound:
            pass

        try:
            return self.etcd_client.read(
                service_name + '/' + service_name + '.' + key
            ).value
        except etcd.EtcdKeyNotFound:
            pass

        try:
            return self.etcd_client.read(
                GLOBAL_SERVICE_NAME + '/' + GLOBAL_SERVICE_NAME + '.' + service_version + '.' + key
            ).value
        except etcd.EtcdKeyNotFound:
            pass

        try:
            return self.etcd_client.read(
                GLOBAL_SERVICE_NAME + '/' + GLOBAL_SERVICE_NAME + '.' + key
            ).value
        except etcd.EtcdKeyNotFound:
            print('KEY', key)
            raise Exception("Key not found")
