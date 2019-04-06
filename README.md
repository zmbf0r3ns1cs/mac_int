![Screenshot](/images/mac_intLogo.png)

### macOS Artifact Intelligence Tool

mac_int is an interpretive, modular DFIR intelligence and artifact correlation tool designed to automatically identify patterns and connections between parsed artifact data from the SQLite output of Yogesh Khatri’s open source tool, **mac_apt**.

#### Requirements: Python 3.x - 32/64 bit
#### mac_apt: https://github.com/ydkhatri/mac_apt

### Background

Users of mac_int will have the ability to utilize pre-researched data interpretation for desired correlations, potentially saving time in a DFIR investigation. Numerous forensic artifacts within macOS can reflect the same event in different ways, allowing the correlation of these related data fragments to be used to provide a better, more fluid story of events that occurred on the system. Calling on the SQLite output of mac_apt, mac_int will combine previously performed research and user interaction to build a clearly defined timeline, all relevant to the needs specified by the user.

#### Features
- Cross-Platform (runs on any OS with Python 3.x)
- Intelligent "connective parsing" from mac_apt SQLite Database output
- Interpreted data can be displayed via HTML format for ease-of-use and readability

### Getting Started

To see all available options, run the following invocation:
```
python mac_int -h 
```

### Current Modules

mac_int operates off pre-defined Python3 scripts that are called upon using command arguments. This list is a constant work in progress - any new module based on mac_apt SQLite output can be created and added to the argument parser for command line accessibility. Below is a working table describing the current modules and their functionality:

| Module | Description | mac_apt Connections (Tables) |
| --- | --- | --- |
| MountedVolumes | Names, Creation Dates, First and Last Seen Dates, and Bash Sessions | RecentItems, Spotlight-1-store, BashSessions |
| UserInfo | Parse for all related **user information** on the system, including information such as mounted volumes and installed applications | InstallHistory, NetUsage, RecentItems, Safari, Dock Items |
| InstalledApps | Total or User-Based search for **updates**, **downloaded** and **installed applications** with their corresponding **network usage** | InstallHistory, Dock Items, RecentItems, Safari, NetUsage, BashSessions, Quarantine, Spotlight-1-store |
| InternetSearch | Parse for any **internet searches** that occured | Safari, Quarantine |
| NetworkInfo | Parse for any **network activity** that occured, including info such as WiFi, DHCP, AD, and network usage | Domain_ActiveDirectory, WiFi, Network_DHCP, Network_Interfaces, Network_Details |
| SystemInfo | Parse for any **internet searches** that occured | Basic_Info |

### Example Usage

Below you will find an example of mac_int usage, utilizing the `-mv` switch to run the Mounted Volumes module with username *"justin.boncaldo"* and output to a specified directory:
```
mac_int.py C:\Users\burnh\Desktop\Capstone\Mac_apt_Output\mac_apt02.db justin.boncaldo -o C:\Users\burnh\Desktop\Capstone\Mac_apt_Output -mv
```

Below is another example, this time utilizing the `-a` switch to run all mac_int modules together:
```
mac_int.py C:\Users\burnh\Desktop\Capstone\Mac_apt_Output\mac_apt02.db justin.boncaldo -a 
```
