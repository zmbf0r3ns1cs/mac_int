# Query Logic for Bash Sessions v0.1
# Justin Boncaldo, Zachary Burnham (@zmbf0r3ns1cs) 2019
# ----------------------------------------------------------

# The following is the parts removed from mountedDevices.py to be used here
    
    elif counter == 5:
        # Define variables for Bash Commands
        if counter == 5:
            while L < volLength:
                a = sc
                b = bs
                # SQLite Search Start
                cursor.execute("SELECT {} FROM {} WHERE User = ? AND All_Commands LIKE ?".format(a, b),
                                (userSearch, '%' + str(mount_volList[L]) + '%',))
                bashOutput = cursor.fetchall()
                e.clear()
                for row in bashOutput:
                    e.append(str(row[0]))
                pos = 0
                for (row) in bashOutput:
                    string1 = str(e[pos])
                    pos = pos + 1
                    if counter == 5:
                        mount_bashList.append(string1)
                        mount_bashListLength: int = len(mount_bashList)
                        if L == (volLength - 1):
                            L = 0
                            counter = counter + 1
                        else:
                            L = L + 1
                    else:
                        L = (volLength + 1)
                
                #counter = counter + 1
                #f.append(str(row[0]))
            #mount_bashList.append(str(f))
            #L = L + 1
        end = "yes"

m = 0
z = 0
k = 0

# Bash value check
#if not mount_bashList:
    #mount_bashList = str("None")

# Begin writing output
while m < (volLength):
    file.write("\t-Volume Name: " + str(mount_volList[z]) + "\n" + "\t\tVolume created on: " + str(
        mount_crList[z]) + "\n" + "\t\tVolume first seen on: " + str(
        mount_fsList[z]) + "\n" + "\t\tVolume last seen on: " + str(
        mount_lsList[z]) + "\n")
    if not mount_bashList:
        continue
    else:
        file.write("\t\t" + str(mount_bashList + "\n"))
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
    