## filemanager的使用方法
### 基本参数
```python
parser.add_argument("--mkfile",type=str,help="要制作文件的名称")
parser.add_argument("--location",type=str,help="要制作文件的路径")
parser.add_argument("--struct",type = int,help="打印当前目录结构")
parser.add_argument("--mkdir",type=str,help="要制作的文件夹名称")
```
### 使用方法
1. 首先建立一个名为filemanager的文件夹
2. 在文件夹下创建`fl.py`
3. 使用命令行（前提是cd到filemaker的目录下）
4. 命令行使用方法如下
```shell
python fl.py --struct 1 #将struct设置为1以查看文件结构
python fl.py --location [文件目录名] #找到目标文件目录，与mkfile和mkdir结合使用
python fl.py --location  [文件目录名] --mkfile [文件名] --mkdir[要创建的目录名]
# 在文件目录名位置下，创建文件或文件目录(--makefile和--mkdir必须与--location连用)
```
### 应用实例
![alt text](image.png)
![alt text](<屏幕截图 2024-11-21 160309.png>)
转到了filetest(filemanager)目录下
![alt text](<屏幕截图 2024-11-21 160756.png>)
打印了文件结构
![alt text](<屏幕截图 2024-11-21 161206.png>)
在chap11目录下创建了创建了test1_1文件和chap11_1文件夹
![alt text](<屏幕截图 2024-11-21 161443.png>)
再打印一下文件结构。

