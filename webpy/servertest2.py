# -*- coding:   UTF-8 -*-
"""
Primer ejemplo para web.py version 0.37
"""

import web
print web.__version__
# Directorio de plantillas:
render = web.template.render('templates/')

#url
urls = (
 # 'regex para url', 'clase donde se envia la peticion'
  '/', 'index'    
)

# Aplicacion donde se especifican las urls.
app = web.application(urls, globals())
 

 # Clase index:
class index:
        def GET(self):
            i = web.input(nombre=None)
            return render.index(i.nombre)
        
# Ejecutar app web.py
if __name__ == '__main__':
    app.run()

        