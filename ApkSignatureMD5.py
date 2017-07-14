#!/usr//bin/env python
# -*- coding:UTF-8 -*-

import os
import string


def get_apk_signature_md5():
    keystore_file_path = raw_input('Please input keystore\'s file path: ').strip()
    keystore_alias = raw_input('Please input keystore\'s alias: ').strip()
    keystore_pwd = raw_input('Please input keystore\'s password: ').strip()

    command = 'keytool -list -keystore %s -storepass %s -alias %s -v' % (
        keystore_file_path, keystore_pwd, keystore_alias)
    r = os.popen(command)
    info = r.readlines()
    for line in info:
        line = line.strip('\r\n')
        if string.find(line, 'MD5:') != -1:
            return handle_line_text(line)
    return ''


def handle_line_text(text):
    text = string.replace(text, 'MD5:', '')
    text = string.replace(text, ':', '')
    text = string.lower(text)
    return text.strip()


if __name__ == '__main__':
    md5 = get_apk_signature_md5()
    print(md5)
