# 
# Comando que llama a Python-Markdown para convertir un fichero 
# Markdown en HTML incluyendo un fichero CSS.
#
# Ejemplo de llamada:
#
# cd apuntes/software
# python3 ../generator.py software.md ../mads.css software.html
#
# Necesario: Python3 y Python-Markdown
#
# brew install python
# pip3 install markdown
#
# python-markown: https://python-markdown.github.io
# Extensiones: https://python-markdown.github.io/extensions/

import markdown, codecs, sys

output = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
"""

cssin = codecs.open(sys.argv[2], mode="r", encoding="utf-8")

output += cssin.read()

output += """
</head>

<body>
"""
mkin = open(sys.argv[1])
output += markdown.markdown(mkin.read(), extensions = ['admonition', 'extra', 'sane_lists', 'codehilite', 'pymdownx.superfences'])

output += """</body>

</html>
"""

outfile = codecs.open(sys.argv[3], "w",
                      encoding="utf-8",
                      errors="xmlcharrefreplace"
)
outfile.write(output)
outfile.close()
