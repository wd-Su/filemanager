import os
import argparse
curpath = os.getcwd()
#命令行工具

parser = argparse.ArgumentParser(description="文件管理器")

parser.add_argument("--mkfile",type=str,help="要制作文件的名称")
parser.add_argument("--location",type=str,help="要制作文件的路径")
parser.add_argument("--struct",type = int,help="打印当前目录结构")
parser.add_argument("--mkdir",type=str,help="要制作的文件夹名称")

args = parser.parse_args()


def chpath(aim_path):
    os.chdir(aim_path)

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
        print(f"已经在{curpath}创建了{path}文件夹")

    else:
        print("目录已存在")

def mkfile(filename):
    with open(filename,'w') as f:
        print(f"已经在目录{curpath}创建了{filename}文件")

value = 0
def list_files_and_dirs(directory):
    # 获取目录和文件列表
    items = os.listdir(directory)
    items = [item for item in items if not item.startswith('.')]
    # 区分目录和文件，并构建完整的路径列表
    files_and_dirs = []
    for item in items:
        full_path = os.path.join(directory, item)
        if os.path.isdir(full_path):
            files_and_dirs.append(item + '/')  

        else:
            files_and_dirs.append(item)

    return files_and_dirs,directory

def drawit(files_and_dirs,directory):
    for item in files_and_dirs:
        path = os.path.join(directory, item)
        if os.path.isdir(path):
            print(f'|---{item}')
            if os.listdir(path) is False:pass
            else:creatsub(path,1)

        else:
            print(f'|---{item}')

def creatsub(directory,value):
    new_value = value+1
    result,directory_path=list_files_and_dirs(directory)
    for item in result:
        path = os.path.join(directory_path, item)
        if os.path.isdir(path):
            print(4*value*' '+f'|---{item}')
            if os.listdir(path) is False:
                pass
            else:
                creatsub(path,new_value)

        else:
            print(4*value*' '+f'|---{item}')


def find_directory(start_path, target_name):
    # 遍历起始目录中的所有内容
    for item in os.listdir(start_path):
        # 构建当前项的完整路径
        item_path = os.path.join(start_path, item)

        # 检查当前项是否为目录
        if os.path.isdir(item_path):
            # 如果当前目录的名称与目标名称匹配，则返回其路径
            if item == target_name:
                return item_path
            # 否则，递归地调用find_directory函数，继续遍历当前目录的内容
            else:
                result = find_directory(item_path, target_name)
                # 如果找到了目标目录，则返回其路径
                if result is not None:
                    return result

    # 如果遍历完起始目录及其所有子目录后仍未找到目标目录，则返回None
    return None

if __name__ == '__main__':

    if args.struct ==1:
        directory_path = curpath
        result, directory_path = list_files_and_dirs(directory_path)
        drawit(result, directory_path)
    if args.location:
        location = args.location
        result1 = find_directory(curpath, location)
        if result1 is not None:
            if args.mkfile:
                mkfile(result1+"\\"+args.mkfile)
                print(f'已成功创建{args.mkfile}')
            if args.mkdir:
                mkdir(result1+"\\"+args.mkdir)
                print(f'已成功创建{args.mkdir}')

        else:
            print("无该文件夹")
    # chpath(aim_path)
    # mkdir(dirname)
    # mkfile(filename)
    # directory_path = 'C:\\Users\littl\Desktop\imgenhance'
    # result, directory_path = list_files_and_dirs(directory_path)
    # drawit(result, directory_path)