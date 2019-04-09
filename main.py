import nxppy
import ndef
import time

place_ID = A1

def code_finder(ndef_string,len_code):
    index = ndef_string.index('Text',17)
    code_start = index+6
    code_end = index+6+len_code
    code = ndef_string[code_start:code_end]
    return code

#def write_to_file(string):


'''
Appunti:
-tutti i record vanno inseriti in una lista (conviene creare un tipo di dato)
-ogni tot tempo questa lista viene svuotata dentro un file che viene inviato via ftp
'''
def main():
    # Instantiate reader
    mifare = nxppy.Mifare()
    # dict with presence signed in
    registro = {}
    while True:
        try:
            # Select tag
            uid = mifare.select()
            # Read NDEF data
            ndef_data = mifare.read_ndef()
            # Parse NDEF data
            ndef_records = list(ndef.message_decoder(ndef_data))
            print(ndef_records)
            stringa = str(ndef_records[0])
            code = code_finder(stringa,5)
            print(code)
            current_time = time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime())
            print(current_time)
            registro.update(code:current_time)
        except nxppy.SelectError:
            # SelectError is raised if no card is in the field.
            pass

        time.sleep(3)

if __name__ == '__main__':
    main()
