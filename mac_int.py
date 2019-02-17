'''
   Authors: Zachary Burnham (@zmbf0r3ns1cs), Justin Boncaldo, & Benjamin Estes 2019 
   
   This file is part of mac_int (macOS Artifact Intelligence Tool).
   
   This is the main script - used to load the target database and any user
   preference before processing. 

   NOTE: This requires the SQLITE Database output from Yogesh Khatri's mac_apt tool
   against a macOS image.

    The tool and relevant documentation can be found here:
        https://github.com/ydkhatri/mac_apt 
   
   For usage information, run: 
    python mac_int.py -h

   NOTE: Currently only compatible with Python3.
   
'''
import argparse

__VERSION = "0.1"
__STATUS = "ALPHA"
__PROGRAMNAME = "macOS Artifact Intelligence Tool"

#### MAIN PROGRAM ####

arg_parser = argparse.ArgumentParser(description='mac_int is a program designed to apply intelligence to macOS artifacts found within mac_apt SQLITE output.\n'\
                                                 'You are running {} version {} - {}'.format(__PROGRAMNAME, __VERSION, __STATUS), formatter_class=argparse.RawTextHelpFormatter)
arg_parser.add_argument('input_path', help='Path to mac_apt SQLITE Database output')
arg_parser.add_argument('output_path', help='Path to store mac_int output files')
arg_parser.add_argument('-t', '--target_info', help='Topics: Mounted Volumes, Network Activity, User Information, App Installations, App Executions')
arg_parser.add_argument('-c', '--case_type', help='ALTERNATIVE to TARGET_INFO: Incident Response (IR), IP Theft (IP)')
args = arg_parser.parse_args()

if args.input_path and args.output_path:
    print ("Target database file: {}".format(args.input_path))
    print ("Output path set to {}".format(args.output_path))
    f = open(args.output_path,"x+")
