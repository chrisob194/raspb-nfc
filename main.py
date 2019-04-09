import nxppy
import ndef

#def string_parser(string):


# Instantiate reader
mifare = nxppy.Mifare()

# Select tag
uid = mifare.select()

# Read NDEF data
ndef_data = mifare.read_ndef()

# Parse NDEF data
ndef_records = list(ndef.message_decoder(ndef_data))
print(ndef_records)
print(type(ndef_records))
stringa = str(ndef_records[0])
print(stringa)
