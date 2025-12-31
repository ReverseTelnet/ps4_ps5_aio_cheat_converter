# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#
#   PS4/PS5 - All-In-One Cheat Converter
#
#   When run, the script will present a dialog box to select a Cheat File.
#
#   The script will then convert and standardize the input file three output files:
#       • JSON
#       • SHN
#       • MC4
#
#
#   The output files are saved to `script_results` directory.
#   Script Results will contain a sub-directory for the date (`log_date_folder`).
#   The Log Date Folder will have sub-directories per Title-ID.
#
#
#       script_results
#           ├── 2025-12-28
#           │   └── CUSA04480
#           │       ├── CUSA04480_01.06.json
#           │       ├── CUSA04480_01.06.mc4
#           │       └── CUSA04480_01.06.shn
#           ├── 2025-12-29
#           │   └── CUSA02378
#           │       ├── CUSA02378_01.52.json
#           │       ├── CUSA02378_01.52.mc4
#           │       └── CUSA02378_01.52.shn
#           └── 2025-12-30
#               └── CUSA00103
#                   ├── CUSA00103_01.04.json
#                   ├── CUSA00103_01.04.mc4
#                   └── CUSA00103_01.04.shn
#
#
#   Workflow:
#       If input is JSON:
#          • Convert JSON to SHN
#          • Encrypt SHN to MC4
#
#       If input is SHN:
#          • Convert SHN to JSON
#          • Encrypt SHN to MC4
#
#       If input is MC4:
#          • Decrypt MC4 to SHN
#          • Convert SHN to JSON
#
#
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                                Script Version Number                                                                #
#                                                                                                                                                     #
#######################################################################################################################################################



#######################  Script Version  #######################



SCRIPT_VERSION = 0.01



#########################################################################################################################################################
#                                                                                                                                                       #
#                                                               Python Version Enforcement                                                              #
#                                                                                                                                                       #
#########################################################################################################################################################



import sys



#######################  Check Python Version and Enforce  #######################



MAJOR_VERSION = sys.version_info[0]
MINOR_VERSION = sys.version_info[1]
MICRO_VERSION = sys.version_info[2]



if MAJOR_VERSION < 3:
    print('This script requires a minimum Python version of 3.11.3.')
    sys.exit(1)



if MINOR_VERSION == 11:
    if MICRO_VERSION < 3:
        print('This script requires a minimum Python version of 3.11.3.')
        sys.exit(1)



if MINOR_VERSION < 11:
    print('This script requires a minimum Python version of 3.11.3.')
    sys.exit(1)



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                               Various Helper Functions                                                              #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                             Constants Objects                              #
#                                                                            #
##############################################################################



import datetime
from utilities.common_utilities import PWD
from utilities.common_utilities import get_pwd_absolute_path



#######################  Initial Setup Constants  #######################



now = datetime.datetime.now()                   # Example: datetime.datetime(2025, 12, 30, 23, 54, 43, 715367)
log_date_folder = now.strftime('%Y-%m-%d')      # Example: '2025-12-30'
absolute_path = get_pwd_absolute_path(PWD)



##############################################################################
#                                                                            #
#                 Create Script Results Directories Function                 #
#                                                                            #
##############################################################################



from os import makedirs



#######################  Create Script Results Directories  #######################



def create_script_results_directories(title_id):
    try:
        makedirs(f'{absolute_path}/script_results/{log_date_folder}/{title_id}')
    except FileExistsError:
        pass



##############################################################################
#                                                                            #
#          Get Output Filename by Title-ID and Output Type Function          #
#                                                                            #
##############################################################################



#######################  Title-ID / Type --> In | Filename --> Out  #######################



def get_output_filename_by_title_and_type(output_type, title_id, title_id_and_version):
    file_path = f'{absolute_path}/script_results/{log_date_folder}/{title_id}'
    if output_type == 'json':
        output_filename = f'{file_path}/{title_id_and_version}.json'
    elif output_type == 'shn':
        output_filename = f'{file_path}/{title_id_and_version}.shn'
    elif output_type == 'mc4':
        output_filename = f'{file_path}/{title_id_and_version}.mc4'
    return output_filename



#######################################################################################################################################################
#                                                                                                                                                     #
#                                                                  Workflow Functions                                                                 #
#                                                                                                                                                     #
#######################################################################################################################################################



##############################################################################
#                                                                            #
#                     Cheat Conversion Workflow Function                     #
#                                                                            #
##############################################################################



from utilities.mc4_utilities import decrypt_mc4_to_shn
from utilities.shn_utilities import json_to_xml_workflow
from utilities.json_utilities import shn_to_json_workflow
from utilities.shn_utilities import normalize_xml_entity_idents



#######################  Any to Any Conversion Workflow  #######################



def conversion_workflow(file_type, file_data):
    if file_type == 'json':
        json_cheat_object = file_data
        shn_cheat_object = json_to_xml_workflow(file_data)
    elif file_type == 'shn':
        json_cheat_object = shn_to_json_workflow(file_data)
        shn_cheat_object = normalize_xml_entity_idents(file_data)
    elif file_type == 'mc4':
        mc4_decrypted = decrypt_mc4_to_shn(file_data)
        shn_cheat_object = normalize_xml_entity_idents(mc4_decrypted)
        json_cheat_object = shn_to_json_workflow(shn_cheat_object)
    return json_cheat_object, shn_cheat_object



##############################################################################
#                                                                            #
#                      Console Print Workflow Function                       #
#                                                                            #
##############################################################################



from rich import print as rich_print
from utilities.common_utilities import PRINT_NEWLINES



#######################  Visual Confirmation of the Script Functioning  #######################



def console_print_workflow(json_cheat_object, shn_cheat_object):
    rich_print(json_cheat_object)
    PRINT_NEWLINES(2)
    rich_print(shn_cheat_object)
    PRINT_NEWLINES(2)



##############################################################################
#                                                                            #
#                      Write and Save Workflow Function                      #
#                                                                            #
##############################################################################



from utilities.mc4_utilities import encrypt_shn_to_mc4
from utilities.write_and_save_utilities import save_to_json_file
from utilities.write_and_save_utilities import write_bytes_to_file
from utilities.write_and_save_utilities import save_string_to_text_file



#######################  Always Log | Always Save  #######################



def write_and_save_workflow(json_cheat_object, shn_cheat_object, title_id, title_id_and_version):
    final_json_filename = get_output_filename_by_title_and_type('json', title_id, title_id_and_version)
    save_to_json_file(final_json_filename, json_cheat_object)
        #
    final_shn_filename = get_output_filename_by_title_and_type('shn', title_id, title_id_and_version)
    save_string_to_text_file(final_shn_filename, shn_cheat_object)
        #
    mc4_data = encrypt_shn_to_mc4(shn_cheat_object)
    final_mc4_filename = get_output_filename_by_title_and_type('mc4', title_id, title_id_and_version)
    write_bytes_to_file(final_mc4_filename, mc4_data)



##############################################################################
#                                                                            #
#                    'if __name__ == __main__:' Function                     #
#                                                                            #
##############################################################################



from utilities.common_utilities import open_and_read_file_workflow



#######################  Putting It All Together  #######################



def if_name_equals_main():
    file_type, file_data, title_id_and_version = open_and_read_file_workflow()
    json_cheat_object, shn_cheat_object = conversion_workflow(file_type, file_data)
    title_id = title_id_and_version.split('_')[0].strip()
        #
    create_script_results_directories(title_id)
    console_print_workflow(json_cheat_object, shn_cheat_object)
    write_and_save_workflow(json_cheat_object, shn_cheat_object, title_id, title_id_and_version)



if_name_equals_main()


