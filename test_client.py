import pytest
import s7client
from s7client import S7Client


IP = '127.0.0.1'  # Insert server addres
RACK = 0
SLOT = 2

DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 260

DATA = b'Snap 7 test write blaaaaaaa'
DATA1 = b'dfskjhkjsdhf'
DATA2 = b'zsdfzsdfvgzsdvgfzsdvzsdvzsdvzsdvzsadvfzsdv'
DATA3 = b'#$%^$%^&#$%^#$_+)_('



# client = S7Client(IP, RACK, SLOT)
# client.connect()
# print(client.check_connection())
# print(client.read_from_plc(DB_NUMBER, START_ADDRESS, SIZE))
# print(client.writo_to_plc(DB_NUMBER, START_ADDRESS, DATA))
# print(client.check_connection())
# print(client.read_from_plc(DB_NUMBER, START_ADDRESS, SIZE))


@pytest.mark.parametrize("data", [DATA, DATA1, DATA2, DATA3])
def test_write_to_plc(data):
    client = S7Client(IP, RACK, SLOT)
    client.connect()
    client.writo_to_plc(DB_NUMBER, START_ADDRESS, DATA)
    length = len(DATA)
    plc_read_data = client.read_from_plc(DB_NUMBER, START_ADDRESS, SIZE)
    get_data = bytes(plc_read_data)
    print("\nget data Is: ", data)
    print("\nDATA Is: ", DATA)
    # print("READ DATA Is: ", get_data[:length])
    assert DATA == get_data[:length]
