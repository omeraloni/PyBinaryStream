from BinaryStream import *
import math
import sys

def PrintInt(value):
	print('value: ' + '{0}'.format(value) + ', hex: ' + '{0:016x}'.format(value) + ', type: ' + str(type(value)))

def PrintOther(value):
	print('value: ' + '\"{0}\"'.format(value) + ', type: ' + str(type(value)))

def PrintStr(value):
	print('value: ' + '\"{0}\"'.format(value) + ', hex: ' + ":".join("{:02x}".format(ord(c)) for c in value) + ', type: ' + str(type(value)))

def PrintVal(value):

	print_method = {
		int : PrintInt,
		float : PrintOther,
		unicode : PrintStr,
		str : PrintStr,
		bool : PrintInt,
		long : PrintInt,
	}

	print_method[type(value)](value)

def float_to_hex(value):
    return hex(struct.unpack('<I', struct.pack('<f', value))[0])

def double_to_hex(value):
    return hex(struct.unpack('<Q', struct.pack('<d', value))[0])

def int32_to_hex(value):
    return hex(struct.unpack('<I', struct.pack('<i', value))[0])

def uint32_to_hex(value):
    return hex(struct.unpack('<I', struct.pack('<I', value))[0])

def str_to_hex(value):
    return ":".join("{:02x}".format(ord(c)) for c in value)

def test():

	print(sys.version_info)

	test_file = "file.bin"

	"""
	w = BinaryWriter(open(test_file, "wb"))
	r = BinaryReader(open(test_file, "rb"))

	# test byte array	w.Seek(0, os.SEEK_SET)
	w.WriteBytes(bytearray([0x12, 0x34, 0x56, 0x78]))
	w.Flush()

	bytes_array = r.ReadBytes(4)

	for b in bytes_array:
		#print(type(b))
		#print(b)
		PrintStr(b)

	#PrintStr('hello')

	#print(float_to_hex(1.0))
	#print(double_to_hex(2.0))
	#print(int32_to_hex(-2147483648))
	#print(uint32_to_hex(2*2147483648 - 1))
	#print(str_to_hex('hello'))

	"""
	# create a binary writer instance on top of a file stream
	w = BinaryWriter(open(test_file, "wb"), BinaryStream.Endianness.LITTLE)

	# test primitive types
	w.WriteUInt64(45345324524524234)
	w.WriteInt32(5678)
	w.WriteInt16(134)
	w.WriteByte(129)
	w.WriteBool(True)
	w.WriteChar('a')
	w.WriteChars('testing')
	w.WriteSingle(2 * math.asin(1))
	w.WriteDouble((1 + math.sqrt(5)) / 2.0)
	w.Flush()

	r = BinaryReader(open(test_file, "rb"))

	PrintVal(r.ReadUInt64())
	PrintVal(r.ReadInt32())
	PrintVal(r.ReadInt16())
	PrintVal(r.ReadByte())
	PrintVal(r.ReadBool())
	PrintVal(r.ReadChar())
	PrintVal(r.ReadChars(7))
	PrintVal(r.ReadSingle())
	PrintVal(r.ReadDouble())

	# test byte array
	w.Seek(0, os.SEEK_SET)
	w.WriteBytes(bytearray([0x12, 0x34, 0x56, 0x78]))
	w.Flush()

	r.Seek(0, os.SEEK_SET)
	bytes_array = r.ReadBytes(4)
	"""
	for b in bytes_array:
		PrintStr(b)
	"""

	# test big/little endian
	w = BinaryWriter(open(test_file, "wb"), BinaryStream.Endianness.BIG)
	write_val = 0x1234567890ABCDEF
	w.WriteUInt64(write_val)
	w.Flush()

	r = BinaryReader(open(test_file, "rb"), BinaryStream.Endianness.BIG)
	read_val = r.ReadUInt64()
	print('Big-endian: {0}'.format(read_val == write_val))
	PrintVal(write_val)
	PrintVal(read_val)

	r = BinaryReader(open(test_file, "rb"), BinaryStream.Endianness.LITTLE)
	read_val = r.ReadUInt64()
	print('Big-endian: {0}'.format(read_val == write_val))
	PrintVal(write_val)
	PrintVal(read_val)

	######################

	print(r)

test()
