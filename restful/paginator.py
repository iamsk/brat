#!/usr/bin/env python
#-*- coding: utf-8 -*-

import logging
import time

from restful.utils import urlencode


def Paginator(get_pagination_kwargs, is_offset=True):
    def _Paginator(func):
        def do(*args, **kwargs):
            pkwargs = get_pagination_kwargs(func, *args, **kwargs)
            logging.debug(pkwargs)
            params = pkwargs['params']
            start_time = time.time()
            result = func(*args, **kwargs)
            cost_time = time.time() - start_time
            logging.debug('cost time: %s' % cost_time)
            info = {'data': result}
            if is_offset:
                previous_params = {
                    'offset': params['offset'] - params['limit'] if params['offset'] - params['limit'] > 0 else 0}
                next_params = {'offset': params['offset'] + params['limit']}
            else:
                previous_params = {'before_id': result[0]['pageing_id'] if result else 0}
                next_params = {'after_id': result[-1]['pageing_id'] if result else 0}
            try:
                del params['offset']  # 删除原 offset，将被替换为新的
            except Exception:
                pass
            previous_params.update(**params)
            next_params.update(**params)
            info['paging'] = {
                'previous': '?'.join([pkwargs['base_url'], urlencode(previous_params)]),
                'next': '?'.join([pkwargs['base_url'], urlencode(next_params)])
            }
            return info

        return do

    return _Paginator
