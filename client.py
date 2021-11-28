import snap7

IP = '127.0.0.1'  # Insert server addres
RACK = 0
SLOT = 2

DB_NUMBER = 1
START_ADDRESS = 0
SIZE = 260

DATA = b'Snap7 App to PLC!'


plc = snap7.client.Client()
plc.connect(IP, RACK, SLOT)

plc_info = plc.get_cp_info()
# print(plc_info.ModuleTypeName)c
print(f'Module type: {plc_info}')
state = plc.get_cpu_state()
print(f'State: {state}')

db = plc.db_read(DB_NUMBER, START_ADDRESS, SIZE)
# print(db)

plc.db_write(DB_NUMBER, START_ADDRESS, DATA)

product_name = db[0:255].decode('UTF-8').strip('\x00')  # for real PLC, don't work with demo server
print(f'Product name: {product_name}')

product_value = int.from_bytes(db[255:257], byteorder='big')
print(f'Product value: {product_value}')

product_status = bool(db[258])
print(f'Product status: {product_status}')

plc.disconnect()