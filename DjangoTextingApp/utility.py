import os
DEFAULTCONFIG = ["NAME 		: \n",
                 "USERNAME 	: \n",
                 "PASSWORD	: \n",
                 "HOST		: \n",
                 "PORT		: \n",
                 "SECRET_KEY: \n"]


def read_config_file():
    file_path = 'outer_cfg.txt'

    if not os.path.isfile(file_path):
        print("ERROR: outer_cfg file is created, fill all fields and restart server.")
        f = open(file_path, "w+")

        for i in DEFAULTCONFIG:
            f.write(i)

        f.close()
        exit(-1)
    DB_name = ''
    user_name = ''
    Password = ''
    Host = ''
    Port = ''
    Secret_key = ''

    with open(file_path) as fp:
        for line in fp:
            if line.startswith("NAME"):
                DB_name = line.split(':')[1].strip()
            if line.startswith("USERNAME"):
                user_name = line.split(':')[1].strip()
            if line.startswith("PASSWORD"):
                Password = line.split(':')[1].strip()
            if line.startswith("HOST"):
                Host = line.split(':')[1].strip()
            if line.startswith("PORT"):
                Port = line.split(':')[1].strip()
            if line.startswith("SECRET_KEY"):
                Secret_key = line.split(':')[1].strip()
    return [DB_name, user_name, Password, Host, Port, Secret_key]