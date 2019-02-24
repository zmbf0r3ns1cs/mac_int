# Query Logic for Bash Sessions v0.1
# Justin Boncaldo (@boncaldoj), Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------
from mountedDevices import *
from variable_db import *

# The following is the parts removed from mountedDevices.py to be used here
    
    # elif counter == 5:
        # Define variables for Bash Commands

# x is defined for the list we're using, in the other y file
# imports counter
bashCounter = 0


for row in x:  # mount_volList in mountedDevices file
    L = 0
    # SQLite Search Start
    while L < p:

        if bashCounter == 0:
            print("Made it in counter 0")
            a = sc
            b = bs
        cursor.execute("SELECT {} FROM {} WHERE User = ? AND All_Commands LIKE ?".format(a, b), (
            userSearch, '%' + str(x[L]) + '%',))
        bashOutput = cursor.fetchall()
        e.clear()
        for i in bashOutput:
            e.append(str(i[0]))
        if counter == 0:




        pos = 0
        for n in bashOutput:
            string1 = str(d[pos])
            pos = pos + 1
            mount_bashList.append(string1)
            mount_bashListLength: int = len(mount_bashList)
        L = L + 1
        bashCounter = bashCounter + 1

print(bashCounter)
print(str(mount_bashList))




end = "yes"

m = 0
z = 0
k = 0


# Begin writing output
while m < (volLength):
    file.write("\t-Volume Name: " + str(mount_volList[z]) + "\n" + "\t\tVolume created on: " + str(
        mount_crList[z]) + "\n" + "\t\tVolume first seen on: " + str(
        mount_fsList[z]) + "\n" + "\t\tVolume last seen on: " + str(
        mount_lsList[z]) + "\n")






    # if L == (volLength - 1):
    #     L = 0
    #     counter = counter + 1
    # else:
    #     L = L + 1
    # if not mount_bashList:
    #     continue
    # else:
    #     file.write("\t\t" + str(mount_bashList + "\n"))
    m = m + 1
    z = z + 1
    # while k < mount_bashListLength:
    #     if not mount_bashList: 
    #         print("Skipping Bash")
    #         print(m)
    #         m = m + 1
    #         z = z + 1
    #         k = k + 1
    #     if mount_bashList:
    #         print("I MADE IT")
    #         file.write("\t\tBash Command: " + str(mount_bashList[z]) + "\n")
    #         m = m + 1
    #         z = z + 1
    #         k = k + 1
    