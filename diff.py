from filecmp import dircmp
import sys
import os
import md5

if len(sys.argv) < 3:
    print("Please provide folders to compare")
    sys.exit()

if (not os.path.exists(sys.argv[1])):
    print("Dir '",sys.argv[1],"' does not exists" )
    sys.exit()

if (not os.path.exists(sys.argv[2])):
    print("Dir '",sys.argv[1],"' does not exists" )
    sys.exit()

def Dir_Exists(dir):
    if (os.path.isdir(dir)):
        return 1;
    else:
        return -1;


def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "diff_file %s found in %s and %s" % (name, dcmp.left,dcmp.right)
    for name in dcmp.left_only:
        stat = Dir_Exists(dcmp.left+"/"+name)
        if stat == 1:
           print"%s : %s dir only found in %s" % (dcmp.left, name, dcmp.left,)
        else:
            print "%s : %s file only found in %s" % (dcmp.left, name, dcmp.left,)
    for name in dcmp.right_only:
        stat = Dir_Exists(dcmp.right+"/"+name)
        if stat == 1:
           print "%s : %s dir only found in %s"  % (dcmp.right, name,dcmp.right )
        else:
            print "%s : %s file only found in %s" % (dcmp.right, name,dcmp.right )
    #for name in dcmp.same_files:
     #   print "File %s is in both folders (%s and %s)"  % (name,dcmp.right,dcmp.right )
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)


dcmp = dircmp(sys.argv[1], sys.argv[2]) 

print_diff_files(dcmp)