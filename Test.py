from BinaryStream import *
import math

def PrintVal(value):
	if type(value) == str or type(value) == float:
		print('value: ' + '\"{0}\"'.format(value) + ', type: ' + str(type(value)))
	else:
		print('value: ' + '{0}'.format(value) + ', hex: ' + '{0:016X}'.format(value) + ', type: ' + str(type(value)))

def test():
	test_file = "file.bin"

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
	
	for b in bytes_array:
		PrintVal(b)

	# test big/little endian
	w = BinaryWriter(open(test_file, "wb"), BinaryStream.Endianness.BIG)
	write_val = 0x12345678
	w.WriteUInt32(write_val)
	w.Flush()

	r = BinaryReader(open(test_file, "rb"), BinaryStream.Endianness.BIG)
	read_val = r.ReadUInt32()
	print('Big-endian: {0}'.format(read_val == write_val))
	PrintVal(write_val)
	PrintVal(read_val)

	r = BinaryReader(open(test_file, "rb"), BinaryStream.Endianness.LITTLE)
	read_val = r.ReadUInt32()
	print('Big-endian: {0}'.format(read_val == write_val))
	PrintVal(write_val)
	PrintVal(read_val)

test()