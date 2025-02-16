from uuid import uuid4
import os

def e213d18250504ba584359829bd5deca1() -> str:
    _directory_: str = "."
    _uuid_: str = str(uuid4())
    while _uuid_[0].isdigit():
        _uuid_ = str(uuid4())
    _new_package_name_:str = "".join(_uuid_.split("-"))

    _package_path_:str = rf'{_directory_}/{_new_package_name_}' 
    if not os.path.exists(_package_path_):
        os.makedirs(_package_path_)
    
    _file_path_: str = f"{_package_path_}/__init__.py"

    with open(_file_path_, 'w') as _:
        pass

    _file_path_ = f"{_package_path_}/{_new_package_name_}.py"

    with open(_file_path_, 'w') as _:
        pass

    return _new_package_name_

if __name__ == "__main__":
    _create_new_package_: callable = e213d18250504ba584359829bd5deca1
    for _ in range(20):
        print(_create_new_package_())