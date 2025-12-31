# PS4/PS5 - All-In-One Cheat Converter

Convert a JSON, SHN (XML), or MC4 cheat to a JSON, SHN (XML), or MC4 cheat.  

## About This Script
This script takes no command line arguments.  
When ran, a file selection dialog box opens.  

The script will then convert and standardize the input file three output files:
* JSON
* SHN
* MC4
&nbsp;

## Output Files and Directory
The output files are saved to `script_results` directory.  
Script Results will contain a sub-directory for the date (`log_date_folder`).  
The Log Date Folder will have sub-directories per Title-ID.  
&nbsp;

Example:
```perl
    script_results
        ├── 2025-12-28
        │   └── CUSA04480
        │       ├── CUSA04480_01.06.json
        │       ├── CUSA04480_01.06.mc4
        │       └── CUSA04480_01.06.shn
        ├── 2025-12-29
        │   └── CUSA02378
        │       ├── CUSA02378_01.52.json
        │       ├── CUSA02378_01.52.mc4
        │       └── CUSA02378_01.52.shn
        └── 2025-12-30
            └── CUSA00103
                ├── CUSA00103_01.04.json
                ├── CUSA00103_01.04.mc4
                └── CUSA00103_01.04.shn
```
&nbsp;


## Script Conversion Workflow
1. If input file is JSON:
   * Convert JSON to SHN
   * Encrypt SHN to MC4
&nbsp;

2. If input file is SHN:
   * Convert SHN to JSON
   * Encrypt SHN to MC4
&nbsp;

3. If input file is MC4:
   * Decrypt MC4 to SHN
   * Convert SHN to JSON
&nbsp;


## Python Version

Due to the various f-strings methods used, this script hard-enforces a minimum Python Version of 3.11.3.
