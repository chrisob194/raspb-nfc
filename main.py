import nxppy
import ndef

def code_finder(ndef_string,len_code):
    index = ndef_string.index('Text')
    code_start = index+5
    code_end = index+5+len_code
    code = ndef_string[start:end]
    return code


# Instantiate reader
mifare = nxppy.Mifare()

# Select tag
uid = mifare.select()

# Read NDEF data
ndef_data = mifare.read_ndef()

# Parse NDEF data
ndef_records = list(ndef.message_decoder(ndef_data))
print(ndef_records)
#print(type(ndef_records))
stringa = str(ndef_records[0])
code = code_finder(stringa,5)
print(code)
