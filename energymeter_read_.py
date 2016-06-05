from pymodbus.client.sync import ModbusSerialClient as pyRtu
import minimalmodbus as mmRtu

BAUD_RATE = 4800
TIME_OUT = 0.1
REGISTER_COUNT = 90
MODE = 'rtu'
PARITY = 'N'
STOP_BITS = 1
SLAVE_ID = 1
REGISTER_START_ADDRESS = 0


class Modbus_Read(object):
	"""docstring for Modbus_Read"""
	def __init__(self):
		self.__modbus_init()

	def find_port(self):
		for vtr in range(0,12):
			port_id ='/dev/ttyUSB' + str(vtr)
			try:
				mmc_init=mmRtu.Instrument(port = port_id ,slaveaddress=1,mode = 'rtu')   # port name, slave address\
				print ("++ found serial on " + port_id)
				break
			except:
				pass
		return port_id

	def __modbus_init(self):
		port = self.find_port()
		self.pymc = pyRtu(method=MODE, port=port,parity = PARITY,stopbits =STOP_BITS,
		baudrate=BAUD_RATE, timeout=TIME_OUT)
		
	def read_register(self):
		try:
			response = self.pymc.read_input_registers(REGISTER_START_ADDRESS,count=REGISTER_COUNT,unit=SLAVE_ID)
			return response.registers
		except:
			print "No response from register"
			return []

if __name__ == '__main__':
	"""create object of the class and call register_read function"""
	modbus_read = Modbus_Read()
	print modbus_read.register_read()

