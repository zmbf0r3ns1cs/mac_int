
#Other Imports
import re
import datetime
import json
import os
from io import open

def htmlRun():
    os.chdir("../")
    file = open("output.html", 'w+')

    InstAppExists = os.path.isfile('tempinstalledApps.json')
    if InstAppExists:
        with open('tempinstalledApps.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            inst_processName1List = json_data['inst_processName1List']
            inst_processName2List = json_data['inst_processName2List']
            inst_processName3List = json_data['inst_processName3List']
            inst_appName_List = json_data['inst_appName_List']
            inst_fSD_List = json_data['inst_fSD_List']
            inst_lSD_List = json_data['inst_lSD_List']
            inst_wifiIn_List = json_data['inst_wifiIn_List']
            inst_wifiOut_List = json_data['inst_wifiOut_List']
            inst_wiredIn_List = json_data['inst_wiredIn_List']
            inst_wiredOut_List = json_data['inst_wiredOut_List']
            inst_date1List = json_data['inst_date1List']
            inst_date2List = json_data['inst_date2List']
            inst_date3List = json_data['inst_date3List']
            inst_totalNetUsage_List = json_data['inst_totalNetUsage_List']
            inst_recentIName_List = json_data['inst_recentIName_List']
            inst_recentIURL_List = json_data['inst_recentIURL_List']
            inst_SNoT_List = json_data['inst_SNoT_List']
            inst_sURL_List = json_data['inst_sURL_List']
            inst_fileLabelList = json_data['inst_fileLabelList']
            inst_parentModifiedList = json_data['inst_parentModifiedList']
            inst_fileModifiedList = json_data['inst_fileModifiedList']
            inst_filePathList = json_data['inst_filePathList']
            inst_idn_List = json_data['inst_idn_List']
            inst_ifn_List = json_data['inst_ifn_List']
            inst_ik_List = json_data['inst_ik_List']
            inst_ps_List = json_data['inst_ps_List']
            inst_ida_List = json_data['inst_ida_List']
            inst_iwf_List = json_data['inst_iwf_List']
            inst_idn2_List = json_data['inst_idn2_List']
            inst_ifn2_List = json_data['inst_ifn2_List']
            inst_ik2_List = json_data['inst_ik2_List']
            inst_ps2_List = json_data['inst_ps2_List']
            inst_ida2_List = json_data['inst_ida2_List']
            inst_iwf2_List = json_data['inst_iwf2_List']
            user_name = json_data['user_name']
    else:
        inst_processName1List = []
        inst_processName2List = []
        inst_processName3List = []
        inst_appName_List = []
        inst_fSD_List = []
        inst_lSD_List = []
        inst_wifiIn_List = []
        inst_wifiOut_List = []
        inst_wiredIn_List = []
        inst_wiredOut_List = []
        inst_date1List = []
        inst_date2List = []
        inst_date3List = []
        inst_totalNetUsage_List = []
        inst_recentIName_List = []
        inst_recentIURL_List = []
        inst_SNoT_List = []
        inst_sURL_List = []
        inst_fileLabelList = []
        inst_parentModifiedList = []
        inst_fileModifiedList = []
        inst_filePathList = []
        inst_idn_List = []
        inst_ifn_List = []
        inst_ik_List = []
        inst_ps_List = []
        inst_ida_List = []
        inst_iwf_List = []
        inst_idn2_List = []
        inst_ifn2_List = []
        inst_ik2_List = []
        inst_ps2_List = []
        inst_ida2_List = []
        inst_iwf2_List = []
        user_name = "Username Unavailable"

    SysInfoExists = os.path.isfile('tempsystemInfo.json')
    if SysInfoExists:
        with open('tempsystemInfo.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            system_Model = json_data['system_Model']
            system_version1 = json_data['system_version1']
            system_version2 = json_data['system_version2']
            system_serial = json_data['system_serial']
            system_computerName = json_data['system_computerName']
            system_localHostName = json_data['system_localHostName']
            system_timezone = json_data['system_timezone']
            system_lastUserName = json_data['system_lastUserName']
            system_lastLoginStatus = json_data['system_lastLoginStatus']
            system_lastLoginTime = json_data['system_lastLoginTime']
            system_loginText = json_data['system_loginText']
            system_NumberofFiles = json_data['system_NumberofFiles']
            system_NumberofFolders = json_data['system_NumberofFolders']
            system_blockSize = json_data['system_blockSize']
            system_Created = json_data['system_Created']
            system_Modified = json_data['system_Modified']
            system_Checked = json_data['system_Checked']
            system_Backup = json_data['system_Backup']
            system_Mounted = json_data['system_Mounted']
            user_name = json_data['user_name']
    else:
        system_Model = []
        system_version1 = []
        system_version2 = []
        system_serial = []
        system_computerName = []
        system_localHostName = []
        system_timezone = []
        system_lastUserName = []
        system_lastLoginStatus = []
        system_lastLoginTime = []
        system_loginText = []
        system_NumberofFiles = []
        system_NumberofFolders = []
        system_blockSize = []
        system_Created = []
        system_Modified = []
        system_Checked = []
        system_Backup = []
        system_Mounted = []
        user_name = "Username Unavailable"

    IntSearchExists = os.path.isfile('tempinternetSearch.json')
    if IntSearchExists:
        with open('tempinternetSearch.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            internet_SafariDLName_List = json_data['internet_SafariDLName_List']
            internet_SafariDLURL_List = json_data['internet_SafariDLURL_List']
            internet_SafariDLDate_List = json_data['internet_SafariDLDate_List']
            internet_SafariDLOther_List = json_data['internet_SafariDLOther_List']
            internet_SafariLSName_List = json_data['internet_SafariLSName_List']
            internet_SafariLSURL_List = json_data['internet_SafariLSURL_List']
            internet_SafariLSDate_List = json_data['internet_SafariLSDate_List']
            internet_SafariLSOther_List = json_data['internet_SafariLSOther_List']
            internet_SafariRCName_List = json_data['internet_SafariRCName_List']
            internet_SafariRCURL_List = json_data['internet_SafariRCURL_List']
            internet_SafariRCDate_List = json_data['internet_SafariRCDate_List']
            internet_SafariRCOther_List = json_data['internet_SafariRCOther_List']
            internet_SafariHName_List = json_data['internet_SafariHName_List']
            internet_SafariHURL_List = json_data['internet_SafariHURL_List']
            internet_SafariHDate_List = json_data['internet_SafariHDate_List']
            internet_SafariHOther_List = json_data['internet_SafariHOther_List']
            internet_SafariOISLTName_List = json_data['internet_SafariOISLTName_List']
            internet_SafariOISLTURL_List = json_data['internet_SafariOISLTURL_List']
            internet_SafariOISLTDate_List = json_data['internet_SafariOISLTDate_List']
            internet_SafariOISLTType_List = json_data['internet_SafariOISLTType_List']
            internet_SafariOIRSName_List = json_data['internet_SafariOIRSName_List']
            internet_SafariOIRSURL_List = json_data['internet_SafariOIRSURL_List']
            internet_SafariOIRSDate_List = json_data['internet_SafariOIRSDate_List']
            internet_SafariOIRSType_List = json_data['internet_SafariOIRSType_List']
            internet_SafariOITSName_List = json_data['internet_SafariOITSName_List']
            internet_SafariOITSURL_List = json_data['internet_SafariOITSURL_List']
            internet_SafariOITSDate_List = json_data['internet_SafariOITSDate_List']
            internet_SafariOITSOther_List = json_data['internet_SafariOITSOther_List']
            internet_SafariOIFVName_List = json_data['internet_SafariOIFVName_List']
            internet_SafariOIFVURL_List = json_data['internet_SafariOIFVURL_List']
            internet_SafariOIFVDate_List = json_data['internet_SafariOIFVDate_List']
            internet_SafariOIFVOther_List = json_data['internet_SafariOIFVOther_List']
            internet_SafariOIBName_List = json_data['internet_SafariOIBName_List']
            internet_SafariOIBURL_List = json_data['internet_SafariOIBURL_List']
            internet_SafariOIBDate_List = json_data['internet_SafariOIBDate_List']
            internet_SafariOIBType_List = json_data['internet_SafariOIBType_List']
            internet_QuarantineName_List = json_data['internet_QuarantineName_List']
            internet_QuarantineABID_List = json_data['internet_QuarantineABID_List']
            internet_QuarantineTS_List = json_data['internet_QuarantineTS_List']
            internet_QuarantineOURL_List = json_data['internet_QuarantineOURL_List']
            internet_QuarantineOTitle_List = json_data['internet_QuarantineOTitle_List']
            internet_QuarantineDURL_List = json_data['internet_QuarantineDURL_List']
            user_name = json_data['user_name']
    else:
        internet_SafariDLName_List = []
        internet_SafariDLURL_List = []
        internet_SafariDLDate_List = []
        internet_SafariDLOther_List = []
        internet_SafariLSName_List = []
        internet_SafariLSURL_List = []
        internet_SafariLSDate_List = []
        internet_SafariLSOther_List = []
        internet_SafariRCName_List = []
        internet_SafariRCURL_List = []
        internet_SafariRCDate_List = []
        internet_SafariRCOther_List = []
        internet_SafariHName_List = []
        internet_SafariHURL_List = []
        internet_SafariHDate_List = []
        internet_SafariHOther_List = []
        internet_SafariOISLTName_List = []
        internet_SafariOISLTURL_List = []
        internet_SafariOISLTDate_List = []
        internet_SafariOISLTType_List = []
        internet_SafariOIRSName_List = []
        internet_SafariOIRSURL_List = []
        internet_SafariOIRSDate_List = []
        internet_SafariOIRSType_List = []
        internet_SafariOITSName_List = []
        internet_SafariOITSURL_List = []
        internet_SafariOITSDate_List = []
        internet_SafariOITSOther_List = []
        internet_SafariOIFVName_List = []
        internet_SafariOIFVURL_List = []
        internet_SafariOIFVDate_List = []
        internet_SafariOIFVOther_List = []
        internet_SafariOIBName_List = []
        internet_SafariOIBURL_List = []
        internet_SafariOIBDate_List = []
        internet_SafariOIBType_List = []
        internet_QuarantineName_List = []
        internet_QuarantineABID_List = []
        internet_QuarantineTS_List = []
        internet_QuarantineOURL_List = []
        internet_QuarantineOTitle_List = []
        internet_QuarantineDURL_List = []
        user_name = "Username Unavailable"

    MntVolExists = os.path.isfile('tempmountedVolumes.json')
    if MntVolExists:
        with open('tempmountedVolumes.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            mount_volList = json_data['mount_volList']
            mount_crList = json_data['mount_crList']
            mount_fsList = json_data['mount_fsList']
            mount_lsList = json_data['mount_lsList']
            mount_bashList = json_data['mount_bashList']
            mount_ssList = json_data['mount_ssList']
            mount_seList = json_data['mount_seList']
            user_name = json_data['user_name']
    else:
        mount_volList = []
        mount_crList = []
        mount_fsList = []
        mount_lsList = []
        mount_bashList = []
        mount_ssList = []
        mount_seList = []
        user_name = "Username Unavailable"

    NetInfoExists = os.path.isfile('tempnetworkInfo.json')
    if NetInfoExists:
        with open('tempnetworkInfo.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            network_domainList = json_data['network_domainList']
            network_forestList = json_data['network_forestList']
            network_trustDomainList = json_data['network_trustDomainList']
            network_trustAccList = json_data['network_trustAccList']
            network_nodeNameList = json_data['network_nodeNameList']
            network_trustKPrincipalList = json_data['network_trustKPrincipalList']
            network_allowmultiDomainList = json_data['network_allowmultiDomainList']
            network_cacheLastUserLogonList = json_data['network_cacheLastUserLogonList']
            network_wifiNameList = json_data['network_wifiNameList']
            network_SSIDStringList = json_data['network_SSIDStringList']
            network_SecurityTypeList = json_data['network_SecurityTypeList']
            network_lastConnectedList = json_data['network_lastConnectedList']
            network_roamingProfileTypeList = json_data['network_roamingProfileTypeList']
            network_lastConnectedChannelList = json_data['network_lastConnectedChannelList']
            network_otherChannelHistoryList = json_data['network_otherChannelHistoryList']
            network_ClosedList = json_data['network_ClosedList']
            network_PasspointList = json_data['network_PasspointList']
            network_DisabledList = json_data['network_DisabledList']
            network_personalHotspotList = json_data['network_personalHotspotList']
            network_possiblyHiddenNetworkList = json_data['network_possiblyHiddenNetworkList']
            network_interfaceList = json_data['network_interfaceList']
            network_macAddressList = json_data['network_macAddressList']
            network_IPAddressList = json_data['network_IPAddressList']
            network_leaseLengthList = json_data['network_leaseLengthList']
            network_leaseStartDateList = json_data['network_leaseStartDateList']
            network_routerHardwareAddressList = json_data['network_routerHardwareAddressList']
            network_routerIPAddressList = json_data['network_routerIPAddressList']
            network_SSIDList = json_data['network_SSIDList']
            network_BSDNameList = json_data['network_BSDNameList']
            network_HardwareList = json_data['network_HardwareList']
            network_UUIDList = json_data['network_UUIDList']
            network_IPv4ConfigMethodList = json_data['network_IPv4ConfigMethodList']
            network_IPv6ConfigMethodList = json_data['network_IPv6ConfigMethodList']
            network_TypeList = json_data['network_TypeList']
            network_UserDefinedNameList = json_data['network_UserDefinedNameList']
            network_ProxiesExceptionsList = json_data['network_ProxiesExceptionsList']
            network_SMBNetBiosNameList = json_data['network_SMBNetBiosNameList']
            network_SMBWorkgroupList = json_data['network_SMBWorkgroupList']
            network_AllHardwareList = json_data['network_AllHardwareList']
            network_AllUUIDList = json_data['network_AllUUIDList']
            network_AllIPv4ConfigMethodList = json_data['network_AllIPv4ConfigMethodList']
            network_AllIPv6ConfigMethodList = json_data['network_AllIPv6ConfigMethodList']
            network_AllTypeList = json_data['network_AllTypeList']
            network_AllUserDefinedNameList = json_data['network_AllUserDefinedNameList']
            network_AllProxiesExceptionsList = json_data['network_AllProxiesExceptionsList']
            network_AllSMBNetBiosNameList = json_data['network_AllSMBNetBiosNameList']
            network_AllSMBWorkgroupList = json_data['network_AllSMBWorkgroupList']
            inst_appName_List = json_data['inst_appName_List']
            inst_totalNetUsage_List = json_data['inst_totalNetUsage_List']
            inst_fSD_List = json_data['inst_fSD_List']
            inst_lSD_List = json_data['inst_lSD_List']
            inst_wifiIn_List = json_data['inst_wifiIn_List']
            inst_wifiOut_List = json_data['inst_wifiOut_List']
            inst_wiredIn_List = json_data['inst_wiredIn_List']
            inst_wiredOut_List = json_data['inst_wiredOut_List']
            user_name = json_data['user_name']
    else:
        network_domainList = []
        network_forestList = []
        network_trustDomainList = []
        network_trustAccList = []
        network_nodeNameList = []
        network_trustKPrincipalList = []
        network_allowmultiDomainList = []
        network_cacheLastUserLogonList = []
        network_wifiNameList = []
        network_SSIDStringList = []
        network_SecurityTypeList = []
        network_lastConnectedList = []
        network_roamingProfileTypeList = []
        network_lastConnectedChannelList = []
        network_otherChannelHistoryList = []
        network_ClosedList = []
        network_PasspointList = []
        network_DisabledList = []
        network_personalHotspotList = []
        network_possiblyHiddenNetworkList = []
        network_interfaceList = []
        network_macAddressList = []
        network_IPAddressList = []
        network_leaseLengthList = []
        network_leaseStartDateList = []
        network_routerHardwareAddressList = []
        network_routerIPAddressList = []
        network_SSIDList = []
        network_BSDNameList = []
        network_HardwareList = []
        network_UUIDList = []
        network_IPv4ConfigMethodList = []
        network_IPv6ConfigMethodList = []
        network_TypeList = []
        network_UserDefinedNameList = []
        network_ProxiesExceptionsList = []
        network_SMBNetBiosNameList = []
        network_SMBWorkgroupList = []
        network_AllHardwareList = []
        network_AllUUIDList = []
        network_AllIPv4ConfigMethodList = []
        network_AllIPv6ConfigMethodList = []
        network_AllTypeList = []
        network_AllUserDefinedNameList = []
        network_AllProxiesExceptionsList = []
        network_AllSMBNetBiosNameList = []
        network_AllSMBWorkgroupList = []
        inst_appName_List = []
        inst_totalNetUsage_List = []
        inst_fSD_List = []
        inst_lSD_List = []
        inst_wifiIn_List = []
        inst_wifiOut_List = []
        inst_wiredIn_List = []
        inst_wiredOut_List = []
        user_name = "Username Unavailable"


    UserInfoExists = os.path.isfile('tempuserInfo.json')
    if UserInfoExists:
        with open('tempuserInfo.json', 'r', encoding='UTF-8') as f:
            json_data = json.load(f)  # opens the JSON file
            internet_SafariDLName_List = json_data['internet_SafariDLName_List']
            internet_SafariDLURL_List = json_data['internet_SafariDLURL_List']
            internet_SafariDLDate_List = json_data['internet_SafariDLDate_List']
            internet_SafariDLOther_List = json_data['internet_SafariDLOther_List']
            internet_SafariLSName_List = json_data['internet_SafariLSName_List']
            internet_SafariLSURL_List = json_data['internet_SafariLSURL_List']
            internet_SafariLSDate_List = json_data['internet_SafariLSDate_List']
            internet_SafariLSOther_List = json_data['internet_SafariLSOther_List']
            internet_SafariRCName_List = json_data['internet_SafariRCName_List']
            internet_SafariRCURL_List = json_data['internet_SafariRCURL_List']
            internet_SafariRCDate_List = json_data['internet_SafariRCDate_List']
            internet_SafariRCOther_List = json_data['internet_SafariRCOther_List']
            internet_SafariHName_List = json_data['internet_SafariHName_List']
            internet_SafariHURL_List = json_data['internet_SafariHURL_List']
            internet_SafariHDate_List = json_data['internet_SafariHDate_List']
            internet_SafariHOther_List = json_data['internet_SafariHOther_List']
            internet_SafariOISLTName_List = json_data['internet_SafariOISLTName_List']
            internet_SafariOISLTURL_List = json_data['internet_SafariOISLTURL_List']
            internet_SafariOISLTDate_List = json_data['internet_SafariOISLTDate_List']
            internet_SafariOISLTType_List = json_data['internet_SafariOISLTType_List']
            internet_SafariOIRSName_List = json_data['internet_SafariOIRSName_List']
            internet_SafariOIRSURL_List = json_data['internet_SafariOIRSURL_List']
            internet_SafariOIRSDate_List = json_data['internet_SafariOIRSDate_List']
            internet_SafariOIRSType_List = json_data['internet_SafariOIRSType_List']
            internet_SafariOITSName_List = json_data['internet_SafariOITSName_List']
            internet_SafariOITSURL_List = json_data['internet_SafariOITSURL_List']
            internet_SafariOITSDate_List = json_data['internet_SafariOITSDate_List']
            internet_SafariOITSOther_List = json_data['internet_SafariOITSOther_List']
            internet_SafariOIFVName_List = json_data['internet_SafariOIFVName_List']
            internet_SafariOIFVURL_List = json_data['internet_SafariOIFVURL_List']
            internet_SafariOIFVDate_List = json_data['internet_SafariOIFVDate_List']
            internet_SafariOIFVOther_List = json_data['internet_SafariOIFVOther_List']
            internet_SafariOIBName_List = json_data['internet_SafariOIBName_List']
            internet_SafariOIBURL_List = json_data['internet_SafariOIBURL_List']
            internet_SafariOIBDate_List = json_data['internet_SafariOIBDate_List']
            internet_SafariOIBType_List = json_data['internet_SafariOIBType_List']
            internet_QuarantineName_List = json_data['internet_QuarantineName_List']
            internet_QuarantineABID_List = json_data['internet_QuarantineABID_List']
            internet_QuarantineABID_List = json_data['internet_QuarantineABID_List']
            internet_QuarantineOURL_List = json_data['internet_QuarantineOURL_List']
            internet_QuarantineOTitle_List = json_data['internet_QuarantineOTitle_List']
            internet_QuarantineDURL_List = json_data['internet_QuarantineDURL_List']
            user_processName1List = json_data['user_processName1List']
            user_processName2List = json_data['user_processName2List']
            user_processName3List = json_data['user_processName3List']
            user_appName_List = json_data['user_appName_List']
            user_fSD_List = json_data['user_fSD_List']
            user_lSD_List = json_data['user_lSD_List']
            user_wifiIn_List = json_data['user_wifiIn_List']
            user_wifiOut_List = json_data['user_wifiOut_List']
            user_wiredIn_List = json_data['user_wiredIn_List']
            user_wiredOut_List = json_data['user_wiredOut_List']
            user_recentIName_List = json_data['user_recentIName_List']
            user_recentIURL_List = json_data['user_recentIURL_List']
            user_SNoT_List = json_data['user_SNoT_List']
            user_sURL_List = json_data['user_sURL_List']
            user_userUID_List = json_data['user_userUID_List']
            user_fileLabelList = json_data['user_fileLabelList']
            user_parentModifiedList = json_data['user_parentModifiedList']
            user_fileModifiedList = json_data['user_fileModifiedList']
            user_filePathList = json_data['user_filePathList']
            user_date1List = json_data['user_date1List']
            user_date2List = json_data['user_date2List']
            user_date3List = json_data['user_date3List']
            user_idn_List = json_data['user_idn_List']
            user_ifn_List = json_data['user_ifn_List']
            user_ian_List = json_data['user_ian_List']
            user_ik_List = json_data['user_ik_List']
            user_ps_List = json_data['user_ps_List']
            user_iwf_List = json_data['user_iwf_List']
            user_ida_List = json_data['user_ida_List']
            user_idn2_List = json_data['user_idn2_List']
            user_ifn2_List = json_data['user_ifn2_List']
            user_ian2_List = json_data['user_ian2_List']
            user_ik2_List = json_data['user_ik2_List']
            user_ps2_List = json_data['user_ps2_List']
            user_iwf2_List = json_data['user_iwf2_List']
            user_ida2_List = json_data['user_ida2_List']
            user_totalNetUsage_List = json_data['user_totalNetUsage_List']
            user_bashSSList = json_data['user_bashSSList']
            user_bashSEList = json_data['user_bashSEList']
            user_bashSCList = json_data['user_bashSCList']
            user_riNamevol_List = json_data['user_riNamevol_List']
            user_riURLvol_List = json_data['user_riURLvol_List']
            user_riInfovol_List = json_data['user_riInfovol_List']
            user_riNameplace_List = json_data['user_riNameplace_List']
            user_riURLplace_List = json_data['user_riURLplace_List']
            user_riInfoplace_List = json_data['user_riInfoplace_List']
            user_name = json_data['user_name']
    else:
        internet_SafariDLName_List = []
        internet_SafariDLURL_List = []
        internet_SafariDLDate_List = []
        internet_SafariDLOther_List = []
        internet_SafariLSName_List = []
        internet_SafariLSURL_List = []
        internet_SafariLSDate_List = []
        internet_SafariLSOther_List = []
        internet_SafariRCName_List = []
        internet_SafariRCURL_List = []
        internet_SafariRCDate_List = []
        internet_SafariRCOther_List = []
        internet_SafariHName_List = []
        internet_SafariHURL_List = []
        internet_SafariHDate_List = []
        internet_SafariHOther_List = []
        internet_SafariOISLTName_List = []
        internet_SafariOISLTURL_List = []
        internet_SafariOISLTDate_List = []
        internet_SafariOISLTType_List = []
        internet_SafariOIRSName_List = []
        internet_SafariOIRSURL_List = []
        internet_SafariOIRSDate_List = []
        internet_SafariOIRSType_List = []
        internet_SafariOITSName_List = []
        internet_SafariOITSURL_List = []
        internet_SafariOITSDate_List = []
        internet_SafariOITSOther_List = []
        internet_SafariOIFVName_List = []
        internet_SafariOIFVURL_List = []
        internet_SafariOIFVDate_List = []
        internet_SafariOIFVOther_List = []
        internet_SafariOIBName_List = []
        internet_SafariOIBURL_List = []
        internet_SafariOIBDate_List = []
        internet_SafariOIBType_List = []
        internet_QuarantineName_List = []
        internet_QuarantineABID_List = []
        internet_QuarantineABID_List = []
        internet_QuarantineOURL_List = []
        internet_QuarantineOTitle_List = []
        internet_QuarantineDURL_List = []
        user_processName1List = []
        user_processName2List = []
        user_processName3List = []
        user_appName_List = []
        user_fSD_List = []
        user_lSD_List = []
        user_wifiIn_List = []
        user_wifiOut_List = []
        user_wiredIn_List = []
        user_wiredOut_List = []
        user_recentIName_List = []
        user_recentIURL_List = []
        user_SNoT_List = []
        user_sURL_List = []
        user_userUID_List = []
        user_fileLabelList = []
        user_parentModifiedList = []
        user_fileModifiedList = []
        user_filePathList = []
        user_date1List = []
        user_date2List = []
        user_date3List = []
        user_idn_List = []
        user_ifn_List = []
        user_ian_List = []
        user_ik_List = []
        user_ps_List = []
        user_iwf_List = []
        user_ida_List = []
        user_idn2_List = []
        user_ifn2_List = []
        user_ian2_List = []
        user_ik2_List = []
        user_ps2_List = []
        user_iwf2_List = []
        user_ida2_List = []
        user_totalNetUsage_List = []
        user_bashSSList = []
        user_bashSEList = []
        user_bashSCList = []
        user_riNamevol_List = []
        user_riURLvol_List = []
        user_riInfovol_List = []
        user_riNameplace_List = []
        user_riURLplace_List = []
        user_riInfoplace_List = []
        user_name = "Username Unavailable"

    file.write("<!DOCTYPE html> \n" +
                    "<html lang=\"en\"> \n" +
                    "<head> \n" +
                    "<title> mac_int Output </title> \n" +
                    "<meta charset=\"UTF-8\"> \n" +
                    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"> \n" +
                    "<style> \n" +
                    "body {font-family: Times New Roman; margin-bottom: 100px;} \n" +
                    "html {overflow-y: scroll;} \n" +
                    ".tooltip { \n" +
                        "position: relative; \n" +
                        "display: inline-block; \n" +
                        "border-bottom: 1px dotted black; \n" +
                    "} \n" +
                    ".tooltip .tooltiptext { \n" +
                        "visibility: hidden; \n" +
                        "width: 200px; \n" +
                        "background-color: white; \n" +
                        "color: black; \n" +
                        "text-align: center; \n" +
                        "padding: 5px 0; \n" +
                        "border-style: solid; \n" +
                        "border-width: 1px; \n" +
                        "bottom: 100%; \n" +
                        "left: 50%; \n" +
                        "margin-left: -100px; \n" +
                        "position: absolute; \n" +
                        "z-index: 1; \n" +
                    "} \n" +
                    ".tooltip:hover .tooltiptext { \n" +
                        "visibility: visible; \n" +
                    "} \n" +
                    ".tab { \n" +
                        "\toverflow: hidden; \n" +
                        "\tborder: 1px #3a74d1; \n" +
                        "\tbackground-color: #eaf2ef; \n" +
                        "\tfont-weight: bold; \n" +
                    "}\n\n" +
                    ".card { \n" +
                        "\tbox-shadow: 0 4px 8px 0 rgba(0,0,0,0.2); \n" +
                        "\ttransition: 0.3s; \n" +
                        "\twidth: 30%; \n" +
                        "\tborder-radius: 5px; \n" +
                        "\tmargin: 5px; \n" +
                        "\tdisplay: inline-block; \n" +
                    "}\n\n" +
                    ".card:hover { \n" +
                        "\tbox-shadow: 0 8px 16px 0 rgba(0,0,0,0.2); \n" +
                    "}\n\n" +
                    ".card-container { \n" +
                        "\tpadding: 2px 16px; \n" +
                    "}\n\n" +
                    ".tab button { \n" +
                        "\tbackground-color: inherit; \n" +
                        "\tfloat: left; \n" +
                        "\tborder: none; \n" +
                        "\toutline: none; \n" +
                        "\tcursor: pointer; \n" +
                        "\tpadding: 14px 16px; \n" +
                        "\ttransition: 0.3s; \n" +
                        "\tfont-size: 17px; \n" +
                    "} \n\n" +
                    ".tab button:hover { \n" +
                        "\tbackground-color: #d3d3d3; \n" +
                    "} \n\n" +
                    ".tab button.active { \n" +
                        "\tbackground-color: #6F9CEB; \n" +
                    "} \n\n" +
                    ".tabcontent { \n" +
                        "\tdisplay: none; \n" +
                        "\tpadding: 6px 12px; \n" +
                        "\tborder: 1px solid #3a74d1; \n" +
                        "\theight: auto; \n" +
                    "} \n\n" +
                    ".header { \n" +
                        "\tpadding: 20px; \n" +
                        "\ttext-align: center; \n" +
                        "\tbackground: #fff; \n" +
                        "\tcolor: #141B41; \n" +
                        "\tfont-size: 30px; \n" +
                        "\tborder: 1px #3a74d1; \n" +
                    "} \n\n" +
                    ".row { \n" +
                        "\tdisplay: -ms-flexbox; \n" +
                        "\tdisplay: flex; \n" +
                        "\tflex-wrap: wrap; \n" +
                    "} \n\n" +
                    ".overview { \n" +
                        "\tflex: 19%; \n" +
                        "\tborder: 1px solid #3a74d1; \n" +
                        "\tbackground-color: #eaf2ef; \n" +
                    "} \n\n" +
                    ".main { \n" +
                        "\tflex: 80%; \n" +
                        "\twidth: 80%; \n" +
                    "} \n\n" +
                    ".footer { \n" +
                        "\tpadding: 10px; \n" +
                        "\ttext-align: center; \n" +
                        "\tbackground: #8aa399; \n" +
                        "\tborder: 1px #3a74d1; \n" +
                        "\tposition: static; \n" +
                        "\tleft: 0; \n" +
                        "\tbottom: 0; \n" +
                        "\twidth: 99%; \n" +
                    "} \n\n" +
                    "table { \n" +
                        "\tmargin:20px; \n" +
                    "} \n\n" +
                    ".accordion { \n" +
                        "\tbackground-color: #eaf2ef; \n" +
                        "\tcolor: #444; \n" +
                        "\tcursor: pointer; \n" +
                        "\tpadding: 18px; \n" +
                        "\twidth: 100%; \n" +
                        "\tborder: none; \n" +
                        "\ttest-align: left; \n" +
                        "\toutline: none; \n" +
                        "\tfont-size: 15px; \n" +
                        "\ttransition: 0.4s; \n" +
                        "\tfont-weight: bold; \n" +
                        #"\tposition: fixed; \n" +
                    "} \n\n" +
                    ".accordion:hover { \n" +
                        "\tbackground-color: #d3d3d3; \n" +
                    "} \n\n" +
                    ".accordion:after {\n" +
                        "\tcontent: '\\002B'; \n" +
                        "\tcolor: #777; \n" +
                        "\tfont-weight: bold; \n" +
                        "\tfloat: right; \n" +
                        "\tmargin-left: 5px; \n" +
                    "} \n\n" +
                    ".AccordionActive:after { \n" +
                        "\tcontent: \"\\2212\"; \n" +
                    "} \n\n" +
                    ".active { \n" +
                        "\tbackground-color: #6F9CEB; \n" +
                    "} \n\n" +
                    ".panel { \n" +
                        "\tpadding: 0 18px; \n" +
                        "\tdisplay: none; \n" +
                        "\tbackground-color: white; \n" +
                        "\toverflow: hidden; \n" +
                        "\twidth: auto; \n" +
                        "\tposition: relative; \n" +
                        "\tword-wrap: break-word; \n" +
                    "} \n\n" +
                    "strong.indent{ \n" +
                        "\tpadding-left: 2em; \n" +
                    "} \n\n" +
                   ".tooltip { \n" +
                       "\tposition: relative; \n" +
                       "\tdisplay: inline-block; \n" +
                       "\tborder-bottom: 1px dotted black \n" +
                   "} \n\n" +
                   ".tooltip.tooltiptext { \n" +
                       "\tvisibility: hidden; \n" +
                       "\twidth: 120px; \n" +
                       "\tbackground-color: black; \n" +
                       "\tcolor: #fff; \n" +
                       "\ttext - align: center; \n" +
                       "\tborder-radius: 6px; \n" +
                       "\tpadding: 5px 0; \n" +
                       "\tposition: absolute; \n" +
                       "\tz-index: 1; \n" +
                       "\tbottom: 100%; \n" +
                       "\tleft: 50%; \n" +
                       "\tmargin-left: -60px; \n" +
                   "} \n\n" +
                       ".tooltip:hover.tooltiptext { \n" +
                       "\tvisibility: visible; \n" +
                   "} \n\n" +
                    "</style> \n" +
                    "</head> \n" +
                    "<body> \n\n"
                        "<div class=\"header\"> \n" +
                        "\t<img src=\"images\\mac_intLogo.png\" alt=\"The logo for mac_int\" width=\"40%\" height=\"40%\">  \n" +
                    "</div> \n\n" +
                    "<div class=\"row\"> \n" +
                        "\t<div class=\"overview\"> \n" +
                            "\t\t<h2 style=\"text-align: center\"> Overview </h2> \n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Username for Data:</u> </strong></span>" + user_name + "</span><br><hr>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Model Name:</u> </strong></span><span>" + str(system_Model) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> OS Version:</u> </strong></span>" + str(system_version2) + "</span><span> </span><span>" + str(system_version1) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Hardware Serial Number:</u> </strong></span>" + str(system_serial) + "</span><br><hr>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Computer Name:</u> </strong></span>" + str(system_computerName) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Local Hostname:</u> </strong></span>" + str(system_localHostName) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Timezone:</u> </strong></span>" + str(system_timezone) + "</span><br><hr>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Last User:</u> </strong></span>" + str(system_lastUserName) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Last User Status:</u> </strong></span>" + str(system_lastLoginStatus) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Last Login Time:</u> </strong></span>" + str(system_lastLoginTime) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Login Screen Text:</u> </strong></span>" + str(system_loginText) + "</span><br><hr>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Volume's Total Files:</u> </strong></span>" + str(system_NumberofFiles) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Volume's Total Folders:</u> </strong></span>" + str(system_NumberofFolders) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Volume's Block Size:</u> </strong></span>" + str(system_blockSize) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Volume Created Date:</u> </strong></span>" + str(system_Created) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Volume's Last Modified Date:</u> </strong></span>" + str(system_Modified) + "</span><br><br>\n" +
                            "\t\t<span> <strong style=\"padding-left: 10px\"><u> Last Time Volume Check for Errors:</u> </strong></span>" + str(system_Checked) + "</span><br><br>\n")
    if len(system_Backup) == 0:
        file.write("\t\t<span> <strong style=\"padding-left: 10px\"><u> Last Time Volume Backed Up:</u> </strong></span>N/A</span><br><br>\n")
    else:
        file.write("\t\t<span> <strong style=\"padding-left: 10px\"><u> Last Time Volume Backed Up:</u> </strong></span>" + str(system_Backup) + "</span><br><br>\n")
    file.write("\t\t<span> <strong style=\"padding-left: 10px\"><u> Last Volume Mount Version:</u> </strong></span>" + str(system_Mounted) + "</span><br><br>\n" +
                            "\t\t</div> \n" +
                        "\t<div class=\"main\"> \n" +
                            "\t\t<div class=\"tab\"> \n" +
                                "\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'Mounted_Volumes')\"> Mounted Volumes </button> \n" +
                                "\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'Internet_Searches')\"> Internet Searches </button> \n" +
                                "\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'Network_Info')\"> Network Information </button> \n" +
                                "\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'User_Information')\"> User Information </button> \n" +
                                "\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'Installed_Apps')\"> Installed Applications </button> \n" +
                                #"\t\t\t<button class=\"tablinks\" onclick=\"openInfoTab(event, 'PlaceHolder')\"> PlaceHolder </button> \n" +
                            "\t\t</div> \n" +
                            "\t\t<div id=\"Mounted_Volumes\" class=\"tabcontent\"> \n")
    # Mounted Volumes Tab Information ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    MounterVolumesCheck = len(mount_volList) + len(mount_crList) + len(mount_bashList) + len(mount_ssList)
    if MounterVolumesCheck == 0:
        file.write("<p>This module was either not run or there is no output.</p>")
    else:
        file.write("\t\t\t<h2>Mounted Volume Information</h2> \n" +
                                    "\t\t\t<table style=\"width 100%; border-collapse: collapse\"> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Volume Name </th> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Created Date & Time </th> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> First Seen Date & Time </th> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Last Seen Date & Time </th> \n" +
                                        "\t\t\t\t</tr> \n")

        #Mounted Volumes Output Tab Information
        volLengthCounter = 0
        volLength = len(mount_volList)
        while volLengthCounter <= volLength - 1:
            file.write("\t\t\t\t<tr> \n")
            if mount_fsList[volLengthCounter] == '[]':
                file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + mount_volList[volLengthCounter] + "</td> \n")
            else:
                file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + mount_volList[volLengthCounter] + "<div class=\"tooltip\">*<span class=\"tooltiptext\">This is the drive that was imaged during the forensic acquisition</span></div></td> \n")
            mvCRstring = mount_crList[volLengthCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", mvCRstring)
            if DateMatch:
                mvCRdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                mvCRdate = '-'
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", mvCRstring)
            if TimeMatch:
                mvCRtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                mvCRtime = ''
            file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + str(mvCRdate) + "\t" + str(mvCRtime) + "</td> \n")

            mvFSstring = mount_crList[volLengthCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", mvFSstring)
            if DateMatch:
                mvFSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                mvFSdate = '-'
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", mvFSstring)
            if TimeMatch:
                mvFStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                mvFStime = ''
            if mount_fsList[volLengthCounter] == '[]':
                mvFSdate = '-'
                mvFStime = ''
            file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + str(mvFSdate) + "\t" + str(mvFStime) + "</td> \n")

            mvLSstring = mount_crList[volLengthCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", mvLSstring)
            if DateMatch:
                mvLSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                mvLSdate = '-'
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", mvLSstring)
            if TimeMatch:
                mvLStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                mvLStime = ''
            if mount_lsList[volLengthCounter] == '[]':
                mvLSdate = '-'
                mvLStime = ''
            file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + str(mvLSdate) + "\t" + str(mvLStime) + "</td> \n")

            file.write("\t\t\t\t</tr> \n")
            volLengthCounter = volLengthCounter + 1
            if volLengthCounter == volLength:
                file.write("\t\t\t</table>")
        file.write("<strong>Notes about Mounted Volume Information</strong><br> \n")
        file.write("<ul><li><p> If a time Date and Time are not available, the drive is more than likely a secondary drive or a removable device. Since these drives are not usually imaged, date and time information is not gathered by the mac_apt tool.</p></li>\n</ul>")
        file.write("\t\t\t\t<div> \n")
        #Mounted Volumes Bash Output
        mvBashLengthCounter = 0
        mvBashLength = len(mount_bashList)
        file.write("\t\t\t\t<h2>Bash Session Information</h2> \n")
        while mvBashLengthCounter <= mvBashLength - 1:
            if mount_bashList[mvBashLengthCounter] != '':
                file.write("\t\t\t<table style=\"width 100%; border-collapse: collapse\"> \n")
                file.write("\t\t\t\t<tr> \n")
                file.write("\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Start of Bash Session </th> \n")
                file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + mount_ssList[mvBashLengthCounter] + "</td> \n")
                file.write("\t\t\t\t</tr> \n")
                file.write("\t\t\t\t<tr> \n")
                file.write("\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> End of Bash Session </th> \n")
                file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + mount_seList[mvBashLengthCounter] + "</td> \n")
                file.write("\t\t\t\t</tr> \n")
                file.write("\t\t\t\t<tr> \n")
                file.write("\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Bash Command(s)<span class=\"tooltiptext\">Bash Commands are listed in the order ran and are seperated by a semicolon</span></div></th> \n")
                file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + mount_bashList[mvBashLengthCounter] + "</td> \n")
                file.write("\t\t\t\t</tr> \n")
                file.write("\t\t\t</table> \n")
            mvBashLengthCounter = mvBashLengthCounter + 1
        file.write("\t\t\t\t</div> \n")

        #End of Mounted Volume Information ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    file.write("\t\t</div> \n")

    #Start of Internet Searches Information -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    InternetSearchesCheck = len(internet_SafariRCOther_List) + len(internet_SafariRCURL_List) + len(internet_SafariLSName_List) + len(internet_SafariHURL_List) + len(internet_SafariOIFVOther_List) + len(internet_SafariRCDate_List)
    file.write("\t\t<div id=\"Internet_Searches\" class=\"tabcontent\"> \n")
    if InternetSearchesCheck == 0:
        file.write("<p>This module was either not run or there is no output.</p>")
    else:
        file.write("\t\t\t<button class=\"accordion\">Safari Info</button> \n" +
                                    "\t\t\t<div class=\"panel\"> \n")
        #Last Launch Date for Safari
        file.write("<h2>Last Launched Date and Time</h2>")
        ISLLstring = internet_SafariOISLTDate_List[0]
        DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISLLstring)
        if DateMatch:
            ISLLdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
        else:
            ISLLdate = "No Date Available"
        TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISLLstring)
        if TimeMatch:
            ISLLtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
        else:
            ISLLtime = "No Time Available"
        file.write("<strong>The user specified in the Overview last launched safari on </strong><span>" + str(ISLLdate) + "</span><strong> at </strong><span>" + str(ISLLtime) + "</span><br>\n")

        #Safari Bookmarks output tab
        file.write("<h2>Safari Bookmarks</h2>")
        ISBoomarkListLengthCounter = 0
        ISBookmarkListLength = len(internet_SafariOIBURL_List)
        if ISBookmarkListLength == 0:
            file.write("<strong>This User has no bookmarks on Safari.</strong>")
        else:
            while ISBoomarkListLengthCounter <= ISBookmarkListLength - 1:
                file.write("<strong><u>Bookmark Name:</u> </strong><span>" + internet_SafariOIBName_List[ISBoomarkListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\">Bookmark URL: </strong><span>" + internet_SafariOIBURL_List[ISBoomarkListLengthCounter] + "</span><br>\n")
                ISBstring = internet_SafariOIBDate_List[ISBoomarkListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISBstring)
                if DateMatch:
                    ISBdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISBdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISBstring)
                if TimeMatch:
                    ISBtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISBtime = "No Time Available"
                file.write("<strong class=\"indent\">This bookmark was created on </strong><span>" + str(ISBdate) + "</span><strong> at <strong><span>" + ISBtime + "</span><br>\n")
                file.write("<hr><br>")
                ISBoomarkListLengthCounter = ISBoomarkListLengthCounter + 1
        file.write("\t\t\t</div>"
                                    
                                    "\t\t\t<button class=\"accordion\">Downloads</button> \n" +
                                    "\t\t\t<div class=\"panel\"> \n")
        #Downloads from Safari Output Tab
        file.write("<h2>Downloads from Safari</h2> \n")
        ISSafariDLListLengthCounter = 0
        ISSafariDLListLength = len(internet_SafariDLName_List)
        if ISSafariDLListLength == 0:
            file.write("<strong>This User has no downloads from safari.</strong>")
        else:
            while ISSafariDLListLengthCounter <= ISSafariDLListLength - 1:
                file.write("<strong><u>File & URL:</u> </strong><span>" + internet_SafariDLName_List[ISSafariDLListLengthCounter] + "</span>\n <strong>was downloaded from this location</strong>\n<span style=\"color: blue\"> " + internet_SafariDLURL_List[ISSafariDLListLengthCounter] + "</span> <br>\n")
                if internet_SafariDLDate_List[ISSafariDLListLengthCounter] == 'None':
                    file.write("<strong class=\"indent\"><u>Date Downloaded:</u> </strong> <span>No Date Specified</span><br>")
                else:
                    file.write("<strong class=\"indent\"><u>Date Downloaded:</u> </strong><span>" + internet_SafariDLDate_List[ISSafariDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><div class=\"tooltip\"><u>Save Location:</u><span class=\"tooltiptext\">Location that the file was saved on the imaged system. This is stated as a relative path.</span></div> </strong> \n<span>" + internet_SafariDLOther_List[ISSafariDLListLengthCounter] + "</span> <br><br>")
                file.write("<hr><br>\n")
                ISSafariDLListLengthCounter = ISSafariDLListLengthCounter + 1

        #Quarantine Download Output Tab
        file.write("<h2>Downloads Passed Through Quarantine</h2> \n")
        ISQuarantineDLListLengthCounter = 0
        ISQuarantineDLListLength = len(internet_QuarantineOTitle_List)
        if ISQuarantineDLListLength == 0:
            file.write("<strong>This User has no downlaods that passed through quarantine.</strong>")
        else:
            while ISQuarantineDLListLengthCounter <= ISQuarantineDLListLength - 1:
                ISQDstring = internet_QuarantineTS_List[ISQuarantineDLListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISQDstring)
                if DateMatch:
                    ISQDdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISQDdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISQDstring)
                if TimeMatch:
                    ISQDtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISQDtime = "No Time Available"
                file.write("<strong><u>Browser & Date:</u> </strong><span>" + internet_QuarantineName_List[ISQuarantineDLListLengthCounter] + "<span><strong> was used on </strong><span>" + str(ISQDdate) + "</span><strong> at </strong><span>" + str(ISQDtime) + "</span><br> \n")
                file.write("<strong class=\"indent\"><u>Origin Title:</u> </strong><span>" + internet_QuarantineOTitle_List[ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Origin URL:</u> </strong><span>" + internet_QuarantineOURL_List[ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Data URL:</u> </strong><span style=\"color: blue\">" + internet_QuarantineDURL_List[ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Agent Bundle ID:</u> </strong><span>" + internet_QuarantineABID_List[ISQuarantineDLListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISQuarantineDLListLengthCounter = ISQuarantineDLListLengthCounter + 1

        file.write("\t\t\t</div>" +

                                    "\t\t\t<button class=\"accordion\">Site Visit Statistics</button> \n" +
                                    "\t\t\t<div class=\"panel\"> \n")

        #Frequently visited sites tab
        file.write("<h2>Frequently Visited Sites on Safari</h2> \n")
        ISFrequentlyVisistedListLengthCounter = 0
        ISFrequentlyVisistedListLength = len(internet_SafariOIFVURL_List)
        if ISFrequentlyVisistedListLength == 0:
            file.write("<strong>This User has no frequently visited sites on Safari.</strong>")
        else:
            while ISFrequentlyVisistedListLengthCounter <= ISFrequentlyVisistedListLength - 1:
                file.write("<strong><u>Site & URL:</u> </strong><span>" + internet_SafariOIFVName_List[ISFrequentlyVisistedListLengthCounter] + "</span><Strong> located at </strong><span style=\"color: blue\">" + internet_SafariOIFVURL_List[ISFrequentlyVisistedListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Date:</u> </strong><span>" + internet_SafariOIFVDate_List + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariOIFVOther_List + "</span><br>\n")
                file.write("<hr><br>\n")
                ISFrequentlyVisistedListLengthCounter = ISFrequentlyVisistedListLengthCounter + 1

        #Top visited Sites on Safari
        file.write("<h2>Top Visited Sites on Safari</h2> \n")
        ISTopVisitedSitesListLengthCounter = 0
        ISTopVisitedSitesListLength = len(internet_SafariOITSURL_List)
        if ISTopVisitedSitesListLength == 0:
            file.write("<strong>This User has no top visited sites on Safari.</strong>")
        else:
            while ISTopVisitedSitesListLengthCounter <= ISTopVisitedSitesListLength - 1:
                if internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] == 'http://www.apple.com/startpage/':
                    file.write("<strong><u>Site Title & URL:</u> </strong><span>Apple </span><strong> at the URL</strong><span style=\"color: blue\"> " + internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] + "</span><br>\n")
                else:
                    file.write("<strong><u>Site Title & URL:</u> </strong><span>" + internet_SafariOITSName_List[ISTopVisitedSitesListLengthCounter] + "</span><strong> at the URL </strong><span style=\"color: blue\">" + internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] + "</span><br>\n")
                ISTVstring = internet_SafariOITSDate_List[ISTopVisitedSitesListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISTVstring)
                if DateMatch:
                    ISTVdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISTVdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISTVstring)
                if TimeMatch:
                    ISTVtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISTVtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date:</u> </strong><span>" + str(ISTVdate) + "</span><span> </span><span>" + str(ISTVtime) + "<br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariOITSOther_List[ISTopVisitedSitesListLengthCounter] + "<br><br>\n")
                file.write("<hr><br>\n")
                ISTopVisitedSitesListLengthCounter = ISTopVisitedSitesListLengthCounter + 1
        file.write("\t\t\t</div>" +

                                    "\t\t\t<button class=\"accordion\">Searches</button> \n" +
                                    "\t\t\t<div class=\"panel\"> \n")

        #Recent Searches tab content
        file.write("<h2>Recent Searches on Safari</h2> \n")
        ISRecentSearchesListLengthCounter = 0
        ISRecentSearchesListLength = len(internet_SafariOIRSName_List)
        if ISRecentSearchesListLength == 0:
            file.write("<strong>This User has no recent searches on safari.</strong>")
        else:
            while ISRecentSearchesListLengthCounter <= ISRecentSearchesListLength - 1:
                file.write("<strong><u>Search Term:</u> </strong><span>" + internet_SafariOIRSName_List[ISRecentSearchesListLengthCounter] + "<span><br>\n ")
                ISRSstring = internet_SafariOIRSDate_List[ISRecentSearchesListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISRSstring)
                if DateMatch:
                    ISRSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISRSdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRSstring)
                if TimeMatch:
                    ISRStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISRStime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of Search:</u> </strong><span>" + str(ISRSdate) + "</span><span> </span><span>" + str(ISRStime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Type of Search:</u> </strong><span>" + internet_SafariOIRSType_List[ISRecentSearchesListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISRecentSearchesListLengthCounter = ISRecentSearchesListLengthCounter + 1

        #Search History tab content
        file.write("<h2>Safari Search History</h2>")
        ISSearchHistoryListLengthCounter = 0
        ISSearchHistoryListLength = len(internet_SafariHURL_List)
        if ISSearchHistoryListLength == 0:
            file.write("<strong>This User has no search history on safari.</strong>")
        else:
            while ISSearchHistoryListLengthCounter <= ISSearchHistoryListLength - 1:
                file.write("<strong><u>Search Query/Term & URL:</u> </strong><span>" + internet_SafariHName_List[ISSearchHistoryListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" + internet_SafariHURL_List[ISSearchHistoryListLengthCounter] + "</span><br>")
                ISHstring = internet_SafariHDate_List[ISSearchHistoryListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISHstring)
                if DateMatch:
                    ISHdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISHdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRSstring)
                if TimeMatch:
                    ISHtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISHtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of the Query/Search:</u> </strong><span>" + str(ISHdate) + "</span><span> </span><span>" + str(ISHtime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariHOther_List[ISSearchHistoryListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISSearchHistoryListLengthCounter = ISSearchHistoryListLengthCounter + 1
        file.write("\t\t\t</div>" +

                                    "\t\t\t<button class=\"accordion\">Previous Safari Session Information</button> \n" +
                                    "\t\t\t<div class=\"panel\"> \n")

        #Searches from last Session
        file.write("<h2>Searches Queries/Terms that were Auto-launched/Saved from Last Safari Session</h2>")
        ISLastSessionListLengthCounter = 0
        ISLastSessionListLength = len(internet_SafariLSURL_List)
        if ISLastSessionListLength == 0:
            file.write("<strong>This User has no searches from their last session on safari.</strong>")
        else:
            while ISLastSessionListLengthCounter <= ISLastSessionListLength - 1:
                file.write("<strong><u>Search Query/Term & URL:</u> </strong><span>" + internet_SafariLSName_List[ISLastSessionListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" + internet_SafariLSURL_List[ISLastSessionListLengthCounter] + "</span><br>\n")
                ISLSstring = internet_SafariLSDate_List[ISLastSessionListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISLSstring)
                if DateMatch:
                    ISLSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISLSdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISLSstring)
                if TimeMatch:
                    ISLStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISLStime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of the Query/Search:</u> </strong><span>" + str(ISLSdate) + "</span><span> </span><span>" + str(ISLStime) + "</span><br>\n")
                if internet_SafariLSOther_List[ISLastSessionListLengthCounter] == '':
                    file.write("<strong class=\"indent\"><u>Save Location:</u> </strong><span>No Save Location Found</span><br><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Save Location:</u> </strong><span>" + internet_SafariLSOther_List[ISLastSessionListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISLastSessionListLengthCounter = ISLastSessionListLengthCounter + 1

        #Recently Closed Tabs from Safari
        file.write("<h2>Recently Closed Tabs on Safari</h2>")
        ISRecentlyClosedListLengthCounter = 0
        ISRecentlyClosedListLength = len(internet_SafariRCURL_List)
        if ISRecentlyClosedListLength == 0:
            file.write("<strong>This User has no recently closed tabs on safari.</strong>")
        else:
            while ISRecentlyClosedListLengthCounter <= ISRecentlyClosedListLength - 1:
                file.write("<strong><u>Tab Title & URL:</u> </strong><span>" + internet_SafariRCName_List[ISRecentlyClosedListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" + internet_SafariRCURL_List[ISRecentlyClosedListLengthCounter] + "</span><br>\n")
                ISRCstring = internet_SafariRCDate_List[ISRecentlyClosedListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISRCstring)
                if DateMatch:
                    ISRCdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISRCdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRCstring)
                if TimeMatch:
                    ISRCtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISRCtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time:</u> </strong><span>" + str(ISRCdate) + "</span><span> </span><span>" + str(ISRCtime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariRCOther_List[ISRecentlyClosedListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISRecentlyClosedListLengthCounter = ISRecentlyClosedListLengthCounter + 1

        file.write("\t\t\t</div>")

    file.write("\t\t</div> \n")

        #End of Internet Searches Information ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Start of Network Information------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    file.write("\t\t<div id=\"Network_Info\" class=\"tabcontent\"> \n")
    NetworkInfoCheck = len(network_domainList) + len(network_forestList) + len(network_wifiNameList) + len(network_SSIDStringList) + len(network_interfaceList) + len(network_SSIDList) + len(network_AllHardwareList) + len(network_AllUUIDList) + len(inst_appName_List) + len(inst_totalNetUsage_List)
    if NetworkInfoCheck == 0:
        file.write("<p>This module was either not run or there is no output.</p>")
    else:
        file.write("\t\t\t<h2> Primary Network Interface Information </h2> \n" +
        #Domain Active Directory Table
                                    "\t\t\t<table style=\"width 100%; border-collapse: collapse\"> \n" +
                                        "\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Domain Active Directory Info </th> \n" +

                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Domain Name<span class=\"tooltiptext\">The name of the domain server that the system was connected to.</span></div> </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_domainList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Forest<span class=\"tooltiptext\">A Forest is a group of Active Directory domains, sharing the same schema.</span></div> </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_forestList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Trust Domain User<span class=\"tooltiptext\">The domain server name that the system uses to authenticate users.</span></div> </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_trustDomainList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Trust Account </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_trustAccList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Node Name<span class=\"tooltiptext\">The name of the tree that the system is connected to in the active directory.</span></div> </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_nodeNameList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Trust Kerberos Principal<span class=\"tooltiptext\">The name of the trust account and the realm/forest that it is connected to.</span></div> </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_trustKPrincipalList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Allow Multi-Domain? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_allowmultiDomainList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"><div class=\"tooltip\">Cache Last User Logon?<span class=\"tooltiptext\">Does the system store the last logon to the system?</span></div></th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_cacheLastUserLogonList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +

                                    "\t\t\t</table> \n")

        #WiFi Table
        file.write("\t\t\t<table style=\"width 100%; border-collapse: collapse\"> \n" +
                                        "\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> WiFi Interface Info </th> \n" +

                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> WiFi Name </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_wifiNameList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SSID String </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_SSIDStringList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Domain Security Type </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_SecurityTypeList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Date Last Connected to " + network_wifiNameList[0] + "</th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_lastConnectedList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Roaming Profile Type </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_roamingProfileTypeList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Channel Last Connected </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_lastConnectedChannelList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Prior Channel History </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_otherChannelHistoryList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Is Domain Closed? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_ClosedList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Is Domain a Passpoint? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_PasspointList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Is the Domain Disabled? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_DisabledList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Is this Domain a Personal Hotspot? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_personalHotspotList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Is this Domain Possibly Hidden? </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_possiblyHiddenNetworkList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                    "\t\t\t</table> \n")

        #Primary Network DHCP Table
        file.write("\t\t\t<table style=\"width 100%; border-collapse: collapse\"> \n" +
                                        "\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Primary Network DHCP Info </th> \n" +

                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Interface </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_interfaceList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> MAC Address </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_macAddressList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SSID </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_SSIDList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IP Address </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_IPAddressList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IP Lease Start Date </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_leaseStartDateList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IP Lease Length </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_leaseLengthList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Router IP Address </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_routerIPAddressList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Router Hardware Address </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_routerHardwareAddressList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> DHCP OpenBSD Name </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_BSDNameList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> DHCP Instance Hardware Connection </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_HardwareList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Network UUID </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_UUIDList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IPv4 Configuration Method </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_IPv4ConfigMethodList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IPv6 Configuration Method </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_IPv6ConfigMethodList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Network Connection Type </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_TypeList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> User Defined Name </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_UserDefinedNameList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> List of Proxies Exceptions </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_ProxiesExceptionsList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SMB NetBios Name </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_SMBNetBiosNameList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                        "\t\t\t\t<tr> \n" +
                                            "\t\t\t\t\t<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SMB Workgroup </th> \n")
        file.write("\t\t\t\t\t<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_SMBWorkgroupList[0] + "</td> \n")
        file.write("\t\t\t\t</tr> \n" +
                                    "\t\t\t</table> \n")

        #All other DHCP Interface Details Tables
        file.write("<h2> All Other DHCP Interface Details </h2>")
        AllDHCPCounterListLength = 0
        AllDHCPListLength = len(network_AllUUIDList)
        while AllDHCPCounterListLength <= AllDHCPListLength - 1:
            file.write("<table style=\"width 100%; border-collapse: collapse\"> \n")
            file.write("<th style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> DHCP Details for Interface Named " + network_AllUserDefinedNameList[AllDHCPCounterListLength] + "</th> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> DHCP Hardware for Connection </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllHardwareList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Network UUID </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllUUIDList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IPv4 Configuration Method </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllIPv4ConfigMethodList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> IPv6 Configuration Method </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllIPv6ConfigMethodList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Network Connection Type </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllTypeList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> User Defined Name </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllUserDefinedNameList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> Proxy Exceptions </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllProxiesExceptionsList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SMB NetBios Name </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllSMBNetBiosNameList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("<tr> \n")
            file.write("<th style =\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\"> SMB Workgroup </th> \n")
            file.write("<td style=\"border: 1px solid black; background-color:white; text-align: left; padding: 8px\">" + network_AllSMBWorkgroupList[AllDHCPCounterListLength] + "</td> \n")
            file.write("</tr> \n")
            file.write("</table> \n")
            AllDHCPCounterListLength = AllDHCPCounterListLength + 1

        #Network Usage for Installed Apps
        file.write("<h2> Network Usage Statistics for Specific Applications </h2>")
        NetworkUsageForSpecificAppsCounter = 0
        NetworkUsageForSpecificAppsListLength = len(inst_appName_List)
        while NetworkUsageForSpecificAppsCounter <= NetworkUsageForSpecificAppsListLength - 1:
            file.write("<strong>The Application </strong><span>" + str(inst_appName_List[NetworkUsageForSpecificAppsCounter]) + "</span><strong> used a total of </strong><span>" + str(inst_totalNetUsage_List[NetworkUsageForSpecificAppsCounter]) + " bytes</span><br>\n")
            IntAppsFirstSeenstring = inst_fSD_List[NetworkUsageForSpecificAppsCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", IntAppsFirstSeenstring)
            if DateMatch:
                IntAppsFirstSeendate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                IntAppsFirstSeendate = "No Date Available"
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", IntAppsFirstSeenstring)
            if TimeMatch:
                IntAppsFirstSeentime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                IntAppsFirstSeentime = "No Time Available"
            file.write("<strong class=\"indent\">First Seen on </strong><span>" + str(IntAppsFirstSeendate) + "</span><span> </span><span>" + str(IntAppsFirstSeentime) + "</span><br>\n")
            IntAppsLastSeenstring = inst_fSD_List[NetworkUsageForSpecificAppsCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", IntAppsLastSeenstring)
            if DateMatch:
                IntAppsLastSeendate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                IntAppsLastSeendate = "No Date Available"
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", IntAppsLastSeenstring)
            if TimeMatch:
                IntAppsLastSeentime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                IntAppsLastSeentime = "No Time Available"
            file.write("<strong class=\"indent\">Last Seen on </strong><span>" + str(IntAppsLastSeendate) + "</span><span> </span><span>" + str(IntAppsLastSeentime) + "</span><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wifiIn_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: green\"> <u>into</u> </span>the system over a<span style=\"color: blue\"> <u>WiFi</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wifiOut_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: red\"> <u>out</u> </span>of the system over a<span style=\"color: blue\"> <u>WiFi</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wiredIn_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: green\"> <u>into</u> </span>the system over a<span style=\"color: purple\"> <u>Wired</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wiredOut_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: red\"> <u>out</u> </span>of the system over a<span style=\"color: purple\"> <u>Wired</u> </span>connection from this application.</strong><br><br>\n")
            file.write("<hr><br>\n")
            NetworkUsageForSpecificAppsCounter = NetworkUsageForSpecificAppsCounter + 1

        file.write("\t\t</div> \n")

        #End of Network Information-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #Start of User Info Tab-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    file.write("\t\t<div id=\"User_Information\" class=\"tabcontent\"> \n")

    UserInfoCheck = len(inst_recentIURL_List) + len(user_riNamevol_List) + len(user_riURLplace_List) + len(user_riURLvol_List) + len(user_idn_List) + len(user_ifn_List) + len(user_idn2_List) + len(user_ifn2_List) + len(user_bashSSList)
    if UserInfoCheck == 0:
        file.write("<p>This module was either not run or there is no output.</p>")
    else:
        file.write("\t\t\t<button class=\"accordion\">User's Recent Interactions</button> \n" +
        "\t\t\t<div class=\"panel\"> \n")

        #Recent Used Apps
        file.write("<h2>Recently Used Applications</h2>")
        RecentUsedAppsCounter = 0
        RecentUsedAppsListLength = len(inst_recentIName_List)
        if RecentUsedAppsListLength == 0:
            file.write("<p>This User has no recently used applications.</p>")
        else:
            while RecentUsedAppsCounter <= RecentUsedAppsListLength - 1:
                file.write("<span>" + inst_recentIName_List[RecentUsedAppsCounter] + "</span><strong> has recently been used from the location </strong><span>" + inst_recentIURL_List[RecentUsedAppsCounter] + "</span><br><br><hr><br>\n")
                RecentUsedAppsCounter = RecentUsedAppsCounter + 1

        #Recently interacted Volumes
        file.write("<h2>Volumes that have been recently interacted with</h2>")
        RecentlyInteractedVolumesCounter = 0
        RecentlyInteractedVolumesListLength = len(user_riInfovol_List)
        if RecentlyInteractedVolumesListLength == 0:
            file.write("<p>This User has not recently interacted with any volumes on the system.</p>")
        else:
            while RecentlyInteractedVolumesCounter <= RecentlyInteractedVolumesListLength - 1:
                DateAndTimeListRecentIntVolume = user_riInfovol_List[RecentlyInteractedVolumesCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", DateAndTimeListRecentIntVolume)
                if DateMatch:
                    RecentIntVolDate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    RecentIntVolDate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", DateAndTimeListRecentIntVolume)
                if TimeMatch:
                    RecentIntVolTime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    RecentIntVolTime = "No Time Available"
                file.write("<strong>The volume named </strong><span>" + user_riNamevol_List[RecentlyInteractedVolumesCounter] + "</span><strong> was interacted with from the location </strong><span> " + user_riURLvol_List[RecentlyInteractedVolumesCounter] + "</span><strong> which was created on </strong><span>" + str(RecentIntVolDate) + "</span><span> </span><span>" + str(RecentIntVolTime) + "</span><br><br><hr><br>\n")
                RecentlyInteractedVolumesCounter = RecentlyInteractedVolumesCounter + 1

        #Recently visisted Places
        file.write("<h2>Recently Visited Places on System</h2>")
        RecentlyVisitedPlacesCounter = 0
        RecentlyVisitedPlacesListLength = len(user_riNameplace_List)
        if RecentlyVisitedPlacesListLength == 0:
            file.write("<p>This User has not recently visited a notable place on this system.</p>")
        else:
            while RecentlyVisitedPlacesCounter <= RecentlyVisitedPlacesListLength - 1:
                file.write("<strong>The User visited </strong><span>" + user_riNameplace_List[RecentlyVisitedPlacesCounter] + "</span><strong> from the location </strong><span>" + user_riURLplace_List[RecentlyVisitedPlacesCounter] + "</span><br><br><hr><br>\n")
                RecentlyVisitedPlacesCounter = RecentlyVisitedPlacesCounter + 1

        file.write("\t\t\t</div>" +

        "\t\t\t<button class=\"accordion\">User's Executables</button> \n" +
        "\t\t\t<div class=\"panel\"> \n")

        #Unix Executables
        file.write("<h2>Unix Executables</h2>")
        UnixExecListCounter = 0
        UnixExecListLength = len(user_idn_List)
        if UnixExecListLength == 0:
            file.write("<p>This User has no Unix Executables.</p>")
        else:
            while UnixExecListCounter <= UnixExecListLength - 1:
                file.write("<strong><u>Executable Name:</u> </strong><span>" + user_idn_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item File Name:</u> </strong><span>" + user_ifn_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item Kind:</u> </strong><span>" + user_ik_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Physical Size:</u> </strong><span>" + user_ps_List[UnixExecListCounter] + " bytes</span><br>\n")
                file.write("<strong class=\"indent\"><u>Date it was added to the system:</u> </strong><span>" + user_ida_List[UnixExecListCounter] + "</span><br>\n")
                if user_iwf_List[UnixExecListCounter] == "":
                    file.write("<strong class=\"indent\"><u>Where it came from</u> </strong><span>Not Available</span><br><br><hr><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>" + user_iwf_List[UnixExecListCounter] + "</span><br><br><hr><br>\n")
                UnixExecListCounter = UnixExecListCounter + 1

        #Windows Executables
        file.write("<h2>Windows Executables</h2>")
        WindowsExecListCounter = 0
        WindowsExecListLength = len(user_idn2_List)
        if WindowsExecListLength == 0:
            file.write("<p>This User has no Windows Executables.</p>")
        else:
            while WindowsExecListCounter <= WindowsExecListLength - 1:
                file.write("<strong><u>Executable Name:</u> </strong><span>" + user_idn2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item File Name:</u> </strong><span>" + user_ifn2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item Kind:</u> </strong><span>" + user_ik2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Physical Size:</u> </strong><span>" + user_ps2_List[WindowsExecListCounter] + " bytes</span><br>\n")
                file.write("<strong class=\"indent\"><u>Date it was added to the system:</u> </strong><span>" + user_ida2_List[WindowsExecListCounter] + "</span><br>\n")
                if user_iwf2_List[WindowsExecListCounter] == "":
                    file.write("<strong class=\"indent\"><u>Where it came from</u> </strong><span>Not Available</span><br><br><hr><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>" + user_iwf2_List[WindowsExecListCounter] + "</span><br><br><hr><br>\n")
                WindowsExecListCounter = WindowsExecListCounter + 1

        file.write("\t\t\t</div>")

        file.write("\t\t\t<button class=\"accordion\">User's Bash Sessions</button> \n" +
        "\t\t\t<div class=\"panel\"> \n")
        file.write("<h2>Bash Sessions</h2>")
        #Bash Sessions
        SessionCounter = 1
        BashSessionListCounter = 0
        BashSessionListLength = len(user_bashSSList)
        if BashSessionListLength == 0:
            file.write("<p>This User has no Bash Sessions.</p>")
        else:
            while BashSessionListCounter <= BashSessionListLength - 1:
                if user_bashSCList[BashSessionListCounter] == "":
                    file.write("")
                else:
                    file.write("<strong>Session Number " + str(SessionCounter) + "</strong><br>\n")
                    file.write("<strong><u>Session Start Time:</u> </strong><span>" + user_bashSSList[BashSessionListCounter] + "</span><br> \n")
                    file.write("<strong><u>Session End Time:</u> </strong><span>" + user_bashSEList[BashSessionListCounter] + "</span><br> \n")
                    file.write("<strong><div class=\"tooltip\"><u>Bash Commands:</u><span class=\"tooltiptext\">Bash commands are listed in order that they were ran and are seperated by a semicolon.</span></div> </strong><span>" + user_bashSCList[BashSessionListCounter] + "</span><br><br><hr><br> \n")
                BashSessionListCounter = BashSessionListCounter + 1
                SessionCounter = SessionCounter + 1

        file.write("\t\t\t</div>")

        file.write("\t\t\t<button class=\"accordion\">Safari Info for User</button> \n" +
        "\t\t\t<div class=\"panel\"> \n")
        # Last Launch Date for Safari
        file.write("<h2>Last Launched Date and Time</h2>")
        ISLLstring = internet_SafariOISLTDate_List[0]
        DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISLLstring)
        if DateMatch:
            ISLLdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
        else:
            ISLLdate = "No Date Available"
        TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISLLstring)
        if TimeMatch:
            ISLLtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
        else:
            ISLLtime = "No Time Available"
        file.write("<strong>The user specified in the Overview last launched safari on </strong><span>" + str(
            ISLLdate) + "</span><strong> at </strong><span>" + str(ISLLtime) + "</span><br>\n")

        # Safari Bookmarks output tab
        file.write("<h2>Safari Bookmarks</h2>")
        ISBoomarkListLengthCounter = 0
        ISBookmarkListLength = len(internet_SafariOIBURL_List)
        if ISBookmarkListLength == 0:
            file.write("<strong>This User has no bookmarks on Safari.</strong>")
        else:
            while ISBoomarkListLengthCounter <= ISBookmarkListLength - 1:
                file.write("<strong><u>Bookmark Name:</u> </strong><span>" + internet_SafariOIBName_List[
                    ISBoomarkListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\">Bookmark URL: </strong><span>" + internet_SafariOIBURL_List[
                    ISBoomarkListLengthCounter] + "</span><br>\n")
                ISBstring = internet_SafariOIBDate_List[ISBoomarkListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISBstring)
                if DateMatch:
                    ISBdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISBdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISBstring)
                if TimeMatch:
                    ISBtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISBtime = "No Time Available"
                file.write("<strong class=\"indent\">This bookmark was created on </strong><span>" + str(
                    ISBdate) + "</span><strong> at <strong><span>" + ISBtime + "</span><br>\n")
                file.write("<hr><br>")
                ISBoomarkListLengthCounter = ISBoomarkListLengthCounter + 1
        file.write("\t\t\t</div>"
        
                "\t\t\t<button class=\"accordion\">User Specific Downloads from Safari</button> \n" +
                "\t\t\t<div class=\"panel\"> \n")
        # Downloads from Safari Output Tab
        file.write("<h2>Downloads from Safari</h2> \n")
        ISSafariDLListLengthCounter = 0
        ISSafariDLListLength = len(internet_SafariDLName_List)
        if ISSafariDLListLength == 0:
            file.write("<strong>This User has no downloads from safari.</strong>")
        else:
            while ISSafariDLListLengthCounter <= ISSafariDLListLength - 1:
                file.write("<strong><u>File & URL:</u> </strong><span>" + internet_SafariDLName_List[
                    ISSafariDLListLengthCounter] + "</span>\n <strong>was downloaded from this location</strong>\n<span style=\"color: blue\"> " +
                        internet_SafariDLURL_List[ISSafariDLListLengthCounter] + "</span> <br>\n")
                if internet_SafariDLDate_List[ISSafariDLListLengthCounter] == 'None':
                    file.write("<strong class=\"indent\"><u>Date Downloaded:</u> </strong> <span>No Date Specified</span><br>")
                else:
                    file.write("<strong class=\"indent\"><u>Date Downloaded:</u> </strong><span>" + internet_SafariDLDate_List[
                        ISSafariDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><div class=\"tooltip\"><u>Save Location:</u><span class=\"tooltiptext\">Location in which the file was saved to on the imaged system. This location is represented with a relative path.</span></div> </strong> \n<span>" + internet_SafariDLOther_List[
                    ISSafariDLListLengthCounter] + "</span> <br><br>")
                file.write("<hr><br>\n")
                ISSafariDLListLengthCounter = ISSafariDLListLengthCounter + 1

        # Quarantine Download Output Tab
        file.write("<h2>Downloads Passed Through Quarantine</h2> \n")
        ISQuarantineDLListLengthCounter = 0
        ISQuarantineDLListLength = len(internet_QuarantineOTitle_List)
        if ISQuarantineDLListLength == 0:
            file.write("<strong>This User has no downlaods that passed through quarantine.</strong>")
        else:
            while ISQuarantineDLListLengthCounter <= ISQuarantineDLListLength - 1:
                ISQDstring = internet_QuarantineTS_List[ISQuarantineDLListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISQDstring)
                if DateMatch:
                    ISQDdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISQDdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISQDstring)
                if TimeMatch:
                    ISQDtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISQDtime = "No Time Available"
                file.write("<strong><u>Browser & Date:</u> </strong><span>" + internet_QuarantineName_List[
                    ISQuarantineDLListLengthCounter] + "<span><strong> was used on </strong><span>" + str(
                    ISQDdate) + "</span><strong> at </strong><span>" + str(ISQDtime) + "</span><br> \n")
                file.write("<strong class=\"indent\"><u>Origin Title:</u> </strong><span>" + internet_QuarantineOTitle_List[
                    ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Origin URL:</u> </strong><span>" + internet_QuarantineOURL_List[
                    ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Data URL:</u> </strong><span style=\"color: blue\">" +
                        internet_QuarantineDURL_List[ISQuarantineDLListLengthCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Agent Bundle ID:</u> </strong><span>" + internet_QuarantineABID_List[
                    ISQuarantineDLListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISQuarantineDLListLengthCounter = ISQuarantineDLListLengthCounter + 1

        file.write("\t\t\t</div>" +

                "\t\t\t<button class=\"accordion\">Safari Site Visit Statistics for User</button> \n" +
                "\t\t\t<div class=\"panel\"> \n")

        # Frequently visited sites tab
        file.write("<h2>Frequently Visited Sites on Safari</h2> \n")
        ISFrequentlyVisistedListLengthCounter = 0
        ISFrequentlyVisistedListLength = len(internet_SafariOIFVURL_List)
        if ISFrequentlyVisistedListLength == 0:
            file.write("<strong>This User has no frequently visited sites on Safari.</strong>")
        else:
            while ISFrequentlyVisistedListLengthCounter <= ISFrequentlyVisistedListLength - 1:
                file.write("<strong><u>Site & URL:</u> </strong><span>" + internet_SafariOIFVName_List[
                    ISFrequentlyVisistedListLengthCounter] + "</span><Strong> located at </strong><span style=\"color: blue\">" +
                        internet_SafariOIFVURL_List[ISFrequentlyVisistedListLengthCounter] + "</span><br>\n")
                file.write(
                    "<strong class=\"indent\"><u>Date:</u> </strong><span>" + internet_SafariOIFVDate_List + "</span><br>\n")
                file.write(
                    "<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariOIFVOther_List + "</span><br>\n")
                file.write("<hr><br>\n")
                ISFrequentlyVisistedListLengthCounter = ISFrequentlyVisistedListLengthCounter + 1

        # Top visited Sites on Safari
        file.write("<h2>Top Visited Sites on Safari</h2> \n")
        ISTopVisitedSitesListLengthCounter = 0
        ISTopVisitedSitesListLength = len(internet_SafariOITSURL_List)
        if ISTopVisitedSitesListLength == 0:
            file.write("<strong>This User has no top visited sites on Safari.</strong>")
        else:
            while ISTopVisitedSitesListLengthCounter <= ISTopVisitedSitesListLength - 1:
                if internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] == 'http://www.apple.com/startpage/':
                    file.write(
                        "<strong><u>Site Title & URL:</u> </strong><span>Apple </span><strong> at the URL</strong><span style=\"color: blue\"> " +
                        internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] + "</span><br>\n")
                else:
                    file.write("<strong><u>Site Title & URL:</u> </strong><span>" + internet_SafariOITSName_List[
                        ISTopVisitedSitesListLengthCounter] + "</span><strong> at the URL </strong><span style=\"color: blue\">" +
                            internet_SafariOITSURL_List[ISTopVisitedSitesListLengthCounter] + "</span><br>\n")
                ISTVstring = internet_SafariOITSDate_List[ISTopVisitedSitesListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISTVstring)
                if DateMatch:
                    ISTVdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISTVdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISTVstring)
                if TimeMatch:
                    ISTVtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISTVtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date:</u> </strong><span>" + str(
                    ISTVdate) + "</span><span> </span><span>" + str(ISTVtime) + "<br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariOITSOther_List[
                    ISTopVisitedSitesListLengthCounter] + "<br><br>\n")
                file.write("<hr><br>\n")
                ISTopVisitedSitesListLengthCounter = ISTopVisitedSitesListLengthCounter + 1
        file.write("\t\t\t</div>" +

                "\t\t\t<button class=\"accordion\">Internet Searches by User</button> \n" +
                "\t\t\t<div class=\"panel\"> \n")

        # Recent Searches tab content
        file.write("<h2>Recent Searches on Safari</h2> \n")
        ISRecentSearchesListLengthCounter = 0
        ISRecentSearchesListLength = len(internet_SafariOIRSName_List)
        if ISRecentSearchesListLength == 0:
            file.write("<strong>This User has no recent searches on safari.</strong>")
        else:
            while ISRecentSearchesListLengthCounter <= ISRecentSearchesListLength - 1:
                file.write("<strong><u>Search Term:</u> </strong><span>" + internet_SafariOIRSName_List[
                    ISRecentSearchesListLengthCounter] + "<span><br>\n ")
                ISRSstring = internet_SafariOIRSDate_List[ISRecentSearchesListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISRSstring)
                if DateMatch:
                    ISRSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISRSdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRSstring)
                if TimeMatch:
                    ISRStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISRStime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of Search:</u> </strong><span>" + str(
                    ISRSdate) + "</span><span> </span><span>" + str(ISRStime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Type of Search:</u> </strong><span>" + internet_SafariOIRSType_List[
                    ISRecentSearchesListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISRecentSearchesListLengthCounter = ISRecentSearchesListLengthCounter + 1

        # Search History tab content
        file.write("<h2>Safari Search History</h2>")
        ISSearchHistoryListLengthCounter = 0
        ISSearchHistoryListLength = len(internet_SafariHURL_List)
        if ISSearchHistoryListLength == 0:
            file.write("<strong>This User has no search history on safari.</strong>")
        else:
            while ISSearchHistoryListLengthCounter <= ISSearchHistoryListLength - 1:
                file.write("<strong><u>Search Query/Term & URL:</u> </strong><span>" + internet_SafariHName_List[
                    ISSearchHistoryListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" +
                        internet_SafariHURL_List[ISSearchHistoryListLengthCounter] + "</span><br>")
                ISHstring = internet_SafariHDate_List[ISSearchHistoryListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISHstring)
                if DateMatch:
                    ISHdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISHdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRSstring)
                if TimeMatch:
                    ISHtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISHtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of the Query/Search:</u> </strong><span>" + str(
                    ISHdate) + "</span><span> </span><span>" + str(ISHtime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariHOther_List[
                    ISSearchHistoryListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISSearchHistoryListLengthCounter = ISSearchHistoryListLengthCounter + 1
        file.write("\t\t\t</div>" +

                "\t\t\t<button class=\"accordion\">Previous Safari Session Information for User</button> \n" +
                "\t\t\t<div class=\"panel\"> \n")

        # Searches from last Session
        file.write("<h2>Searches Queries/Terms that were Auto-launched/Saved from Last Safari Session</h2>")
        ISLastSessionListLengthCounter = 0
        ISLastSessionListLength = len(internet_SafariLSURL_List)
        if ISLastSessionListLength == 0:
            file.write("<strong>This User has no searches from their last session on safari.</strong>")
        else:
            while ISLastSessionListLengthCounter <= ISLastSessionListLength - 1:
                file.write("<strong><u>Search Query/Term & URL:</u> </strong><span>" + internet_SafariLSName_List[
                    ISLastSessionListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" +
                        internet_SafariLSURL_List[ISLastSessionListLengthCounter] + "</span><br>\n")
                ISLSstring = internet_SafariLSDate_List[ISLastSessionListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISLSstring)
                if DateMatch:
                    ISLSdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISLSdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISLSstring)
                if TimeMatch:
                    ISLStime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISLStime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time of the Query/Search:</u> </strong><span>" + str(
                    ISLSdate) + "</span><span> </span><span>" + str(ISLStime) + "</span><br>\n")
                if internet_SafariLSOther_List[ISLastSessionListLengthCounter] == '':
                    file.write(
                        "<strong class=\"indent\"><u>Save Location:</u> </strong><span>No Save Location Found</span><br><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Save Location:</u> </strong><span>" + internet_SafariLSOther_List[
                        ISLastSessionListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISLastSessionListLengthCounter = ISLastSessionListLengthCounter + 1

        # Recently Closed Tabs from Safari
        file.write("<h2>Recently Closed Tabs on Safari</h2>")
        ISRecentlyClosedListLengthCounter = 0
        ISRecentlyClosedListLength = len(internet_SafariRCURL_List)
        if ISRecentlyClosedListLength == 0:
            file.write("<strong>This User has no recently closed tabs on safari.</strong>")
        else:
            while ISRecentlyClosedListLengthCounter <= ISRecentlyClosedListLength - 1:
                file.write("<strong><u>Tab Title & URL:</u> </strong><span>" + internet_SafariRCName_List[
                    ISRecentlyClosedListLengthCounter] + "</span><strong> from the URL </strong><span style=\"color: blue\">" +
                        internet_SafariRCURL_List[ISRecentlyClosedListLengthCounter] + "</span><br>\n")
                ISRCstring = internet_SafariRCDate_List[ISRecentlyClosedListLengthCounter]
                DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", ISRCstring)
                if DateMatch:
                    ISRCdate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
                else:
                    ISRCdate = "No Date Available"
                TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", ISRCstring)
                if TimeMatch:
                    ISRCtime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
                else:
                    ISRCtime = "No Time Available"
                file.write("<strong class=\"indent\"><u>Date & Time:</u> </strong><span>" + str(
                    ISRCdate) + "</span><span> </span><span>" + str(ISRCtime) + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Other Info:</u> </strong><span>" + internet_SafariRCOther_List[
                    ISRecentlyClosedListLengthCounter] + "</span><br><br>\n")
                file.write("<hr><br>\n")
                ISRecentlyClosedListLengthCounter = ISRecentlyClosedListLengthCounter + 1

        file.write("\t\t\t</div>" +
                "\t\t</div> \n")

        #End of USer Info Tab ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    #STart of Installed Apps--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    file.write("\t\t<div id=\"Installed_Apps\" class=\"tabcontent\"> \n")

    InstalledAppsCheck = len(inst_processName1List) + len(inst_processName2List) + len(inst_processName3List) + len(inst_appName_List) + len(inst_fSD_List) + len(inst_SNoT_List) + len(inst_sURL_List) + len(inst_idn_List) + len(inst_idn2_List)
    if InstalledAppsCheck == 0:
        file.write("<p>This module was either not run or there is no output.</p>")
    else:
        file.write("\t\t\t<button class=\"accordion\">Non-User Specific Information</button> \n" +
                "\t\t\t<div class=\"panel\"> \n")

        #macOS Updates Info/cards
        macUpdatesCounter = 0
        macUpdatesListLength = len(inst_processName1List)
        file.write("<h2>macOS Update Instances</h2>")
        if macUpdatesListLength == 0:
            file.write("<p>There are no recent macOS update instances for this system.")
        else:
            # macOSUpdateListsZipped = zip(inst_processName1List, inst_date1List)
            # dictOfmacOSUpdateLists = dict(macOSUpdateListsZipped)
            # for key, value in sorted(dictOfmacOSUpdateLists.items(), key=lambda x: x[1]):
            #     file.write("<div class=\"card\"> \n")
            #     file.write("<div class=\"card-container\"> \n")
            #     file.write("<h4><b>" + "{}".format(key) + "</b></h4><hr> \n")
            #     file.write("<p>" + "{}".format(value) + "</p> \n")
            #     file.write("</div>\n")
            #     file.write("</div>\n")
            while macUpdatesCounter <= macUpdatesListLength - 1:
                file.write("<div class=\"card\"> \n")
                file.write("<div class=\"card-container\"> \n")
                file.write("<h4><b>" + inst_processName1List[macUpdatesCounter] + "</b></h4><hr> \n")
                file.write("<p>" + inst_date1List[macUpdatesCounter] + "</p> \n")
                file.write("</div>\n")
                file.write("</div>\n")
                macUpdatesCounter = macUpdatesCounter + 1

        #Software Updates Info/cards
        softwareUpdatesCounter = 0
        softwareUpdatesListLength = len(inst_processName2List)
        file.write("<h2>Software Update Instances</h2>")
        if softwareUpdatesListLength == 0:
            file.write("<p>There are no recent software update instances on this system.")
        else:
            # macOSUpdateListsZipped = zip(inst_processName2List, inst_date2List)
            # dictOfmacOSUpdateLists = dict(macOSUpdateListsZipped)
            # for key, value in sorted(dictOfmacOSUpdateLists.items(), key=lambda x: x[1]):
            #     file.write("<div class=\"card\"> \n")
            #     file.write("<div class=\"card-container\"> \n")
            #     file.write("<h4><b>" + "{}".format(key) + "</b></h4><hr> \n")
            #     file.write("<p>" + "{}".format(value) + "</p> \n")
            #     file.write("</div>\n")
            #     file.write("</div>\n")
            while softwareUpdatesCounter <= softwareUpdatesListLength - 1:
                file.write("<div class=\"card\"> \n")
                file.write("<div class=\"card-container\"> \n")
                file.write("<h4><b>" + inst_processName2List[softwareUpdatesCounter] + "</b></h4><hr> \n")
                file.write("<p>" + inst_date2List[softwareUpdatesCounter] + "</p> \n")
                file.write("</div>\n")
                file.write("</div>\n")
                softwareUpdatesCounter = softwareUpdatesCounter + 1

        #Application Installers Info/cards
        installersCounter = 0
        installersListLength = len(inst_processName3List)
        file.write("<h2>Ran Application Installer Instances</h2>")
        if installersListLength == 0:
            file.write("<p>There are no recent application installers ran on this system.")
        else:
            while installersCounter <= installersListLength - 1:
                file.write("<div class=\"card\"> \n")
                file.write("<div class=\"card-container\"> \n")
                file.write("<h4><b>" + inst_processName3List[installersCounter] + "</b></h4><hr> \n")
                file.write("<p>" + inst_date3List[installersCounter] + "</p> \n")
                file.write("</div>\n")
                file.write("</div>\n")
                installersCounter = installersCounter + 1

        #Network Usage for Installed Apps
        file.write("<h2> Network Usage Statistics for Installed Applications </h2>")
        NetworkUsageForSpecificAppsCounter = 0
        NetworkUsageForSpecificAppsListLength = len(inst_appName_List)
        while NetworkUsageForSpecificAppsCounter <= NetworkUsageForSpecificAppsListLength - 1:
            file.write("<strong>The Application </strong><span>" + str(inst_appName_List[NetworkUsageForSpecificAppsCounter]) + "</span><strong> used a total of </strong><span>" + str(inst_totalNetUsage_List[NetworkUsageForSpecificAppsCounter]) + " bytes</span><br>\n")
            IntAppsFirstSeenstring = inst_fSD_List[NetworkUsageForSpecificAppsCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", IntAppsFirstSeenstring)
            if DateMatch:
                IntAppsFirstSeendate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                IntAppsFirstSeendate = "No Date Available"
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", IntAppsFirstSeenstring)
            if TimeMatch:
                IntAppsFirstSeentime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                IntAppsFirstSeentime = "No Time Available"
            file.write("<strong class=\"indent\">First Seen on </strong><span>" + str(IntAppsFirstSeendate) + "</span><span> </span><span>" + str(IntAppsFirstSeentime) + "</span><br>\n")
            IntAppsLastSeenstring = inst_fSD_List[NetworkUsageForSpecificAppsCounter]
            DateMatch = re.search(r"\d{4}\-\d{2}\-\d{2}", IntAppsLastSeenstring)
            if DateMatch:
                IntAppsLastSeendate = datetime.datetime.strptime(DateMatch.group(), '%Y-%m-%d').date()
            else:
                IntAppsLastSeendate = "No Date Available"
            TimeMatch = re.search(r"\d{2}\:\d{2}\:\d{2}", IntAppsLastSeenstring)
            if TimeMatch:
                IntAppsLastSeentime = datetime.datetime.strptime(TimeMatch.group(), '%H:%M:%S').time()
            else:
                IntAppsLastSeentime = "No Time Available"
            file.write("<strong class=\"indent\">Last Seen on </strong><span>" + str(IntAppsLastSeendate) + "</span><span> </span><span>" + str(IntAppsLastSeentime) + "</span><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wifiIn_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: green\"> <u>into</u> </span>the system over a<span style=\"color: blue\"> <u>WiFi</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wifiOut_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: red\"> <u>out</u> </span>of the system over a<span style=\"color: blue\"> <u>WiFi</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wiredIn_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: green\"> <u>into</u> </span>the system over a<span style=\"color: purple\"> <u>Wired</u> </span>connection from this application.</strong><br>\n")
            file.write("<strong class=\"indent\">There are </strong><span>" + inst_wiredOut_List[NetworkUsageForSpecificAppsCounter] + " </span><strong>bytes going<span style=\"color: red\"> <u>out</u> </span>of the system over a<span style=\"color: purple\"> <u>Wired</u> </span>connection from this application.</strong><br><br>\n")
            file.write("<hr><br>\n")
            NetworkUsageForSpecificAppsCounter = NetworkUsageForSpecificAppsCounter + 1

        file.write("\t\t</div> \n")

        #Tab for User Specific Information for Installed Apps--------------------------------------------------------------------------------------------------

        file.write("\t\t\t<button class=\"accordion\">User Specific Information</button> \n \t\t\t<div class=\"panel\"> \n")

        #Downloads from safari
        file.write("<h2>Files Downloaded from Safari</h2>")
        InstAppsDownloadsCounter = 0
        InstAppsDownloadsListLength = len(inst_sURL_List)
        if InstAppsDownloadsListLength == 0:
            file.write("<p>This User has no downloads from safari.</p>")
        else:
            while InstAppsDownloadsCounter <= InstAppsDownloadsListLength - 1:
                file.write("<strong>The file </strong><span>" + inst_SNoT_List[InstAppsDownloadsCounter] + " </span><strong>was downlaoded from the URL </strong><span style=\"color: blue\">" + inst_sURL_List[InstAppsDownloadsCounter] + "</span><br><br><hr><br> \n")
                InstAppsDownloadsCounter = InstAppsDownloadsCounter + 1

        #Unix Executables
        file.write("<h2>Unix Executables</h2>")
        UnixExecListCounter = 0
        UnixExecListLength = len(inst_idn_List)
        if UnixExecListLength == 0:
            file.write("<p>This User has no Unix Executables.</p>")
        else:
            while UnixExecListCounter <= UnixExecListLength - 1:
                file.write("<strong><u>Executable Name:</u> </strong><span>" + inst_idn_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item File Name:</u> </strong><span>" + inst_ifn_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item Kind:</u> </strong><span>" + inst_ik_List[UnixExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Physical Size:</u> </strong><span>" + inst_ps_List[UnixExecListCounter] + " bytes</span><br>\n")
                file.write("<strong class=\"indent\"><u>Date it was added to the system:</u> </strong><span>" +inst_ida_List[UnixExecListCounter] + "</span><br>\n")
                if user_iwf_List[UnixExecListCounter] == "":
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>Not Available</span><br><br><hr><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>" + inst_iwf_List[UnixExecListCounter] + "</span><br><br><hr><br>\n")
                UnixExecListCounter = UnixExecListCounter + 1

        #Windows Executables
        file.write("<h2>Windows Executables</h2>")
        WindowsExecListCounter = 0
        WindowsExecListLength = len(inst_idn2_List)
        if WindowsExecListLength == 0:
            file.write("<p>This User has no Windows Executables.</p>")
        else:
            while WindowsExecListCounter <= WindowsExecListLength - 1:
                file.write("<strong><u>Executable Name:</u> </strong><span>" + inst_idn2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item File Name:</u> </strong><span>" + inst_ifn2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Item Kind:</u> </strong><span>" + inst_ik2_List[WindowsExecListCounter] + "</span><br>\n")
                file.write("<strong class=\"indent\"><u>Physical Size:</u> </strong><span>" + inst_ps2_List[WindowsExecListCounter] + " bytes</span><br>\n")
                file.write("<strong class=\"indent\"><u>Date it was added to the system:</u> </strong><span>" + inst_ida2_List[WindowsExecListCounter] + "</span><br>\n")
                if user_iwf2_List[WindowsExecListCounter] == "":
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>Not Available</span><br><br><hr><br>\n")
                else:
                    file.write("<strong class=\"indent\"><u>Where it came from:</u> </strong><span>" + inst_iwf2_List[WindowsExecListCounter] + "</span><br><br><hr><br>\n")
                WindowsExecListCounter = WindowsExecListCounter + 1
        file.write("\t\t</div> \n")
        #file.write("<div id=\"piechart\"> </div>")
        file.write("\t\t</div> \n")

        #ENd of Installed Apps------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    file.write("\t\t<div id=\"PlaceHolder\" class=\"tabcontent\"> \n" +
                                "\t\t\t<h3> PlaceHolder </h3> \n" +
                                "\t\t\t<p> Placehoilder for now </p> \n" +
                                "\t\t\t<div id=\"piechart\" style=\"width: 90%;\"> </div> \n" +
                            "\t\t</div> \n")
    file.write("\t</div> \n" +
                    "</div> \n" +
                    #Script for Tabs
                    "<script> \n" +
                    "function openInfoTab(evt, tabName) { \n" +
                        "\tvar i, tabcontent, tablinks; \n" +
                        "\ttabcontent = document.getElementsByClassName(\"tabcontent\"); \n" +
                        "\tfor (i = 0; i < tabcontent.length; i++) { \n" +
                            "\t\ttabcontent[i].style.display = \"none\"; \n" +
                        "\t} \n" +
                        "\ttablinks = document.getElementsByClassName(\"tablinks\"); \n" +
                        "\tfor (i = 0; i < tablinks.length; i++) { \n" +
                            "\t\ttablinks[i].className = tablinks[i].className.replace(\" active\", \"\"); \n" +
                        "\t} \n" +
                        "\tdocument.getElementById(tabName).style.display = \"block\"; \n" +
                        "\tevt.currentTarget.className += \" active\"; \n" +
                    "} \n" +
                    "</script> \n" +
                    "<script type=\"text/javascript\" src=\"https://www.gstatic.com/charts/loader.js\"> </script>  \n\n" +  #CHANGE PATH LATER TO LOCAL PATH
                    "<script type=\"text/javascript\"> \n" +
                    #Load google charts
                    "google.charts.load('current', {'packages':['corechart']}); \n" +
                    "google.charts.setOnLoadCallback(drawChart); \n\n" +
                    #Draw the chart and set the chart values
                    "function drawChart() { \n" +
                        "\tvar data = google.visualization.arrayToDataTable([ \n")

    file.write("\t['Number of Applications', 'Bytes Used'], \n")
    # GraphCounter = 0
    # NumberOfPoints = len(inst_totalNetUsage_List)
    # print(len(inst_appName_List))
    # print(len(inst_totalNetUsage_List))
    # while GraphCounter <= NumberOfPoints - 1:
    #     file.write("\t['" + str(inst_appName_List[GraphCounter]) + "', " + str(inst_totalNetUsage_List[GraphCounter]) + "], \n")
    #     GraphCounter = GraphCounter + 1
    file.write("]); \n" +
                        #Optional; add a title and set the width and height of the chart 
                        "\tvar options = {'title':'Installed Applications', 'width':550, 'height':400}; \n\n" +
                        #Display the chart inside the < div > element with id="piechart" 
                        "\tvar chart = new google.visualization.PieChart(document.getElementById('piechart')); \n" +
                        "\tchart.draw(data, options); \n" +
                    "} \n" +
                    "</script> \n\n" +
                    #Script for Accordian Tabs
                    "<script> \n" +
                    "var acc = document.getElementsByClassName(\"accordion\"); \n" +
                    "var i; \n" +
                    "for (i = 0; i < acc.length; i++) { \n" +
                        "\tacc[i].addEventListener(\"click\", function() { \n" +
                            "\t\tthis.classList.toggle(\"AccordionActive\"); \n" +
                            "\t\tvar panel = this.nextElementSibling; \n" +
                            "\t\tif (panel.style.display === \"block\") { \n" +
                                "\t\t\tpanel.style.display = \"none\"; \n" +
                            "\t\t} else { \n" +
                                "\t\t\tpanel.style.display = \"block\"; \n" +
                            "\t\t} \n \t}); \n } \n" +
                    "</script> \n" +
                    #Footer
                    "<div class=footer> \n" +
                        "\t<p>The mac_Int Project</p> \n" +
                        "\t<a href=\"https://github.com/ydkhatri/mac_apt\"> Powered by mac_apt </a> \n" +
                    "</div> \n" +
                    "</body> \n" +
                    "</html> \n")

    if InstAppExists:
        os.remove("tempinstalledApps.json")
    if IntSearchExists:
        os.remove("tempinternetSearch.json")
    if MntVolExists:
        os.remove("tempmountedVolumes.json")
    if NetInfoExists:
        os.remove("tempnetworkInfo.json")
    if SysInfoExists:
        os.remove("tempsystemInfo.json")
    if UserInfoExists:
        os.remove("tempuserInfo.json")

htmlRun()
