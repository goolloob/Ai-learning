import fitz # pdf转为图片P
from aip import AipOcr # 图片文字识别
import time # 程序运行时间间隔以避免出错
import docx # 将识别结果保存为docx文件
from docx.oxml.ns import qn # 设置docx文件的字体

""" 你的 APPID AK SK """
APP_ID = '31812718'
API_KEY = 'ezDW0V6Fr3SNCq14u8A39l4l'
SECRET_KEY = 'v4zOjCQ69HBn9CyGhG7fyD5ThP9eRdFU'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def pdf_image(pdfPath, imgPath, zoom_x=5, zoom_y=5, rotation_angle=0):
    # 获取pdf文件名称
    name = pdfPath.split("\\")[-1].split('.pdf')[0]
    # 打开PDF文件
    pdf = fitz.open(pdfPath)
    # 获取pdf页数
    num = pdf.pageCount
    # 逐页读取PDF
    for pg in range(0, num):
        page = pdf[pg]
        # 设置缩放和旋转系数
        trans = fitz.Matrix(zoom_x, zoom_y).preRotate(rotation_angle)
        pm = page.getPixmap(matrix=trans, alpha=False)
        # 开始写图像
        pm.writePNG(imgPath + name + "_" + str(pg) + ".png")
    pdf.close()
    return name, num


def ReadDetail_docx(imgPath, name, num):
    # 建立一个空doc文档
    doc = docx.Document()
    # 设置全局字体
    doc.styles["Normal"].font.name=u"宋体"
    doc.styles["Normal"]._element.rPr.rFonts.set(qn('w:eastAsia'), u'宋体')
    # 读取图片
    for n in range(0,num):
        i = open(imgPath+name+"_"+str(n)+".png",'rb')
        time.sleep(0.1)
        img = i.read()
        message = client.basicGeneral(img)
        content = message.get('words_result')
        # 将内容写入doc文档
        for i in range(len(content)):
            doc.add_paragraph(content[i].get('words'))
    # 保存doc文档
    doc.save(imgPath + name + '.docx')

def pdf_to_docx(pdfPath, imgPath, zoom_x=5, zoom_y=5, rotation_angle=0):
    print("正在将pdf文件转换为图片...")
        # 调用函数一将pdf转换为图片，并获得文件名和页数
    name_, num_ = pdf_image(pdfPath, imgPath, zoom_x, zoom_y, rotation_angle)
    print("转换成功！")
    print("正在读取图片内容...")
        # 调用函数二逐页读取图片并逐行保存在docx文件中
    ReadDetail_docx(imgPath, name_, num_)
    print("名为 {}.pdf 的pdf文件共有{}页,已成功转换为docx文件!".format(name_, num_))       
# pdf储存路径
# pdf_path = r"D:\data\Desktop\123.pdf"
# # 图片和生成的docx文件的储存路径
# img_path = r"D:\data\Desktop\123\\"
pdf_path = input('请输入PDF文件全路径:')
img_path = input('请输入存储路径:')
# 调用函数
pdf_to_docx(pdf_path, img_path)