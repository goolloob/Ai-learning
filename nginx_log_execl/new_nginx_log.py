# import re
# from datetime import datetime
# import openpyxl
# from dateutil.parser import parse
# import time
# import os


# # file = 'D:\data\Desktop\Ai-learning\python_learning\lifpay.me.access.log'
# file = r'D:\data\Desktop\Ai-learning\python_learning\test.log'


# def re_data(data):
#     log_pattern = r'(.*?) - (-|.*) \[(.*?)\] "(.*?)" (.*?) (.*?) "(.*?|-)" "(.*?)" (.*?)$'
#     data_match = re.match(log_pattern, data)
#     return data_match


# def time_data(data):
#     data_match = re_data(data)
#     # 定义日期字符串的格式
#     date_format = "%d/%b/%Y:%H:%M:%S %z"
#     # 将日期字符串解析为datetime对象
#     datetime_obj = datetime.strptime(data_match.group(3), date_format)
#     # 将datetime对象按照指定格式进行格式化
#     time_date = datetime_obj.strftime("%Y-%m-%d %H:%M:%S %Z")
#     return time_date


# def excel_from_name(dict):
#     date_str = dict['日期']
#     datetime_obj = parse(date_str)
#     # 获取月份和年份，用于创建工作表名称
#     month = datetime_obj.strftime("%m")
#     year = datetime_obj.strftime("%Y")
#     return month, year

# def from_header(nginx_log_from, year, month):
#     # 创建execle表格头行数据标题
#     workbook_from = openpyxl.load_workbook('D:\data\Desktop\Ai-learning\data.xlsx')
#     ws_name = workbook_from.get_sheet_names()
    
#     if f'{year}-{month}' in ws_name:
#         name = f"{year}-{month}"
#         ws = workbook_from.get_sheet_by_name(name)
#         ws['A1'] = list(nginx_log_from.keys())[0]
#         ws['B1'] = list(nginx_log_from.keys())[1]
#         ws['C1'] = list(nginx_log_from.keys())[2]
#         ws['D1'] = list(nginx_log_from.keys())[3]
#         ws['E1'] = list(nginx_log_from.keys())[4]
#         ws['F1'] = list(nginx_log_from.keys())[5]
#         ws['G1'] = list(nginx_log_from.keys())[6]
#     else:
#         workbook_from.create_sheet(f'{year}-{month}')
#         name = f"{year}-{month}"
#         ws = workbook_from.get_sheet_by_name(name)
#         ws['A1'] = list(nginx_log_from.keys())[0]
#         ws['B1'] = list(nginx_log_from.keys())[1]
#         ws['C1'] = list(nginx_log_from.keys())[2]
#         ws['D1'] = list(nginx_log_from.keys())[3]
#         ws['E1'] = list(nginx_log_from.keys())[4]
#         ws['F1'] = list(nginx_log_from.keys())[5]
#         ws['G1'] = list(nginx_log_from.keys())[6]
#     workbook_from.save('data.xlsx')
   


# def from_write(nginx_log, year, month):
#     workbook_from = openpyxl.load_workbook('D:\data\Desktop\Ai-learning\data.xlsx')
#     # ws = workbook_from.active
#     print('写入数据中.....................')
#     name = f"{year}-{month}"
#     ws = workbook_from.get_sheet_by_name(name)
#     ws.append(list(nginx_log.values()))
#     workbook_from.save('data.xlsx')  # bug execl文件打开关闭次数太多浪费资源

# def from_master():
#     workbook = openpyxl.Workbook()
#     workbook.save('data.xlsx')



# with open(file,'r') as file:
#     with open(file=r'D:\data\Desktop\Ai-learning\python_learning\1.txt', mode='r+') as files :
#         a = files.read()
#     re_txt=r'(.*?):(.*?)$'
#     text = re.match(re_txt, a)
#     print(text.group(2))
#     file.seek(int(text.group(1)))
#     data = file.readline()
#     number = int(text.group(2))
#     if not os.path.exists(r'D:\data\Desktop\Ai-learning\data.xlsx'):
#         from_master()
#     while data:
#         # time.sleep(0.001)
#         data_match = re_data(data)
#         time_date = time_data(data)
#         nginx_log = dict()
#         nginx_log["IP"] = data_match.group(1)
#         nginx_log["日期"] = time_date
#         nginx_log["请求方法"] = data_match.group(4)
#         nginx_log["请求状态"] = data_match.group(5)
#         nginx_log["请求大小"] = data_match.group(6)
#         nginx_log["客户端信息"] = data_match.group(8)
#         nginx_log["行数"] = number
        
#         month, year = excel_from_name(nginx_log)
#         from_header(nginx_log, year, month)
#         time.sleep(0.1)
#         from_write(nginx_log, year, month)
       
#         number += 1
#         data = file.readline()
#     a = file.tell()+2  # 获取日志文件指针位置指针的
#     a = str(f'{a}:{number}')
#     # 下次直接从指针开始
#     with open(file=r'D:\data\Desktop\Ai-learning\python_learning\1.txt',mode='r+') as file:
#         file.write(str(a))



# # if __name__ ==:
#     # pass
