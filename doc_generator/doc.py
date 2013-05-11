#-*- coding: utf-8 -*-

import os
import sys
import imp
import argparse
import requests
from tornado import template


def _gen(config):
    _APP_PATH = config['APP_PATH'].split(':')
    OBJ = _APP_PATH[1]
    FILE_PATH = _APP_PATH[0]
    _FILE_PATH = FILE_PATH.split('/')

    PARENT_PATH = '/'.join(_FILE_PATH[:-1])
    MODULE_NAME = _FILE_PATH[-1]

    sys.path.append(PARENT_PATH)

    module = imp.load_module(MODULE_NAME, *imp.find_module(MODULE_NAME))

    app = getattr(module, OBJ)

    group_urls = dict()
    info = {'title': config['TITLE'], 'base_url': config['BASE_URL'], 'version': config['VERSION'], 'group_urls': group_urls}

    for regex, obj in app.handlers:
        base_regex = regex.strip('/').split('/')[0]
        group_urls.setdefault(base_regex, dict())
        _regex = regex.replace('(\\d+)', '1')
        _regex = _regex.replace('(\\w+)', '1')
        request_url = config['BASE_URL'] + _regex
        r = requests.options(request_url)
        if r.status_code != 200:
            if r.status_code == 405:
                print regex, u'未实现 HTTP options 方法'
            else:
                print r.status_code, r.json()['error']['message']
            continue
        options = r.json()
        for option in options:
            if option['method'] in ['GET', 'DELETE']:
                r = requests.get(request_url, auth=('user', 'pass'))
                option['response'] = r.json()
                option['request'] = 'curl --basic %s:%s %s -X %s' % (config['USERNAME'], config['PASSWORD'], request_url, option['method'])
            else:
                option['response'] = ''
                option['request'] = 'curl --basic %s:%s %s -X %s' % (config['USERNAME'], config['PASSWORD'], request_url, option['method'])
        group_urls[base_regex][regex] = options

    TPL_DIR = os.path.realpath(os.path.dirname(__file__))
    loader = template.Loader(TPL_DIR)
    try:
        output = loader.load("doc.tpl").generate(**info)
        return output
    except Exception, e:
        print e
        print u'HTTP options method 返回格式不正确'
        return None


def init_doc_conf():
    import shutil

    os.mkdir('docs')
    shutil.copy('eggs/tornado-restful/doc_generator/doc.conf', 'docs')


def gen():
    parser = argparse.ArgumentParser(description='process args for doc gen', conflict_handler='resolve')
    parser.add_argument('--init', action='store_true', default=False, help='init config file for doc generator')
    parser.add_argument('-c', '--config', dest='config', type=str, default='docs/doc.conf', help='use config file for doc generator')
    config = dict()
    args = parser.parse_args()
    if args.init:
        init_doc_conf()
    else:
        try:
            execfile(args.config, config)
            output = _gen(config)
            if not output:
                return
            output_file = args.config.replace('.conf', '.md')
            with open(output_file, 'w') as f:
                f.write(output)
            _config = args.config.split('/')
            if len(_config) == 1:
                _dir = '.'
            else:
                _dir = '/'.join(_config[:-1])
            cmd = 'parts/restdown/restdown-master/bin/restdown -b parts/restdown/restdown-master/brand/api.no.de -m %s %s' % (_dir, output_file)
            os.system(cmd)
        except IOError:
            print 'you need `bin/do_gen --init` first; then change the docs/doc.conf as your wish'

if __name__ == '__main__':
    gen()
