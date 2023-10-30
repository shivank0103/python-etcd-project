# cashify-python-etcd

How to use:
 Use steps under to use directly from source code
- Install library using pip install git+https://git@github.com/reglobe/cashify-python-etcd.git
- Install library using pip install git+ssh://git@github.com/reglobe/cashify-python-etcd.git
- Create a different file for ETCD configuration
- Import -> from cashifyetcd import CashifyETCD
- Initialize cashify_etcd = CashifyETCD('host', 'protocol', port, 'service_name', 'service_version')
- Simply use cashify_etcd.get_property_value('etcd.key') to get value else this will throw exception "Key not found"
- 300 seconds cache is already applied on ETCD
- add this line to requirements file to install "-e git+ssh://git@github.com/reglobe/cashify-python-etcd.git#egg=cashifypythonetcd" automatically
