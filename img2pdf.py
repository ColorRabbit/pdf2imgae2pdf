#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys
from reportlab.platypus import SimpleDocTemplate, Image, PageBreak
from reportlab.lib.pagesizes import A4, landscape
from time import process_time
from PIL import Image as pilImage


def transfer_pdf_by_path(file_path, pdf_name, pdf_path=''):
    file_list = []

    result = os.listdir(file_path)
    result.sort()

    for i in result:
        file_list.append(os.path.join(file_path, i))
    create_pdf(os.path.join(pdf_path, str(pdf_name) + '.pdf'), file_list)


def transfer_pdf_by_files(file_list, pdf_name, pdf_path=''):
    create_pdf(os.path.join(pdf_path, str(pdf_name) + '.pdf'), file_list)


def create_pdf(pdf_path, file_list):
    __a4_w, __a4_h = landscape(A4)
    pdf_data = []

    print("[*][转换PDF] : 开始. [名称] > [%s]" % (pdf_path))
    begin_time = process_time()

    pdf_doc = SimpleDocTemplate(pdf_path, pagesize=A4, rightMargin=72, leftMargin=72, topMargin=72, bottomMargin=18)

    for page in file_list:
        img_w, img_h = ImageTools().get_image_size(page)

        if __a4_w / img_w < __a4_h / img_h:
            ratio = __a4_w / img_w
        else:
            ratio = __a4_h / img_h
        data = Image(page, img_w * ratio, img_h * ratio)
        pdf_data.append(data)
        pdf_data.append(PageBreak())

    try:
        pdf_doc.build(pdf_data)
        # print("已转换 >>>> " + bookName)
    except Exception as err:
        print("[*][转换PDF] : 错误. [名称] > [%s]" % (pdf_path))
        print("[*] Exception >>>> ", err)

    end_time = process_time()
    print("[*][转换PDF] : 结束. [名称] > [%s] , 耗时 %f s " % (pdf_path, (end_time - begin_time)))


class ImageTools:
    def get_image_size(self, imagePath):
        img = pilImage.open(imagePath)
        return img.size


# pic_path = '/usr/local/var/python/pic'
# pdf_name = 'test'
# pdf_path = '/usr/local/var/python/pdf'
# pic_list = ['/usr/local/var/python/pic/1.jpg', '/usr/local/var/python/pic/2.jpg',]


# 第一个参数为图片目录，第二个参数为pdf名称，第三个参数为pdf目录名称
if __name__ == '__main__':
    pic_path = sys.argv[1]
    pdf_name = sys.argv[2]
    pdf_path = sys.argv[3]
    transfer_pdf_by_path(pic_path, pdf_name, pdf_path)
