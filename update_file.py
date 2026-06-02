# Open server.conf file to update MAX_CONNECTION
def update_file(file_path, key, value):
    # Open file in read mode
    with open(file_path, "r") as file:
        lines = file.readlines()
    # Open file in write mode
    with open(file_path, "w") as file:
        for line in lines:
            if key in line:
                file.write(key + "=" + value + "\n")
            else:
                file.write(line)
update_file("server.conf", "MAX_CONNECTIONS", "1000")


