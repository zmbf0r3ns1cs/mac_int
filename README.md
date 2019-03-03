![Screenshot](/images/mac_intLogo.png)

### macOS Artifact Intelligence Tool

mac_int is an interpretive DFIR intelligence and artifact correlation tool designed to automatically identify patterns and connections between parsed artifact data from the SQLite output of Yogesh Khatri’s open source tool, **mac_apt**.

#### Requirements: Python3 - 32/64 bit
#### mac_apt: https://github.com/ydkhatri/mac_apt

### Background

Users of mac_int will have the ability to utilize pre-researched data interpretation for desired correlations, potentially saving time in a DFIR investigation. Numerous forensic artifacts within macOS can reflect the same event in different ways, allowing the correlation of these related data fragments to be used to provide a better, more fluid story of events that occurred on the system. Calling on the SQLite output of mac_apt, mac_int will combine previously performed research and user interaction to build a clearly defined timeline, all relevant to the needs specified by the user.

#### Features
- Cross-Platform (runs on any OS with Python3)
- Intelligent parsing from mac_apt SQLite Database output
- Interpreted data is displayed via HTML format for ease-of-use and readability

### Modules

mac_int operates off predefined Python3 scripts that are called upon using command arguments. This list is a work in progress - any newly created module can be created and added to the argument parser for mac_int for command line accessibility. Below is a working table describing the current modules and their functionality:

| Module | Description | mac_apt Connections (Tables) |
| --- | --- | --- |
| MountedVolumes | Names, Creation Dates, First and Last Seen Dates, and Bash Sessions | Spotlight-1-store, BashSessions |
| InstalledApps | Updates, Downloaded and Installed Applications | InstallHistory, DockItems, NetUsage |
| UserInfo | Parse for all related **user information** on the system, including information such as mounted volumes and installed applications | InstallHistory, NetUsage, RecentItems, Safari, DockItems |
| NetworkActivity | Parse for any **network activity** that occured, including info such as WiFi, DHCP, AD, and network usage | Network_DHCP, NetUsage |
