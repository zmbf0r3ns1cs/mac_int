'''
   Authors: Zachary Burnham (@zmbf0r3ns1cs), Justin Boncaldo (@boncaldoj), & Benjamin Estes 2019
   
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
import os
import mountedDevices

__VERSION = "0.1"
__STATUS = "ALPHA"
__PROGRAMNAME = "macOS Artifact Intelligence Tool"

#### MAIN PROGRAM ####

parser = argparse.ArgumentParser(description='mac_int is a program designed to apply intelligence to macOS artifacts found within mac_apt\'s SQLITE output.\n'\
                                                 'You are running {} version {} - {}'.format(__PROGRAMNAME, __VERSION, __STATUS), formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('input_path', help='Path to mac_apt SQLITE Database output')
parser.add_argument('-o', '--output_dir', help='Desired DIRECTORY to store mac_int output files')
parser.add_argument('user_name', help='Username of target account')
parser.add_argument('-mv', '--MountedVolumes', action="store_true", help='Runs for Mounted Volume Info')
parser.add_argument('-ui', '--UserInfo', action="store_true", help='Runs for User Info')
parser.add_argument('-ia', '--InstalledApps', action="store_true", help='Runs for Installed Application Info')
parser.add_argument('-na', '--NetworkActivity', action="store_true", help='Runs for Network Activity Info')
#arg_parser.add_argument('-t', '--target_info', help='Topics: Mounted Volumes, Network Activity, User Information, Installed Apps')
#arg_parser.add_argument('-c', '--case_type', help='ALTERNATIVE to TARGET_INFO: Incident Response (IR), IP Theft (IP)')
parser.add_argument('--version', action='version', version='%(prog)s {} ({})'.format(__VERSION, __STATUS))
args = parser.parse_args()

if args.output_dir:
    print("[#] Output directory for mac_int results set to '{}'".format(args.output_dir))
else:
    # Output to same directory as program by default
    cwd = os.getcwd()
    print("[!] No Output Directory specified!")
    print("[#] Using current directory ({}) for mac_int results...".format(cwd))
    args.output_dir = cwd

if args.MountedVolumes:
    mountedDevices.mountedDevicesRun(args.output_dir, args.input_path, args.user_name)
else:
    exit

if args.UserInfo:
    mountedDevices.mountedDevicesRun(args.output_dir, args.input_path, args.user_name)
else:
    exit

if args.InstalledApps:
    mountedDevices.mountedDevicesRun(args.output_dir, args.input_path, args.user_name)
else:
    exit

if args.NetworkActivity:
    mountedDevices.mountedDevicesRun(args.output_dir, args.input_path, args.user_name)
else:
    exit