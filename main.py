#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.httpclient
import tornado.httpserver
import tornado.options
import os
import wdf

from tornado.template import Template

from tornado.options import define, options
define('port', default=9006, help='run the given port', type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', wdf.HomeHandler),
            (r'/s', wdf.SearchHandler)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()    

if __name__ == '__main__':
    main()
