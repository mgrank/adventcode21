with open("day16full.txt") as f:
  hex_string = f.readline().strip()

#hex_string = "A0016C880162017C3686B18A3D4780"
hex_number = int(hex_string, 16)
print(hex_string)
bin_list = list(f'{hex_number:0>{len(hex_string)*4}b}')
print(bin_list)

def bitSliceToDecimal(bit_slice):
  return int(''.join(bit_slice), 2)

def packetVerId(packet):
  return bitSliceToDecimal(packet[0:3]), bitSliceToDecimal(packet[3:6])

def parseValuePacket(packet):
  ver, id = packetVerId(packet)
  if id != 4:
    raise NameError("Not a value packet")
  i = 6
  num = []
  while True:
    num += packet[i+1: i+5]
    if packet[i] == '0':
      break
    i+=5
  print(f"Value packet, v={ver}, id={id}, num={bitSliceToDecimal(num)}")
  return (i+5, ver, bitSliceToDecimal(num))

def parseCommandPacket(packet):
  ver, id = packetVerId(packet)
  lengthID = packet[6]
  if lengthID == '0':
    lenInBits = bitSliceToDecimal( packet[7:22] )
    s_i = 22
    print(f"[start]Command packet 0, lenInBits={lenInBits}, v={ver}, id={id}")
    while s_i != 22 + lenInBits:
      subpackets = packet[s_i:]
      i, s_ver, s_val = parsePacket(subpackets)
      s_i += i
      ver += s_ver
    print(f"[end]Command packet 0, lenInBits={lenInBits}, v={ver}, id={id}")
    return (s_i, ver, id)

  if lengthID == '1':
    numSubPackets = bitSliceToDecimal( packet[7:18] )
    s_i = 18
    print(f"[start]Command packet 1, numSubPackets={numSubPackets}, v={ver}, id={id}")
    while numSubPackets > 0:
      subpacket = packet[s_i:]
      i, s_ver, s_val = parsePacket(subpacket)
      s_i += i
      ver += s_ver
      numSubPackets -= 1
    print(f"[end]Command packet 1, numSubPackets={numSubPackets}, v={ver}, id={id}")
    return (s_i, ver, id)

def parsePacket(packet):
  ver, id = packetVerId(packet)
  if id == 4:
    return parseValuePacket(packet)
  else:
    return parseCommandPacket(packet)

i, sumver, id = parsePacket(bin_list)
print(sumver)