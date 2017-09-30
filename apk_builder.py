#!/usr//bin/env python
# -*- coding:UTF-8 -*-

import json
import xml_helper
import file_helper

_project_root_path = None


def build(config, pro_root_path):
    _project_root_path = pro_root_path
    for key in config:
        value = config[key]
        if key == 'appId':
            modify_app_id(key)
        if key == 'appName':
            modify_app_name(value)
        if key == 'text':
            modify_text(value)
        if key == 'color':
            modify_color(value)
        if key == 'image':
            modify_image(value)
        if key == 'logo':
            modify_app_logo(value)
    pass


def modify_app_id(app_id):
    gradle_file_path = '%s/android/app/src/build.gradle' % _project_root_path

    file_data = ''
    with open(gradle_file_path, 'r') as f:
        for line in f:
            if 'applicationId' in line:
                old_id = line.split('\"')[1]
                line = line.replace(old_id, app_id)
            file_data += line

    with open(gradle_file_path, 'w') as f:
        f.write(file_data)
    pass


def modify_app_name(app_name):
    res_file_path = '%s/strings.xml' % get_android_res_dir('values')
    modify_xml_file(res_file_path, 'string', 'app_name', app_name)
    pass


def modify_text(texts):
    modify_json_file(get_js_res_file_path('text'), texts)
    pass


def modify_color(colors):
    modify_json_file(get_js_res_file_path('color'), colors)
    pass


def modify_image(images):
    for key in images:
        file_helper.copy_override(images[key], '%s/app/images' % _project_root_path)
    pass


# mdpi: 48
# hdpi: 72
# xhdpi: 96
# xxhdpi: 144
# xxxhdpi: 192
def modify_app_logo(images):
    for key in images:
        image = images[key]
        logo_dir_name = None
        if key == '48px':
            logo_dir_name = 'mipmap-mdpi'
        if key == '72px':
            logo_dir_name = 'mipmap-hdpi'
        if key == '96px':
            logo_dir_name = 'mipmap-xhdpi'
        if key == '144px':
            logo_dir_name = 'mipmap-xxhdpi'
        if key == '192px':
            logo_dir_name = 'mipmap-xxxhdpi'

        override_android_res(image, logo_dir_name)
    pass


def modify_json_file(file_path, configs):
    with open(file_path, 'r') as config_file_r:
        config_file = json.load(config_file_r)

    for key in configs:
        config_file[key] = configs[key]

    with open(file_path, 'w') as config_file_w:
        json.dump(config_file, config_file_w)
    pass


def override_android_res(res, res_dir_name):
    file_helper.copy_override(res, get_android_res_dir(res_dir_name))
    pass


def modify_xml_file(file_path, tag, node_name, value):
    tree = xml_helper.read_xml(file_path)
    nodes = xml_helper.find_nodes(tree, tag)
    result_nodes = xml_helper.get_node_by_keyvalue(nodes, {"name": node_name})
    xml_helper.change_node_text(result_nodes, value)
    xml_helper.write_xml(tree, file_path)


def get_js_res_file_path(category):
    return '%s/app/res/%s.json' % (_project_root_path, category)


def get_android_res_dir(category):
    return '%s/android/app/src/main/res/%s' % (_project_root_path, category)
