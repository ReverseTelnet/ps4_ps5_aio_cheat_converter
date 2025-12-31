# ------------------------------------------------------------------------------------------------------------------------------------
#
#
#   This Utility contains functions used to write files and save python objects to files.
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
#                    Write Variable to JSON File Function                    #
#                                                                            #
##############################################################################



'''
Used to write a Variable to a JSON file.
This function assumes the variable can be converted to JSON.
It provides an Indent of 4 to help with readability.
JSON is imported in the function namespace in case it is not desired globally.
'''



#######################  Always Log | Always Save JSON  #######################



def save_to_json_file(filename, a_variable):
    import json
    with open(filename, mode = 'w') as f:
        json_payload = json.dumps(a_variable, indent=4)
        f.write(json_payload)



##############################################################################
#                                                                            #
#                     Write String to Text File Function                     #
#                                                                            #
##############################################################################



'''
Used to write a pure string to a text file.
This function should be used when the string has carriage returns already present in the text.
'''



#######################  Always Log | Always Save Strings  #######################



def save_string_to_text_file(filename, a_variable, write_mode='w'):
    with open(filename, write_mode, encoding='utf-8') as f:
        f.write(f'{a_variable}')



##############################################################################
#                                                                            #
#           Standard Last Index - Write List to Text File Function           #
#                                                                            #
##############################################################################



'''
Used to Write a List to a text file.
Each Index in the List is written on a separate line.
No special treatment is given to the last index.
'''



#######################  Always Log / Always Save Text  #######################



def save_list_to_text_file(filename, a_variable, write_mode='w'):
    with open(filename, write_mode, encoding='utf-8') as f:
        for line in a_variable:
            f.write(f'{line}')



##############################################################################
#                                                                            #
#           Fully Customizable - Write List to Text File Function            #
#                                                                            #
##############################################################################



'''
Used to Write a List to a text file.
Each Index in the List is written on a separate line.
No special treatment is given to the last index.
The number of carriage returns can be defined through an input argument.
The default value is single carriage return which results in each index on a separate line.
'''



#######################  Always Log / Always Save Lists  #######################



def custom_save_list_to_text_file(filename, a_variable, write_mode='w', carriage_returns=''):
    with open(filename, write_mode, encoding='utf-8') as f:
        for line in a_variable:
            line = line + carriage_returns
            f.write(f'{line}')



##############################################################################
#                                                                            #
#                        Write Bytes to File Function                        #
#                                                                            #
##############################################################################



'''
Used to Write bytes to a file.
No encoding method is defined (or supported).

This function is used primarily to write MC4 files, though technically,
anything object in bytes format can be written to file using it.
'''



#######################  Always Log / Always Save Bytes  #######################



def write_bytes_to_file(filename, bytes_object, write_mode='wb'):
    with open(filename, write_mode) as f:
        f.write(bytes_object)


