import nxppy

#initilize and select tag
mifare = nxppy.Mifare()
uid = mifare.select()


#Enable protection
####################

#write password 1234
mifare.write_block(0xE5, '1234')

#password protection starting at address D1
mifare.write_block(0xE3, b'\x04\x00\x00\xD1')

#enable readprotection (default is write protection only)
mifare.write_block(0xE4, b'\x80\x05\x00\x00')


#authenticate
####################
mifare.pwd_auth('1234')
#read and write from/to protected address space


#disable protection
####################

#reset password
#mifare.write_block(0xE5, b'\xFF\xFF\xFF\xFF')

#set protection addr beyond address space
#mifare.write_block(0xE3, b'\x04\x00\x00\xE7')

#reset readprotection
#mifare.write_block(0xE4, b'\x00\x05\x00\x00')
