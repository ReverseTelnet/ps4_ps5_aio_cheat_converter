# ------------------------------------------------------------------------------------------------------------------------------------
#
#
#   This Utility contains functions used to convert numbers between different formats (notations).
#
#
#   The human eye is keen to decimal numbers.
#   The machine ultimately uses binary.
#   Hex values are easier to consume than binary and commonly used in Cheat Files.
#
#
#   Bytes (technically Hex) is another notation.
#   Within Bytes, values can be displayed in Little Endian or Big Endian Order.
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



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                      Functions That Convert From Decimal Values                                                     #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                      Convert Decimal to Hex Function                       #
#                                                                            #
##############################################################################



#######################  Decimal --> In | Hex --> Out  #######################



def convert_decimal_to_hex(decimal_string):
    hex_value = hex(int(decimal_string))
    return hex_value



##############################################################################
#                                                                            #
#                     Convert Decimal to Binary Function                     #
#                                                                            #
##############################################################################



#######################  Decimal --> In | Binary --> Out  #######################



def convert_decimal_to_binary(decimal_string):
    binary_value = f'{int(decimal_string):08b}'
    return binary_value



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                        Functions That Convert From Hex Values                                                       #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                      Convert Hex to Decimal Function                       #
#                                                                            #
##############################################################################



#######################  Hex --> In | Decimal --> Out  #######################



def convert_hex_to_decimal(hex_string):
    decimal_value = int(hex_string, 16)
    return decimal_value



##############################################################################
#                                                                            #
#                       Convert Hex to Binary Function                       #
#                                                                            #
##############################################################################



#######################  Hex --> In | Binary --> Out  #######################



def convert_hex_to_binary(hex_string):
    binary_value = f'{int(str(hex_string), 16):08b}'
    return binary_value



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                      Functions That Convert From Binary Values                                                      #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                     Convert Binary to Decimal Function                     #
#                                                                            #
##############################################################################



#######################  Binary --> In | Decimal --> Out  #######################



def convert_binary_to_decimal(binary_string):
    decimal_value = int(binary_string, 2)
    return decimal_value



##############################################################################
#                                                                            #
#                       Convert Binary to Hex Function                       #
#                                                                            #
##############################################################################



#######################  Binary --> In | Hex --> Out  #######################



def convert_binary_to_hex(binary_string):
    hex_value = hex(int(str(binary_string, 2)))
    return hex_value



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                       Functions That Convert From Byte Values                                                       #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#              Convert Little Endian Bytes to Decimal Function               #
#                                                                            #
##############################################################################



#######################  Little Endian Bytes --> In | Decimal --> Out  #######################



def convert_le_bytes_to_decimal(le_byte_value):
    decimal_value = int.from_bytes(le_byte_value, byteorder='little')
    return decimal_value



##############################################################################
#                                                                            #
#                Convert Big Endian Bytes to Decimal Function                #
#                                                                            #
##############################################################################



#######################  Big Endian Bytes --> In | Decimal --> Out  #######################



def convert_be_bytes_to_decimal(be_byte_value):
    decimal_value = int.from_bytes(be_byte_value, byteorder='big')
    return decimal_value



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                 Functions The Convert From Decimal to Bytes and Hex                                                 #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                        Zero Pad Hex Values Function                        #
#                                                                            #
##############################################################################



'''
When viewing memory or a file through a Hex Tool, each Hex Value is represented
using at least two digits:

    Example:
        0x09

While `0x09` and `0x9` are technically equivalent, they are not the same string.

This function ensures that a Hex Value always has an even number of characters.
'''



# https://stackoverflow.com/questions/16414559/how-to-use-hex-without-0x-in-python
# https://stackoverflow.com/questions/12638408/decorating-hex-function-to-pad-zeros
# https://stackoverflow.com/questions/4368676/is-there-a-way-to-pad-to-an-even-number-of-digits



#######################  Hex String (no `0x`) --> In | Padded Hex (String) --> Out  #######################



def pad_hex_values(hex_string):
  padded_hex = hex_string if len(hex_string) % 2 == 0 else '0' + hex_string
  return padded_hex



##############################################################################
#                                                                            #
#                        Strip Leading Zeros Function                        #
#                                                                            #
##############################################################################



'''
Different methods in Python display Hex values differently.
They may or may not include leading zeros.
They may or may not have an even number of characters.


This function removes leading Zeros if the number of characters is not 4 or 8.
It is mainly used for working with Big Endian Hex Values.


Example:
    Decimal:   74565
    Hex Value: 0x12345 --> hex(int(decimal_string))

    Big Endian Byte Value: b'\x00\x01#E'
    Hex Value: 00012345 --> byte_value.hex()
'''



#######################  `00012345` --> In | `12345` --> Out  #######################



def strip_leading_zeros(hex_string):
    if len(hex_string) == 8 or len(hex_string) == 4:
        hex_string = hex_string.upper()
    else:
        hex_string = hex_string.lstrip('0').upper()
    return hex_string



##############################################################################
#                                                                            #
#                       Strip Trailing Zeros Function                        #
#                                                                            #
##############################################################################



'''
Different methods in Python display Hex values differently.
They may or may not include leading zeros.
They may or may not have an even number of characters.


This function removes leading Zeros if the number of characters is not 4 or 8.
It is mainly used for working with Little Endian Hex Values.


Example:
    Decimal:   74565
    Hex Value: 0x12345 --> hex(int(decimal_string))

    Little Endian Byte Value: b'E#\x01\x00'
    Hex Value: 45230100 --> byte_value.hex()
'''



#######################  `45230100` --> In | `452301` --> Out  #######################



def strip_trailing_zeros(hex_string):
    if len(hex_string) == 8 or len(hex_string) == 4:
        hex_string = hex_string.upper()
    else:
        hex_string = hex_string.rstrip('0').upper()
    return hex_string



##############################################################################
#                                                                            #
#            Convert Decimal to Bytes and Big Endian Hex Function            #
#                                                                            #
##############################################################################



'''
This function takes a decimal value as the input and returns the value in:
    • Bytes
    • Big Endian Hex
    • Space Separated Hex (Big Endian)


The input value can be an integer or a string.
As a string, the value can use commas or periods (full-stops) to separate the digits.


Example:
    Integer: 2147483647
    String: '2147483647'
    Comma Separated: '2,147,483,647'
    Period (Full-Stop) Separated: '2.147.483.647'
'''



import struct



#######################  Decimal --> In | Big Endian Hex --> Out  #######################



def convert_decimal_to_bytes_and_be_hex(input_value):
    input_value = str(input_value).replace(',', '').replace('.', '')
    byte_value = struct.pack('>I', int(input_value))
    hex_string = strip_leading_zeros(byte_value.hex())
    hex_value = f'0x{pad_hex_values(hex_string)}'
    hex_separated = byte_value.hex(' ', 1).upper()
    return byte_value, hex_value, hex_separated



##############################################################################
#                                                                            #
#          Convert Decimal to Bytes and Little Endian Hex Function           #
#                                                                            #
##############################################################################



'''
This function takes a decimal value as the input and returns the value in:
    • Bytes
    • Little Endian Hex
    • Space Separated Hex (Little Endian)


The input value can be an integer or a string.
As a string, the value can use commas or periods (full-stops) to separate the digits.


Example:
    Integer: 2147483647
    String: '2147483647'
    Comma Separated: '2,147,483,647'
    Period (Full-Stop) Separated: '2.147.483.647'
'''



#######################  Decimal --> In | Little Endian Hex --> Out  #######################



def convert_decimal_to_bytes_and_le_hex(input_value):
    input_value = str(input_value).replace(',', '').replace('.', '')
    byte_value = struct.pack('<I', int(input_value))
    hex_string = strip_trailing_zeros(byte_value.hex())
    hex_value = f'0x{pad_hex_values(hex_string)}'
    hex_separated = byte_value.hex(' ', 1).upper()
    return byte_value, hex_value, hex_separated



##############################################################################
#                                                                            #
#                      Convert Hex and Decimal Function                      #
#                                                                            #
##############################################################################



'''
This function converts the input value to:
    • Decimal (Integer)
    • Hex (String)
    • Binary (String)


For the input value to be recognized as Hex, it must must start with '0x'.
Binary Values that result in less than 8 characters are padded.


Example:
    Decimal: 21
    Hex: 0x15
    Binary: 10101
    Padded Binary: 00010101


Hex Values are padded to an even number of digits.


Example:
    Decimal: 2147
    Hex: 0x0863
    Binary: 100001100011


The input value can be an integer or a string.
As a string, the value can use commas or periods (full-stops) to separate the digits.


Example:
    Integer: 2147483647
    String: '2147483647'
    Comma Separated: '2,147,483,647'
    Period (Full-Stop) Separated: '2.147.483.647'
'''



#######################  Decimal or Hex --> In | Decimal, Hex, Binary --> Out  #######################



def convert_hex_and_decimal(input_value):
    input_string = str(input_value).replace(',', '').replace('.', '')
    if input_string.startswith('0x'):
        decimal_value = int(input_string, 16)
        hex_string = input_string.replace('0x', '')
        hex_value = f'0x{pad_hex_values(hex_string)}'
        binary_value = f'{int(input_string, 16):08b}'
    else:
        decimal_value = int(input_string)
        hex_string = f'{int(input_string):x}'
        hex_value = f'0x{pad_hex_values(hex_string)}'
        binary_value = f'{int(input_string):08b}'
    return decimal_value, hex_value, binary_value


