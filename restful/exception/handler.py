#-*- coding: utf-8 -*-
__author__ = 'iamsk'
__email__ = 'iamsk.info@gmail.com'

import logging
import random
from tornado.web import RequestHandler

from restful.macro import HTTP_CODE
from restful.exception import exceptions


def ExceptionHandler(func):
    def _ExceptionHandler(self, *args, **kwargs):
        try:
            info = func(self, *args, **kwargs)
            output = self.encoder(info)
            return self.finish(output)
        except exceptions.BadRequest, e:
            self.set_status(HTTP_CODE.BAD_REQUEST)
            logging.warning(e)
        except exceptions.Unauthorized, e:
            self.set_status(HTTP_CODE.UNAUTHORIZED)
            logging.warning(e)
        except exceptions.Forbidden, e:
            self.set_status(HTTP_CODE.FORBIDDEN)
            logging.warning(e)
        except exceptions.NotFound, e:
            self.set_status(HTTP_CODE.NOT_FOUND)
            logging.warning(e)
        except exceptions.MethodNotAllowed, e:
            self.set_status(HTTP_CODE.METHOD_NOT_ALLOWED)
            logging.warning(e)
        except exceptions.InternalServerError, e:
            self.set_status(HTTP_CODE.INTERNAL_SERVER_ERROR)
            logging.error(e, exc_info=True)
        except Exception, e:
            logging.error(e, exc_info=True)
            e = exceptions.InternalServerError(message=e.message)
            self.set_status(HTTP_CODE.INTERNAL_SERVER_ERROR)
        output = self.encoder(e.info)
        return self.finish(output)

    return _ExceptionHandler


class DemoHandler(RequestHandler):
    @ExceptionHandler
    def get(self, *args, **kwargs):
        exception_name_list = [exception_name for exception_name in dir(exceptions) if
                               not exception_name.startswith('__')]
        exception_name = random.choice(exception_name_list)
        e = getattr(exceptions, exception_name)
        raise e
