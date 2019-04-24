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
from modules import mountedVolumes, installedApps, internetSearch, userInfo, systemInfo, networkInfo

__VERSION = "1.0"
__STATUS = "Release Candidate"
__PROGRAMNAME = "macOS Artifact Intelligence Tool"

#### MAIN PROGRAM ####

# Establish Arguments
parser = argparse.ArgumentParser(description='''
                              _       __ 
   ____ ___  ____ ______     (_)___  / /_
  / __ `__ \/ __ `/ ___/    / / __ \/ __/
 / / / / / / /_/ / /__     / / / / / /_  
/_/ /_/ /_/\__,_/\___/____/_/_/ /_/\__/  
                    /_____/              
                    
mac_int is a program designed to apply intelligence to macOS artifacts found within mac_apt\'s SQLITE output.
You are running {} version {} - {}\n
'''.format(__PROGRAMNAME, __VERSION, __STATUS), formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('input_path', help='Path to mac_apt SQLITE Database output')
parser.add_argument('user_name', help='Username of target account')
parser.add_argument('-a', '--all', action="store_true", help='Run a full scan utilizing all available mac_int modules')
parser.add_argument('-o', '--output_path', help='Desired DIRECTORY to store mac_int output files')
parser.add_argument('--html', action="store_true", help='Show results in HTML format')
parser.add_argument('-v', '--version', action='version', version='%(prog)s {} ({})'.format(__VERSION, __STATUS))

modules = parser.add_argument_group('available modules')
modules.add_argument('-mv', '--MountedVolumes', action="store_true", help='Runs for Mounted Volume Info')
modules.add_argument('-ui', '--UserInfo', action="store_true", help='Runs for User Information')
modules.add_argument('-ia', '--InstalledApps', action="store_true", help='Runs for Installed Application Info')
modules.add_argument('-is', '--InternetSearch', action="store_true", help='Runs for Internet Searches')
modules.add_argument('-ni', '--NetworkInfo', action="store_true", help='Runs for Network Information')
modules.add_argument('-si', '--SystemInfo', action="store_true", help='Runs for System Information')
args = parser.parse_args()

# Establish Actions
if args.output_path:
    print("[#] Output path for mac_int results set to '{}'".format(args.output_path))
else:
    # Output to same directory as program by default
    cwd = os.getcwd()
    print("[!] No Output Path specified!")
    print("[#] Using current directory ({}) for mac_int results...".format(cwd))
    args.output_path = cwd

if args.all:
    args.MountedVolumes = True
    args.UserInfo = True
    args.InstalledApps = True
    args.InternetSearch = True
    args.NetworkInfo = True
    args.SystemInfo = True
else:
    exit

# Mounted Devices Search
if args.MountedVolumes:
    mountedVolumes.mountedVolumesRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# User Information Search
if args.UserInfo:
    userInfo.userInfoRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# Installed Apps Search
if args.InstalledApps:
    installedApps.installedAppsRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# Internet Search
if args.InternetSearch:
    internetSearch.internetSearchRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# Network Information Search
if args.NetworkInfo:
    networkInfo.networkInfoRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# System Info Search
if args.SystemInfo:
    systemInfo.systemInfoRun(args.output_path, args.input_path, args.user_name)
    if args.all:
        print("------------------------------------------------------------")
else:
    exit

# HTML Output
if args.html:
    os.chdir('modules')
    exec(open('htmlOutput.py').read())
else:
    exit