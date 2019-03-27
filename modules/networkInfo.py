# Query Logic for Network Information v1.0
# Justin Boncaldo (@boncaldoj) 2019
# ----------------------------------------------------------

import sqlite3
import re
from var_db import *

user_name = 'justin.boncaldo'
#def systemInfoRun(output_dir, input_path, user_name):
#file = open(output_dir + "\\mac_int-SystemINFO-" + user_name + "-Output.txt", 'w+')
file = open("E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\NetworkInfo.txt", 'w+')
#connection = sqlite3.connect(input_path)
connection = sqlite3.connect("E:\\CAPSTONE\\Mac_apt_Output-20190117T201041Z-001\\Mac_apt_Output\\mac_apt02.db")
cursor = connection.cursor()

# Mounted Volume variables
global a, b, c, g, h, i, output, userSearch

def NetworkInfo():
    global a, b, c, g, h, i, output, userSearch
    # Define strings
    d = []
    e = []
    # Define counters
    end = "no"
    counter = 0
    output = None

    userSearch = user_name
    print("[#] Parsing Network Info...")
    print("[~] Finding Application Network Usage...")
    while end != "yes":
        if counter in (0, 1, 2, 3, 4, 5, 6):
            while counter in (0, 1, 2, 3, 4, 5, 6):
                if counter == 0:
                    a = n
                    b = nU
                    c = T
                    g = App
                elif counter == 1:
                    a = fSD
                    b = nU
                    c = T
                    g = App
                elif counter == 2:
                    a = lSD
                    b = nU
                    c = T
                    g = App
                elif counter == 3:
                    a = win
                    b = nU
                    c = T
                    g = App
                elif counter == 4:
                    a = wout
                    b = nU
                    c = T
                    g = App
                elif counter == 5:
                    a = wirIn
                    b = nU
                    c = T
                    g = App
                elif counter == 6:
                    a = wirOut
                    b = nU
                    c = T
                    g = App
                else:
                    print("A counting error has occurred")

                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))

                output = cursor.fetchall()
                del d[:]
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    # Volume Name List Start
                    if counter == 0:
                        inst_appName_List.append(string1)
                        AppNameLength = int = len(inst_appName_List)
                    elif counter == 1:
                        inst_fSD_List.append(string1)
                        fSDLength = int = len(inst_fSD_List)
                    elif counter == 2:
                        inst_lSD_List.append(string1)
                        lSDLength = int = len(inst_lSD_List)
                    elif counter == 3:
                        inst_wifiIn_List.append(string1)
                        AppNameLength = int = len(inst_wifiIn_List)
                    elif counter == 4:
                        inst_wifiOut_List.append(string1)
                        wOutLength = int = len(inst_wifiOut_List)
                    elif counter == 5:
                        inst_wiredIn_List.append(string1)
                        wirInLength = int = len(inst_wiredIn_List)
                    elif counter == 6:
                        inst_wiredOut_List.append(string1)
                        wirOutLength = int = len(inst_wiredOut_List)
                    else:
                        continue
                counter = counter + 1
        elif counter in (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                         31, 32, 33, 34):
            while counter in (7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                              29, 30, 31, 32, 33, 34):
                # 7 - 14 Domain_ActiveDirectory Table
                # 8 - 26 Wifi
                if counter == 7:
                    a = network_d
                    b = D_AD
                elif counter == 8:
                    a = 'forest'
                    b = D_AD
                elif counter == 9:
                    a = 'trust domain'
                    b = D_AD
                elif counter == 10:
                    a = tac
                    b = D_AD
                elif counter == 11:
                    a = nn
                    b = D_AD
                elif counter == 12:
                    a = tkp
                    b = D_AD
                elif counter == 13:
                    a = allowmulti
                    b = D_AD
                elif counter == 14:  # Domain_ActiveDirectory Ends
                    a = cLUL
                    b = D_AD
                elif counter == 15:  # Wifi Table Begins
                    print("[~] Finding Wifi Info...")
                    a = n
                    b = Wifi
                elif counter == 16:
                    a = ssids
                    b = Wifi
                elif counter == 17:
                    a = sT
                    b = Wifi
                elif counter == 18:
                    a = lC
                    b = Wifi
                elif counter == 19:
                    a = rPT
                    b = Wifi
                elif counter == 20:
                    a = lconnC
                    b = Wifi
                elif counter == 21:
                    a = oCH
                    b = Wifi
                elif counter == 22:
                    a = 'Closed'
                    b = Wifi
                elif counter == 23:
                    a = 'Passpoint'
                    b = Wifi
                elif counter == 24:
                    a = 'Disabled'
                    b = Wifi
                elif counter == 25:
                    a = pHot
                    b = Wifi
                elif counter == 26:  # Wifi Table Ends
                    a = pHN
                    b = Wifi
                elif counter == 27:  # Network_DHCP Table Begins
                    a = 'Interface'
                    b = nDHCP
                elif counter == 28:
                    a = Mac
                    b = nDHCP
                elif counter == 29:
                    a = IP
                    b = nDHCP
                elif counter == 30:
                    a = lL
                    b = nDHCP
                elif counter == 31:
                    a = leaseSD
                    b = nDHCP
                elif counter == 32:
                    a = rHA
                    b = nDHCP
                elif counter == 33:
                    a = rIP
                    b = nDHCP
                elif counter == 34:
                    a = 'SSID'
                    b = nDHCP
                else:
                    print("A counting error has occurred")
                cursor.execute('SELECT "{}" FROM "{}"'.format(a, b),)
                output = cursor.fetchall()
                del d[:]
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    # Volume Name List Start
                    if counter == 7:
                        network_domainList.append(string1)
                    elif counter == 8:
                        network_forestList.append(string1)
                    elif counter == 9:
                        network_trustDomainList.append(string1)
                    elif counter == 10:
                        network_trustAccList.append(string1)
                    elif counter == 11:
                        network_nodeNameList.append(string1)
                    elif counter == 12:
                        network_trustKPrincipalList.append(string1)
                    elif counter == 13:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_allowmultiDomainList.append(string2)
                    elif counter == 14:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_cacheLastUserLogonList.append(string2)
                    elif counter == 15:
                        network_wifiNameList.append(string1)
                    elif counter == 16:
                        network_SSIDStringList.append(string1)
                    elif counter == 17:
                        network_SecurityTypeList.append(string1)
                    elif counter == 18:
                        network_lastConnectedList.append(string1)
                    elif counter == 19:
                        network_roamingProfileTypeList.append(string1)
                    elif counter == 20:
                        network_lastConnectedChannelList.append(string1)
                    elif counter == 21:
                        network_otherChannelHistoryList.append(string1)
                    elif counter == 22:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_ClosedList.append(string2)
                    elif counter == 23:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_PasspointList.append(string2)
                    elif counter == 24:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_DisabledList.append(string2)
                    elif counter == 25:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_personalHotspotList.append(string2)
                    elif counter == 26:
                        if string1 == '0':
                            string2 = 'No'
                        elif string1 == '1':
                            string2 = 'Yes'
                        else:
                            string2 = string1
                        network_possiblyHiddenNetworkList.append(string2)
                    elif counter == 27:
                        network_interfaceList.append(string1)
                    elif counter == 28:
                        network_macAddressList.append(string1)
                    elif counter == 29:
                        network_IPAddressList.append(string1)
                    elif counter == 30:
                        network_leaseLengthList.append(string1)
                    elif counter == 31:
                        network_leaseStartDateList.append(string1)
                    elif counter == 32:
                        network_routerHardwareAddressList.append(string1)
                    elif counter == 33:
                        network_routerIPAddressList.append(string1)
                    elif counter == 34:
                        network_SSIDList.append(string1)
                    else:
                        continue
                counter = counter + 1

        elif counter in (35, 36, 37, 38, 39, 40, 41, 42, 43, 44):  # Begin Tricky bit
            network_Placeholder = None
            if counter == 35:
                interfaceCount  = 0
                network_Placeholder = network_macAddressList
                a = 'BSD Name'
                b = nInterface
                c = 'IOMACAddress'
                g = network_macAddressList[interfaceCount]
            elif counter == 36:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = 'Hardware'
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 37:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = 'UUID'
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 38:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = IPv4confm
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 39:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = IPv6confm
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 40:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = 'Type'
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 41:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = uDefN
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 42:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = pEL
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 43:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = smbNBN
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]
            elif counter == 44:
                interfaceCount = 0
                network_Placeholder = network_BSDNameList
                a = smbWork
                b = nDet
                c = dName
                g = network_BSDNameList[interfaceCount]

            while interfaceCount < len(network_Placeholder):
                cursor.execute('SELECT "{}" FROM "{}" WHERE "{}" LIKE ?'.format(a, b, c), (g,))
                output = cursor.fetchall()
                del d[:]
                for row in output:
                    d.append(str(row[0]))
                pos = 0
                for (row) in output:
                    string1 = str(d[pos])
                    pos = pos + 1
                    if counter == 35:
                        network_BSDNameList.append(string1)
                    elif counter == 36:
                        network_HardwareList.append(string1)
                    elif counter == 37:
                        network_UUIDList.append(string1)
                    elif counter == 38:
                        network_IPv4ConfigMethodList.append(string1)
                    elif counter == 39:
                        network_IPv6ConfigMethodList.append(string1)
                    elif counter == 40:
                        network_TypeList.append(string1)
                    elif counter == 41:
                        network_UserDefinedNameList.append(string1)
                    elif counter == 42:
                        network_ProxiesExceptionsList.append(string1)
                    elif counter == 43:
                        network_SMBNetBiosNameList.append(string1)
                    elif counter == 44:
                        network_SMBWorkgroupList.append(string1)
                interfaceCount = interfaceCount + 1

            counter = counter + 1

                    # End Tricky bit



            #         interfaceCount = 0
            #         while interfaceCount < network_interfaceList:
            #             a = 'BSD Name'
            #             b = nINT
            #             c = 'IOMACAddress'
            #             g = network_macAddressList[interfaceCount]
            #
            #             cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
            #             output = cursor.fetchall()
            #             del d[:]
            #             for row in output:
            #                 d.append(str(row[0]))
            #             pos = 0
            #             for (row) in output:
            #                 string1 = str(d[pos])
            #                 pos = pos + 1
            #                 network_BSDNameList.append(string1)
            #             interfaceCount = interfaceCount + 1
            #
            #         interfaceCount2 = 0
            #         while interfaceCount2 < network_BSDNameList:
            #             a = 'Hardware'
            #             b = nDet
            #             c = dName
            #             g = network_BSDNameList[interfaceCount2]
            #
            #             cursor.execute('SELECT "{}" FROM "{}" WHERE "{}"=?'.format(a, b, c), (g,))
            #             output = cursor.fetchall()
            #             del d[:]
            #             for row in output:
            #                 d.append(str(row[0]))
            #             pos = 0
            #             for (row) in output:
            #                 string1 = str(d[pos])
            #                 pos = pos + 1
            #                 network_HardwareList.append(string1)
            #             interfaceCount2 = interfaceCount2 + 1
            #     else:
            #         continue
            # counter = counter + 1



        else:
            # Calculates total app internet usage.
            # Steps through each app name, and adds up all wifi in/out and wired in/outs
            totalCount = 0
            posx = 0
            while totalCount < AppNameLength:
                # Position of each item in lists
                inst_totalNetUsage_List.append((float(inst_wifiIn_List[posx])) + float(inst_wifiOut_List[posx]) + float(
                    inst_wiredIn_List[posx]) + float(inst_wiredOut_List[posx]))
                totalCount = totalCount + 1
                posx = posx + 1
            end = "yes"

    print(network_IPv4ConfigMethodList)
    print(network_IPv6ConfigMethodList)
    print(network_TypeList)
    print(network_UserDefinedNameList)
    print(network_ProxiesExceptionsList)
    print(network_SMBNetBiosNameList)
    print(network_SMBWorkgroupList)
    # Domain_ActiveDirectory
    line1 = 0
    writePos1 = 0
    while line1 < len(network_domainList):
        file.write("Network Information\n\n")
        file.write("Domain name: " + str(network_domainList[writePos1]) + "\nForest: " + str(
            network_forestList[writePos1]) + "\nTrust Domain name: " + str(
            network_trustDomainList[writePos1]) + "\nTrust Account: " + str(
            network_trustAccList[writePos1]) + "\nNode name: " + str(
            network_nodeNameList[writePos1]) + "\nTrust Kerberos Principal: " + str(
            network_trustKPrincipalList[writePos1]) + "\nAllow multi-Domain?: " + str(
            network_allowmultiDomainList[writePos1]) + "\nCache Last User Logon?: " + str(
            network_cacheLastUserLogonList[writePos1]) + "\n")
        line1 = line1 + 1
        writePos1 = writePos1 + 1
    file.write("\n\n")

    # Wifi
    line1 = 0
    writePos1 = 0
    while line1 < len(network_wifiNameList):
        file.write("Wifi name: " + str(network_wifiNameList[writePos1]) + "\nSSID String: " + str(
            network_SSIDStringList[writePos1]) + "\nDomain Security Type: " + str(
            network_SecurityTypeList[writePos1]) + "\nDate Last Connected to " + str(
            network_wifiNameList[writePos1]) + ": " + str(
            network_lastConnectedList[writePos1]) + "\nRoaming Profile Type: " + str(
            network_roamingProfileTypeList[writePos1]) + "\nChannel Last Connected: " + str(
            network_lastConnectedChannelList[writePos1]) + "\nPrior Channel History: " + str(
            network_otherChannelHistoryList[writePos1]) + "\nIs Domain Closed?: " + str(
            network_ClosedList[writePos1]) + "\nIs Domain a Passpoint?: " + str(
            network_PasspointList[writePos1]) + "\nIs the Domain Disabled?: " + str(
            network_DisabledList[writePos1]) + "\nIs this Domain a Personal Hotspot?: " + str(
            network_personalHotspotList[writePos1]) + "\nIs this Domain Possibly Hidden?: " + str(
            network_possiblyHiddenNetworkList[writePos1]) + "\n")
        line1 = line1 + 1
        writePos1 = writePos1 + 1
    file.write("\n\n")

    # Network_DHCP
    line1 = 0
    writePos1 = 0
    while line1 < len(network_interfaceList):
        file.write("Interface: " + str(network_interfaceList) + "\nMAC Address: " + str(
            network_macAddressList[writePos1]) + "\nSSID: " + str(
            network_SSIDList[writePos1]) + "\nIP Address: " + str(
            network_IPAddressList[writePos1]) + "\nIP Lease Start Date: " + str(
            network_leaseStartDateList[writePos1]) + "\nIP Lease Length: " + str(
            network_leaseLengthList[writePos1]) + "\nRouter IP Addressl: " + str(
            network_routerIPAddressList[writePos1]) + "\nARouter Hardware Address?: " + str(
            network_routerHardwareAddressList[writePos1]) + "\n")
        line1 = line1 + 1
        writePos1 = writePos1 + 1
    file.write("\n\n")

    # Writing file items for NetUsage -----------------------------
    line1 = 0
    writePos1 = 0
    file.write("Network usage was found for the following applications on this system:\n")
    while line1 < AppNameLength:
        file.write("\t-'" + str(inst_appName_List[writePos1]) + "' used a total of " + str(
            inst_totalNetUsage_List[writePos1]) + " bytes\n" + "\t\tFirst Seen on " + str(
            inst_fSD_List[writePos1]) + " and Last Seen on " + str(
            inst_lSD_List[writePos1]) + "\n\t\tWifi bytes in:\t " + str(inst_wifiIn_List[writePos1])
                   + "\n\t\tWifi bytes out:\t " + str(
            inst_wifiOut_List[writePos1]) + "\n\t\tWired bytes in:\t " + str(
            inst_wiredIn_List[writePos1]) + "\n\t\tWired bytes out: " + str(
            inst_wiredOut_List[writePos1]) + "\n")
        line1 = line1 + 1
        writePos1 = writePos1 + 1
    file.write("\n\n")



# Global Variables
a = "None"
b = "None"
c = "None"
g = "None"
h = "None"
i = "None"
output = None
userSearch = None

############# MAIN FUNCTION #############

# Run Functions
NetworkInfo()

# Show When Parsing Completed
print("[*] System Information Parsing Completed!")