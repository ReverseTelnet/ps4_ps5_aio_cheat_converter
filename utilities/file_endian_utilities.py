# ------------------------------------------------------------------------------------------------------------------------------------
#
#
#   This Utility contains functions used to determine file encoding and endianness.
#
#
#   https://www.unicode.org/faq/utf_bom
#   https://stackoverflow.com/a/38038099
#
#
# ------------------------------------------------------------------------------------------------------------------------------------



##############################################################################
#                                                                            #
#                      Enable Absolute Imports Function                      #
#                                                                            #
##############################################################################



#######################  Absolute Imports > Relative Imports  #######################



def enable_absolute_imports():
    import sys
    from os import getcwd
    PWD = getcwd()
    if PWD not in sys.path:
        sys.path.append(PWD)



enable_absolute_imports()



##############################################################################
#                                                                            #
#                         BOM to Encoding Dictionary                         #
#                                                                            #
##############################################################################



#######################  Reference: Byte Order Mark: Encoding Method  #######################



bom_to_encoding = {
    '0000FEFF': 'UTF-32 BE',
    'FFFE0000': 'UTF-32 LE',
    'FEFF': 'UTF-16 BE',
    'FFFE': 'UTF-16 LE',
    'EFBBBF': 'UTF-8'
}



##############################################################################
#                                                                            #
#                       Convert Bytes to Hex Function                        #
#                                                                            #
##############################################################################



def convert_bytes_to_hex(byte_value):
    hex_value = byte_value.hex().upper()
    return hex_value



##############################################################################
#                                                                            #
#                        Get Endianness Type Function                        #
#                                                                            #
##############################################################################



#######################  BOM --> In | Endianness --> Out  #######################



def get_file_endianness_type(hex_value):
    if hex_value.startswith('FFFE0000'):
        endianness = 'utf32_le'
    elif hex_value.startswith('0000FEFF'):
        endianness = 'utf32_be'
    elif hex_value.startswith('FFFE'):
        endianness = 'utf16_le'
    elif hex_value.startswith('FEFF'):
        endianness = 'utf16_be'
    return endianness



##############################################################################
#                                                                            #
#                      Determine File Encoding Function                      #
#                                                                            #
##############################################################################



import chardet



#######################  File --> In | Encoding, Endianness --> Out  #######################



def determine_file_encoding(filename):
    with open(filename, 'rb') as file:
        thirty_bytes_raw = file.read(32)
        encoding = chardet.detect(thirty_bytes_raw)['encoding'].lower()
        if encoding == 'utf-16' or encoding == 'utf-32':
            hex_value = convert_bytes_to_hex(thirty_bytes_raw)
            endianness = get_file_endianness_type(hex_value)
        else:
            endianness = None
        return thirty_bytes_raw, encoding, endianness


