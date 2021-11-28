import snap7


class S7Client:
    def __init__(self, ip, slot, rack):
        self.ip = ip
        self.slot = slot
        self.rack = rack

    def connect(self):
        con = snap7.client.Client()
        plc = con.connect(self.ip, self.rack, self.slot)
        connection_state = con.get_cpu_state()
        return connection_state

    def disconnect(self):
        con = snap7.client.Client()
        plc = con.disconnect()
        connection_state = con.get_cpu_state()
        return connection_state

    # @staticmethod
    def check_connection(self):   
        return self.connect()

    def read_from_plc(self, db_num, start_address, block_size):
        con = snap7.client.Client()
        con.connect(self.ip, self.rack, self.slot)
        db = con.db_read(db_num, start_address, block_size)
        return db

    def writo_to_plc(self, db_num, start_address, data):
        con = snap7.client.Client()
        con.connect(self.ip, self.rack, self.slot)
        con.db_write(db_num, start_address, data)



