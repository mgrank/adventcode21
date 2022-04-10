from math import prod

with open("day16full.txt") as f:
  hex_string = f.readline().strip()

hex_string = "C200B40A82"
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
  return (i+5, bitSliceToDecimal(num))

def executeCommand(id, s_res):
  match id:
    case 0:
      return sum(s_res)
    case 1:
      return prod(s_res)
    case 2:
      return min(s_res)
    case 3:
      return max(s_res)
    case 5:
      return 1 if s_res[0] > s_res[1] else 0
    case 6:
      return 1 if s_res[0] < s_res[1] else 0
    case 7:
      return 1 if s_res[0] == s_res[1] else 0

def parseCommandPacket(packet):
  ver, id = packetVerId(packet)
  lengthID = packet[6]
  s_res = []
  if lengthID == '0':
    lenInBits = bitSliceToDecimal( packet[7:22] )
    s_i = 22
    print(f"[start]Command packet 0, lenInBits={lenInBits}, v={ver}, id={id}")
    while s_i != 22 + lenInBits:
      subpackets = packet[s_i:]
      i, s_val = parsePacket(subpackets)
      s_i += i
      s_res.append(s_val)
    print(f"[end]Command packet 0, lenInBits={lenInBits}, v={ver}, id={id}")
    res = executeCommand(id, s_res)
    return (s_i, res)

  if lengthID == '1':
    numSubPackets = bitSliceToDecimal( packet[7:18] )
    s_i = 18
    print(f"[start]Command packet 1, numSubPackets={numSubPackets}, v={ver}, id={id}")
    while numSubPackets > 0:
      subpacket = packet[s_i:]
      i, s_val = parsePacket(subpacket)
      s_i += i
      numSubPackets -= 1
      s_res.append(s_val)
    print(f"[end]Command packet 1, numSubPackets={numSubPackets}, v={ver}, id={id}")
    res = executeCommand(id, s_res)
    return (s_i, res)

def parsePacket(packet):
  ver, id = packetVerId(packet)
  if id == 4:
    return parseValuePacket(packet)
  else:
    return parseCommandPacket(packet)

i, res = parsePacket(bin_list)
print(res)