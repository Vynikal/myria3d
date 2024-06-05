import os
import sys

if __name__ == '__main__':

    if len(sys.argv) > 2:
        print("Please enter the correct folder path parameter")
        print("Wrong number of parameters")
        sys.exit()
    else:
        if os.path.isdir(sys.argv[1]):
            print("Analysis in progress...")
            print(sys.argv[1])
            for file in os.listdir(sys.argv[1]):        
                if file.endswith(".txt"):
                    filepath = os.path.join(sys.argv[1], file)
                    if os.path.isfile(filepath):
                        truthpath = os.path.join(sys.argv[1]+'_Truth', file[:-7]+'CLS.txt')
                        mergepath = os.path.join(sys.argv[1]+'_Merge', file[:-7]+'Merge.txt')
                        paste = "paste -d',' {0} {1} > {2}".format(filepath,truthpath,mergepath)
                        os.system(paste)
                        command = "/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=CloudCompare org.cloudcompare.CloudCompare -SILENT -AUTO_SAVE OFF -O {0} -C_EXPORT_FMT LAS -RGB_CONVERT_TO_SF -RENAME_SF 0 'Intensity' -RENAME_SF 1 'ReturnNumber' -RENAME_SF 2 'Classification' -REMOVE_SF 3 -SAVE_CLOUDS".format(mergepath)
                        os.system(command)
                else:
                    continue
        else:
            print("Wrong number of parameters")
            sys.exit()
