![Screenshot](/images/mac_intLogo.png)

### macOS Artifact Intelligence Tool

mac_int is an interpretive DFIR intelligence and artifact correlation tool designed to automatically identify patterns and connections between parsed artifact data from the SQLite output of Yogesh Khatri’s open source tool, **mac_apt**.

#### Requirements: Python3 - 32/64 bit
#### mac_apt: https://github.com/ydkhatri/mac_apt

### Background

Users of mac_int will have the ability to utilize pre-researched data interpretation for desired correlations, potentially saving time in a DFIR investigation. Numerous forensic artifacts within macOS can reflect the same event in different ways, allowing the correlation of these related data fragments to be used to provide a better, more fluid story of events that occurred on the system. Calling on the SQLite output of mac_apt, mac_int will combine previously performed research and user interaction to build a clearly defined timeline, all relevant to the needs specified by the user.
