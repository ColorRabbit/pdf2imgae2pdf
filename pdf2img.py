#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, tempfile
from time import process_time
from pdf2image import convert_from_path


# pdf转图片
def pdf_to_pic(filename, output_dir):
    print('[*][PDF转图片] : 开始.')
    print('[*][文件名是]：%s' % filename)
    print('[*][图片输出目录]：%s' % output_dir)
    begin_time = process_time()
    # images = convert_from_path(filename)
    # image = convert_from_bytes(open(filename, 'rb').read())
    with tempfile.TemporaryDirectory() as path:
        image_from_path = convert_from_path(filename, output_folder=path)
    # print(images)
    # print(image)
    base_name = FileTools().handle_filename(filename)
    for index, img in enumerate(image_from_path):
        path = '%s_%s.png' % (base_name, index)
        fullpath = os.path.join(output_dir, path)
        img.save(fullpath, 'JPEG', quality=100)
        print('[*][转换图片中]：%s' % fullpath)
    end_time = process_time()
    print('[*][PDF转图片] : 结束. 耗时 %f s ' % ((end_time - begin_time)))


class FileTools:
    def handle_filename(self, fullname, ness=''):
        filename = os.path.basename(fullname)
        if ness == 'ext':
            return os.path.splitext(filename)[-1][1:]
        else:
            return os.path.splitext(filename)[0]


# 第一个参数为文件名，第二个参数为文件夹
if __name__ == '__main__':
    filename = sys.argv[1]
    output_dir = sys.argv[2]
    pdf_to_pic(filename, output_dir)
