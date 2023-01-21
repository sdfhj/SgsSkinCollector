# SgsSkinCollector
三国杀十周年皮肤爬虫

## 使用说明
下载解压；打开命令行或PowerShell，cd到解压后的代码文件夹；使用python运行代码auto_dld.py，即可开始循环抓取所有皮肤。  
如果无法运行，则需要使用pip安装一些包，例如：os、time、requests、faker、shutil、openpyxl，根据报错信息安装即可。  
循环运行一次可能需要数个小时的时间，建议单独放到一个桌面里运行，眼不见心不烦。  

## 文件说明
0-dld_from_nothing_update.py：顾名思义，即从零开始下载，当然也可以不从零开始，下载程序的主体；  
6-extract_female_dragonbones_list_relative.py：根据目录结构提取女性动态皮肤（不会有人想看男性动态吧）相对路径列表，并根据类型保存为几个txt文件；  
auto_dld.py：循环执行以上两个程序，无限循环运行，更新皮肤；  
  
download/Example.xlsx：皮肤源文件下载链接的格式，一般不需要改动；  
download/sort.xlsx：武将编号及名称的对应关系，在看到download/sort文件夹中出现日期较新且名称为纯数字的新文件夹的时候，可以看看里面的皮肤对应哪个新出的武将，并在该xlsx文件内进行更新，后续下载会根据该xlsx文件的信息对文件夹进行重命名。  
