#!/usr/bin/env python

import web
rutas = (
    '/', 'hola'
)
app = web.application(rutas, globals())

class hola:
   def GET(self):

     return """
     <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
     <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="es" lang="es">
     <head>
     <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
         <title>Hola Mundo...</title>
         <style type="text/css" media="screen">
           h1 {text-align:center; color: #444;}
         </style>
    </head>
     <body>
       <h1>Hola Web.py</h124     </body>
     </html>
    """

if __name__ == '__main__':
   app.run()