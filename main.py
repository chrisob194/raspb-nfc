import nxppy
import ndef

# Instantiate reader
mifare = nxppy.Mifare()

# Select tag
uid = mifare.select()

# Read NDEF data
ndef_data = mifare.read_ndef()

# Parse NDEF data
ndef_records = list(ndef.message_decoder(ndef_data))
