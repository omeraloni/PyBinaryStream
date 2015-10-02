import struct
import os
from enum import Enum

class BinaryStream(object):
	def __init__(self, stream):
		pass

	class Endianness(Enum):
		BIG = 0
		LITTLE = 1
		NATIVE = 2

	def GetEndiannes(self, endianness):
		return {
			BinaryStream.Endianness.BIG: '>',
			BinaryStream.Endianness.LITTLE: '<',
			BinaryStream.Endianness.NATIVE: '=',
		}.get(endianness, BinaryStream.Endianness.NATIVE)

	def Close(self):
		self.stream.close()

	def Flush(self):
		self.stream.flush()

	def BaseStream(self):
		return self.stream

	def Seek(self, offset, origin = os.SEEK_SET):
		self.stream.seek(offset, origin)

class BinaryReader(BinaryStream):
	def __init__(self, stream, endianness=BinaryStream.Endianness.NATIVE):
		super(BinaryReader, self).__init__(stream)
		self.stream = stream
		self.endianness = BinaryStream.GetEndiannes(self, endianness)

	def ReadByte(self):
		return struct.unpack(self.endianness + 'B', self.stream.read(1))[0]

	def ReadBool(self):
		return struct.unpack(self.endianness + '?', self.stream.read(1))[0]

	def ReadBytes(self, val):
		return self.stream.read(val)

	def ReadChar(self):
		return self.stream.read(1).decode('ascii')

	def ReadChars(self, num):
		return self.stream.read(num).decode('ascii')

	def ReadDouble(self):
		return struct.unpack(self.endianness + 'd', self.stream.read(8))[0]

	def ReadInt16(self):
		return struct.unpack(self.endianness + 'h', self.stream.read(2))[0]

	def ReadInt32(self):
		return struct.unpack(self.endianness + 'i', self.stream.read(4))[0]

	def ReadInt64(self):
		return struct.unpack(self.endianness + 'q', self.stream.read(8))[0]

	def ReadSByte(self):
		return struct.unpack(self.endianness + 'b', self.stream.read(1))[0]

	def ReadSingle(self):
		return struct.unpack(self.endianness + 'f', self.stream.read(4))[0]

	def ReadString(self):
		pass

	def ReadUInt16(self):
		return struct.unpack(self.endianness + 'H', self.stream.read(2))[0]

	def ReadUInt32(self):
		return struct.unpack(self.endianness + 'I', self.stream.read(4))[0]

	def ReadUInt64(self):
		return struct.unpack(self.endianness + 'Q', self.stream.read(8))[0]
	
	def Read7BitEncodedInt(self):
		pass

class BinaryWriter(BinaryStream):
	def __init__(self, stream, endianness=BinaryStream.Endianness.NATIVE):
		super(BinaryWriter, self).__init__(stream)
		self.stream =  stream
		self.endianness = BinaryStream.GetEndiannes(self, endianness)

	def WriteBool(self, value):
		self.stream.write(struct.pack(self.endianness + '?', value))

	def WriteByte(self, value):
		self.stream.write(struct.pack(self.endianness + 'B', value))

	def WriteBytes(self, value):
		self.stream.write(value)

	def WriteChar(self, value):
		self.stream.write(struct.pack(self.endianness + 'c', value.encode('ascii')))

	def WriteChars(self, value):
		self.stream.write(value.encode('ascii'))

	def WriteDouble(self, value):
		self.stream.write(struct.pack(self.endianness + 'd', value))

	def WriteInt16(self, value):
		self.stream.write(struct.pack(self.endianness + 'h', value))

	def WriteInt32(self, value):
		self.stream.write(struct.pack(self.endianness + 'i', value))

	def WriteInt64(self, value):
		self.stream.write(struct.pack(self.endianness + 'q', value))

	def WriteSByte(self, value):
		self.stream.write(struct.pack(self.endianness + 'b', value))

	def WriteSingle(self, value):
		self.stream.write(struct.pack(self.endianness + 'f', value))

	def WriteString(self, value):
		pass

	def WriteUInt16(self, value):
		self.stream.write(struct.pack(self.endianness + 'H', value))

	def WriteUInt32(self, value):
		self.stream.write(struct.pack(self.endianness + 'I', value))

	def WriteUInt64(self, value):
		self.stream.write(struct.pack(self.endianness + 'Q', value))

	def Write7BitEncodedInt(self, value):
		pass