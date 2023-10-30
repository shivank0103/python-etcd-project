from cashifyetcd import CashifyETCD


def t1():
    etcd = CashifyETCD(
        host='etcd.prv.api.stage.cashify.in', protocol='http', port=80, service_name='supersales-python',
        service_version='v1'
    )
    return etcd.get_property_value('token_version')


def t2():
    etcd = CashifyETCD(
        host='etcd.prv.api.stage.cashify.in', protocol='http', port=80, service_name='supersales-python',
        service_version='v1'
    )
    return etcd.get_value('supersales-python', 'v1', 'server.base.url')


if __name__ == '__main__':
    print(t1())
