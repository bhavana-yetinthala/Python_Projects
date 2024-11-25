# Need to use server.conf file

def server_configuartion(folderpath,key,value):
    
    with open(folderpath,"r") as file:
        lines = file.readlines()

    with open(folderpath,"w") as file:
         for every_line in lines:
              if key in lines:
                file.write(key + "=" + value + "\n")
              else:
                every_line = every_line



server_configuartion(r"C:\Users\yetin\OneDrive\Desktop\Devops\Python\Server_confg_file.txt", "MAX_CONNECTIONS", "500")
