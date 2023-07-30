import os
def create_directory(path,name):
    try:
        new_directory_path = os.path.join(path, dir_name)
        os.mkdir(new_directory_path)

        # In case the above directory does not exist, make new directory using this:
        # os.makedirs(new_directory_path, exist_ok=True)
    except FileExistsError:
        print(name, "already exists")

path = os.path.join("Projects", "CollectInfoFromWebpage")
dir_name = "dimik_pub"
create_directory(path, dir_name)

def create_sub_directories(name):
    print("creating directory", name)
    try:
        # path = "Projects/CollectInfoFromWebpage/dimik_pub/"+name
        path = os.path.join("Projects", "CollectInfoFromWebpage", "dimik_pub", name)
        
        os.mkdir(path)
    except FileExistsError:
        print(name, "already exists")
